
from . import DNAStr, DNAConverter

class DNAConverter2(DNAConverter):

    useDynamicMap = True

    def __init__(self):
        super(DNAConverter2, self).__init__("Same2")
        self.CGCount = 0
        self.ATCount = 0

        self.ATMap = {
            "A": ["TA", "TC", "TT", "TG"],
            "C": ["AA", "AT", "TT", "TA"],
            "T": ["AA", "AC", "AT", "AG"],
            "G": ["AA", "AT", "TT", "TA"]
        }
        self.CGMap = {
            "A": ["CG", "CC", "GC", "GG"],
            "C": ["GA", "GC", "GT", "GG"],
            "T": ["CG", "CC", "GC", "GG"],
            "G": ["CA", "CC", "CT", "CG"]
        }

        self.last = ["A", "T"]
        self.dnaResult = DNAStr("")
        self.byteResult = bytearray([])

        self.byteAche = 0
        self.byteAcheIndex = 0

    def __add_dna(self, dna: str):
        if len(dna) == 1:
            self.last = [self.last[1], dna[0]]
        else:
            self.last = [dna[0], dna[1]]

        self.dnaResult.add(dna)
        self.__add_count(dna)

    def __add_count(self, dna: str):
        for char in dna:
            if char in "AT":
                self.ATCount += 1
            else:
                self.CGCount += 1

    def byteArray_to_DNA(self, arr: bytearray) -> DNAStr:
        self.clear()
        for value in arr:
            self.__bit8_to_DNA(value)
        return self.dnaResult

    def __bit8_to_DNA(self, bit8: int):
        bits = [bit8 // 64, (bit8 % 64) // 16, (bit8 % 16) // 4, bit8 % 4]
        for bit in bits:
            last1, last2 = self.last
            if last1 == last2:
                char = self.__get_Map()[last1][bit]
            else:
                char = self.__get_keyDNA(bit)
            self.__add_dna(char)

    def DNA_to_byteArray(self, dna: DNAStr) -> bytearray:
        self.clear()
        for char in dna.data:
            self.__DNA8_to_bit(char)
        return self.byteResult

    def __DNA8_to_bit(self, char: str):

        if len(self.last) == 2:
            last1, last2 = self.last
            if last1 == last2:
                self.last.append(char)
            else:
                self.__add_byte(self.__get_keyValue(char))
                self.__add_count(char)
                self.last = [last2, char]
        else:
            last1, last2, last3 = self.last
            dic = self.__get_Map()[last1]
            key = last3 + char
            index = dic.index(key)
            self.__add_byte(index)
            self.__add_count(key)
            self.last = [last3, char]

    def __add_byte(self, bit2: int):
        self.byteAche += 4 ** (3 - self.byteAcheIndex) * bit2
        if self.byteAcheIndex == 3:
            self.byteResult.append(self.byteAche)
            self.byteAche = 0
            self.byteAcheIndex = 0
        else:
            self.byteAcheIndex += 1

    def clear(self):
        super(DNAConverter2, self).clear()
        self.CGCount = 0
        self.ATCount = 0
        self.last = ["A", "T"]
        self.dnaResult = DNAStr("")
        self.byteResult = bytearray([])
        self.byteAche = 0
        self.byteAcheIndex = 0

    def __get_dynamicIndex(self) -> int:
        index = (self.CGCount + self.ATCount) // 7 % 19 % 4
        if not self.useDynamicMap:
            index = 0
        return index

    def __get_keyDNA(self, value: int) -> str:
        index = self.__get_dynamicIndex()
        if not self.useDynamicMap:
            index = 0
        keys = "ACTG"
        return keys[(index + value) % 4]

    def __get_keyValue(self, dna1: str) -> int:
        index = self.__get_dynamicIndex()

        value = "ACTG".index(dna1)
        return (value - index + 4) % 4

    def __is_CGMap(self) -> bool:
        # 是否为需要补充CG的Map
        return self.CGCount < self.ATCount * 0.9

    def __get_Map(self) -> {}:
        return self.CGMap if self.__is_CGMap() else self.ATMap
