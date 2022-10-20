
from . import DNAStr, LOG
import random

class DNAConverter:

    def __init__(self):
        self.style = False

    def byteArray_to_DNA(self, arr: bytearray) -> DNAStr:
        result = DNAStr("")
        for value in arr:
            result += self.bit8_to_DNA(value)
        return result

    def DNA_to_byteArray(self, dna: DNAStr) -> bytearray:
        result = bytearray([])
        count = len(dna.data)
        for index in range(0, count, 8):
            part = dna.slice(index, 8)
            result.append(self.DNA8_to_bit8(part))
        return result

    def bit8_to_DNA(self, bit8: int) -> DNAStr:
        # 0-> A/C 1-> T/G
        result = ""
        count = 128
        rest = bit8
        while count > 1:
            result += self.rand_bit(rest > count)
            rest = rest % count
            count = count // 2
        return DNAStr(result)

    def rand_bit(self, bit: bool) -> str:
        if bit:
            return random.choice(['T', 'G'])
        else:
            return random.choice(['A', 'C'])

    def DNA8_to_bit8(self, strr: DNAStr) -> int:
        result = 0
        for char in strr.data[::-1]:
            result *= 2
            if char == 'T' or char == 'G':
                result += 1
        return result

def convert_dnaArr_from_bitArr(arr: [bytearray]) -> [DNAStr]:
    result = []
    LOG.Basic("DNA-ENCODE", "Convert DNA Start")
    conv = DNAConverter()
    for bits in arr:
        dna = conv.byteArray_to_DNA(bits)
        result.append(dna)
    LOG.Basic("DNA-ENCODE", "Convert DNA Finish")
    return result

def convert_bitArr_from_DNAs(DNAs: [DNAStr]) -> [bytearray]:
    result = []
    LOG.Basic("DNA-DECODE", "Convert Bytes Start")
    conv = DNAConverter()
    for dna in DNAs:
        bits = conv.DNA_to_byteArray(dna)
        result.append(bits)
    LOG.Basic("DNA-DECODE", "Convert DNA Finish")
    return result
