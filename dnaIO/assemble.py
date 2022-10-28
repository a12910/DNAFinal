from . import Symbol, LOG
import hashlib
import numpy as np

class AssembleConverter:

    def __init__(self, name):
        self.fileSize = 0
        self.name = name
        self.blocksN = 0

    def clear(self):
        self.fileSize = 0
        self.blocksN = 0

    def symbol_to_bytes(self, symbol: Symbol) -> bytearray:
        return bytearray([])

    def bytes_to_symbow(self, arr: bytearray) -> Symbol or None:
        return None

    def convert_bytes_form_symbols(self, symbols, fileSize, blocksN) -> [bytearray]:
        LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Start use: %s" % self.name)
        LOG.Basic("ASSEM-ENCODE", "Convert Symbol->Bytes Finish")
        return []


    def convert_symbols_from_bitArray(self, arr: [bytearray]) -> ([Symbol], int, int):
        LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols Start use: %s" % self.name)
        LOG.Basic("ASSEM-DECODE", "Parse Legal Symbol: %d / %d -> %d" % (0, len(arr), 0))
        LOG.Basic("ASSEM-DECODE", "Parse FileSize: %d BlockN: %d" % (self.fileSize, self.blocksN))
        LOG.Basic("ASSEM-DECODE", "Convert Bytes->Symbols FINISH")
        return [], self.fileSize, self.blocksN
