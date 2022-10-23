from . import Symbol, LOG
import hashlib
import numpy as np

class AssembleConverter:

    def __init__(self, fileSize: int, blockN: int):
        self.fileSize = fileSize
        self.blockN = blockN

    def symbol_to_bytes(self, symbol: Symbol) -> bytearray:
        # hash/32 degree/32 index/32 data/:
        # degreeBit32 = self.int_to_bit32(symbol.degree)
        indexBit32 = self.int_to_bit32(symbol.index)
        dataBits = bytearray(bytes(symbol.data))

        if symbol.index == 0:
            sizeValue = self.fileSize % (2 ** 32)
            sizeBit32 = self.int_to_bit32(sizeValue)
            countValue = self.blockN % (2 ** 32)
            countBit32 = self.int_to_bit32(countValue)

            hashTest = indexBit32 + sizeBit32 + countBit32 + dataBits
            hashValue = self.get_byteHash(hashTest)
            hashBit32 = self.int_to_bit32(hashValue)
            return hashBit32 + hashTest
        else:
            hashTest = indexBit32 + dataBits
            hashValue = self.get_byteHash(hashTest)
            hashBit32 = self.int_to_bit32(hashValue)
            return hashBit32 + hashTest

    def bytes_to_symbow(self, arr: bytearray) -> Symbol or None:
        # 32-bit * 3
        # hash/32 degree/32 index/32 size/32 count/32 data/:
        # hash/32 degree/32 index/32 data/:

        hashBit32 = arr[:4]
        hashTest = arr[4:]
        hashValue = self.bit32_to_int(hashBit32)
        hastResult = self.get_byteHash(hashTest)
        if hastResult != hashValue:
            return None

        # degreeBit32 = arr[4:8]
        indexBit32 = arr[4:8]
        # degree = self.bit32_to_int(degreeBit32)
        index = self.bit32_to_int(indexBit32)
        if index == 0:
            fileBit32 = arr[8:12]
            self.fileSize = self.bit32_to_int(fileBit32)
            countBit32 = arr[12:16]
            self.blockN = self.bit32_to_int(countBit32)
            dataBits = arr[16:]
            dataSymbol = np.frombuffer(dataBits, dtype=Symbol.NUMPY_TYPE)
            sym = Symbol(index=index,
                         degree=0,
                         data=dataSymbol)
            return sym
        else:
            dataBits = arr[8:]
            dataSymbol = np.frombuffer(dataBits, dtype=Symbol.NUMPY_TYPE)
            sym = Symbol(index=index,
                         degree=0,
                         data=dataSymbol)
            return sym

    def get_byteHash(self, arr: bytearray):
        md5 = hashlib.md5(arr).hexdigest()
        md5Value = int(md5[:16], 16)
        return md5Value % (2 ** 16)

    def int_to_bit32(self, value: int) -> bytearray:
        result = bytearray([])
        rest = value
        for index in range(4):
            modd = rest % 256
            rest = rest // 256
            result = bytearray([modd]) + result
        return result

    def bit32_to_int(self, bit32: bytearray) -> int:
        result = 0
        for index in range(4):
            result *= 256
            result += bit32[index]
        return result

    @staticmethod
    def assemble_test(value) -> bytearray:
        conv = AssembleConverter(0, 0)
        arr = conv.int_to_bit32(value)
        print(arr)
        value2 = conv.bit32_to_int(arr)
        print(value, value2)
        return arr



def convert_bytes_form_symbols(symbols, fileSize, blocksN) -> [bytearray]:
    LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Start")
    conv = AssembleConverter(fileSize, blocksN)
    result = []
    for sym in symbols:
        bits = conv.symbol_to_bytes(sym)
        result.append(bits)
    LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Finish")
    return result


def convert_symbols_from_bitArray(arr: [bytearray]) -> ([Symbol], int, int):
    result = []
    LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols Start")
    conv = AssembleConverter(0, 0)
    for bits in arr:
        sym = conv.bytes_to_symbow(bits)
        if sym is not None:
            result.append(sym)
    LOG.Basic("ASSEM-DECODE", "Parse Legal Symbol: %d / %d" % (len(result), len(arr)))
    LOG.Basic("ASSEM-DECODE", "Parse FileSize: %d BlockN: %d" % (conv.fileSize, conv.blockN))
    LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols FINISH")
    return result, conv.fileSize, conv.blockN

