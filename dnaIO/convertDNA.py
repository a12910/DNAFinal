from . import DNAStr, LOG
import random

# Base
class DNAConverter:

    def __init__(self, name):
        self.style = False
        self.name = name

    def byteArray_to_DNA(self, arr: bytearray) -> DNAStr:
        return DNAStr("")

    def DNA_to_byteArray(self, dna: DNAStr) -> bytearray:
        result = bytearray([])
        return result

    def clear(self):
        pass

def convert_dnaArr_from_bitArr(arr: [bytearray], conv: DNAConverter) -> [DNAStr]:
    result = []
    LOG.Basic("DNA-ENCODE", "Convert Bytes->DNA Start use: %s" % conv.name)
    dnaCount = 0
    for bits in arr:
        dna = conv.byteArray_to_DNA(bits)
        result.append(dna)
        dnaCount += len(dna.data)
    LOG.Basic("DNA-ENCODE", "Convert Bytes->DNA Finish Count: %d/%d=%d" % (dnaCount, len(arr), int(dnaCount / len(arr))))
    return result


def convert_bitArr_from_DNAs(DNAs: [DNAStr], conv: DNAConverter) -> [bytearray]:
    result = []
    LOG.Basic("DNA-DECODE", "Convert DNA->Bytes Start use: %s" % conv.name)
    for dna in DNAs:
        bits = conv.DNA_to_byteArray(dna)
        result.append(bits)
    LOG.Basic("DNA-DECODE", "Convert DNA->Bytes Finish")
    return result
