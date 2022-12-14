
from . import DNAStr, LOG, DNAConverter
import random

class DNAConverter1(DNAConverter):

    def __init__(self):
        super(DNAConverter1, self).__init__("01->AC/TG")
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
        result2 = ""
        rest = bit8
        for index in range(8):
            result = self.rand_bit(rest % 2 == 1) + result
            result2 = str(rest % 2) + result2
            rest = rest // 2
        return DNAStr(result)

    def rand_bit(self, bit: bool) -> str:
        if bit:
            return random.choice(['T', 'G'])
        else:
            return random.choice(['A', 'C'])

    def DNA8_to_bit8(self, strr: DNAStr) -> int:
        result = 0
        for char in strr.data:
            result *= 2
            if char == 'T' or char == 'G':
                result += 1
        return result

    @staticmethod
    def convertDNA_test(arr: bytearray):
        conv = DNAConverter1()
        dna = conv.byteArray_to_DNA(arr)
        print(dna)
        arr2 = conv.DNA_to_byteArray(dna)
        print(arr, arr2)

    def clear(self):
        pass