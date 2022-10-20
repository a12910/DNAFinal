

class DNASymbol:
    def __init__(self):
        self.data = bytearray()

    def loadData(self, binData: bytearray):
        self.data = binData

    def loadDNA(self, dnaStr):
        pass

    def print(self) -> str:
        # A00 C01 T10 G11
        dataLength = len(self.data)
        result = ""
        for index in range(dataLength):
            result += self.byte_to_dna(self.data[index])
        return result

    def byte_to_dna(self, byte: int) -> str:
        keys = ['A', 'C', 'T', 'G']
        result = [ keys[byte // 64],
                   keys[byte & 48 // 32],
                   keys[byte & 12 // 8],
                   keys[byte % 4]]
        return "".join(result)

    def dna_to_byte(self, strr4: str) -> int:
        return 0
