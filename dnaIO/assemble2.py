from . import Symbol, LOG, AssembleConverter1
import hashlib

from collections import defaultdict
import numpy as np

class AssembleConverter2(AssembleConverter1):

    def __init__(self):
        super(AssembleConverter2, self).__init__("Rate")

    def symbol_to_bytes(self, symbol: Symbol) -> bytearray:
        # degree/32 index/32 data/:
        # degreeBit32 = self.int_to_bit32(symbol.degree)
        indexBit32 = self.int_to_bit32(symbol.index)
        dataBits = bytearray(bytes(symbol.data))

        if symbol.index == 0:
            sizeValue = self.fileSize % (2 ** 32)
            sizeBit32 = self.int_to_bit32(sizeValue)
            countValue = self.blocksN % (2 ** 32)
            countBit32 = self.int_to_bit32(countValue)
            return indexBit32 + sizeBit32 + countBit32 + dataBits
        else:
            return indexBit32 + dataBits

    def bytes_to_symbow(self, arr: bytearray) -> Symbol or None:
        # 32-bit * 1
        # index/32 size/32 count/32 data/:
        # index/32 data/:

        indexBit32 = arr[0:4]
        # degree = self.bit32_to_int(degreeBit32)
        index = self.bit32_to_int(indexBit32)
        if index == 0:
            fileBit32 = arr[4:8]
            self.fileSize = self.bit32_to_int(fileBit32)
            countBit32 = arr[8:12]
            self.blocksN = self.bit32_to_int(countBit32)
            dataBits = arr[12:]
            dataSymbol = np.frombuffer(dataBits, dtype=Symbol.NUMPY_TYPE)
            sym = Symbol(index=index,
                         degree=0,
                         data=dataSymbol,
                         fileSize=self.fileSize,
                         blocksN=self.blocksN)
            return sym
        else:
            dataBits = arr[4:]
            dataSymbol = np.frombuffer(dataBits, dtype=Symbol.NUMPY_TYPE)
            sym = Symbol(index=index,
                         degree=0,
                         data=dataSymbol,
                         fileSize=self.fileSize,
                         blocksN=self.blocksN
            )
            return sym

    def convert_bytes_form_symbols(self, symbols, fileSize, blocksN) -> [bytearray]:
        LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Start use: %s" % self.name)
        self.clear()
        self.fileSize = fileSize
        self.blocksN = blocksN
        result = []
        for sym in symbols:
            bits = self.symbol_to_bytes(sym)
            result.append(bits)
        LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Finish")
        return result

    def convert_symbols_from_bitArray(self, arr: [bytearray]) -> ([Symbol], int, int):
        LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols Start use: %s" % self.name)
        self.clear()

        symbolSet = defaultdict(list)
        for bits in arr:
            try:
                sym = self.bytes_to_symbow(bits)
            except Exception as err:
                sym = None
            if sym is not None:
                index = sym.index
                symbolSet[index].append(sym)

        result = []
        for syms in symbolSet.values():
            sym = self.rate_hash(syms)
            if sym is not None:
                result.append(sym)

        result = self.rate_length(result)

        for sym in result:
            if sym.index == 0:
                self.blocksN = sym.blocksN
                self.fileSize = sym.fileSize

        LOG.Basic("ASSEM-DECODE", "Parse Legal Symbol: %d -> %d" % (len(arr), len(result)))
        LOG.Basic("ASSEM-DECODE", "Parse FileSize: %d BlockN: %d" % (self.fileSize, self.blocksN))
        LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols FINISH")
        return result, self.fileSize, self.blocksN

    def rate_hash(self, syms: [Symbol]) -> Symbol or None:
        hashs = {}
        for sym in syms:
            hash0 = sym.datahash
            if hash0 in hashs.keys():
                hashs[hash0].append(sym)
            else:
                hashs[hash0] = [sym]

        maxSyms = []
        for syms in hashs.values():
            if len(syms) >= len(maxSyms):
                maxSyms = syms
        if len(maxSyms) == 0:
            return None
        else:
            return maxSyms[0]

    def rate_length(self, syms: [Symbol]) -> [Symbol]:

        pack = defaultdict(list)
        for sym in syms:
            length = len(sym.data)
            pack[length].append(sym)

        maxSyms = []
        for syms in pack.values():
            if len(syms) >= len(maxSyms):
                maxSyms = syms
        return maxSyms
