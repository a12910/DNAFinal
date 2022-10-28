from . import DNAStr, DNAConverter, DNAConverter2

class DNAConverter3(DNAConverter2):

    def __init__(self):
        super(DNAConverter3, self).__init__("name3")

    def byteArray_to_DNA(self, arr: bytearray) -> DNAStr:
        pass

    def DNA_to_byteArray(self, dna: DNAStr) -> bytearray:
        arr = super(DNAConverter3, self).DNA_to_byteArray(dna)
        return arr
