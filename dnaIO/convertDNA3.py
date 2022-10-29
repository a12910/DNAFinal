
from . import DNAStr, DNAConverter, DNAConverter2

class DNAConverter3(DNAConverter2):

    useDynamicMap = True

    def __init__(self, name=""):
        name1 = name if name != "" else "Same3"
        super(DNAConverter3, self).__init__(name1)

        self.ATMap = {
            "A": ["TA", "C", "TC", "G"],
            "C": ["A", "TC", "TG", "G"],
            "T": ["AT", "C", "AG", "G"],
            "G": ["A", "C", "TA", "TG"]
        }
        self.CGMap = {
            "A": ["CA", "GC", "T", "G"],
            "C": ["A", "GC", "T", "AG"],
            "T": ["A", "C", "GT", "GC"],
            "G": ["A", "CA", "T", "CG"]
        }

    def DNA8_to_bit(self, char: str):
        if len(self.last) == 2:
            last1, last2 = self.last
            if last1 == last2:
                dic = self.get_Map()[last1]
                if char in dic:
                    index = dic.index(char)
                    self.add_byte(index)
                    self.add_count(char)
                    self.last = [last2, char]
                else:
                    self.last.append(char)
            else:
                index = self.get_keyValue(char)
                self.add_byte(index)
                self.add_count(char)
                self.last = [last2, char]
        else:
            last1, last2, last3 = self.last
            dic = self.get_Map()[last1]
            key1 = last3 + char
            if key1 in dic:
                index = dic.index(key1)
                self.add_byte(index)
                self.add_count(key1)
                self.last = [last3, char]
            else:
                raise Exception("")

    def DNA_to_byteArray(self, dna: DNAStr) -> bytearray:
        self.clear()
        for char in dna.data:
            self.DNA8_to_bit(char)
        return self.byteResult

