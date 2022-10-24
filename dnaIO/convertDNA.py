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

    @staticmethod
    def compute_cgRatio(dna: DNAStr) -> float:
        count = 0
        for item in dna.data:
            if item in "CG":
                count += 1
        return count / len(dna.data)

def convert_dnaArr_from_bitArr(arr: [bytearray], conv: DNAConverter) -> [DNAStr]:
    result = []
    cgRatios = []

    LOG.Basic("DNA-ENCODE", "Convert Bytes->DNA Start use: %s" % conv.name)
    dnaCount = 0
    conv.clear()
    for bits in arr:
        dna = conv.byteArray_to_DNA(bits)
        result.append(dna)
        dnaCount += len(dna.data)

        cgRatio = DNAConverter.compute_cgRatio(dna)
        cgRatios.append(cgRatio)

    import numpy as np
    counts = np.percentile(cgRatios, (0, 25, 50, 75, 99), interpolation='midpoint')

    LOG.Basic("DNA-ENCODE", "Convert Bytes->DNA Finish Count: %d/%d=%d" % (dnaCount, len(arr), int(dnaCount / len(arr))))
    LOG.Basic("DNA-ENCODE", "Convert Bytes->DNA CGRatio: %.3f %.3f %.3f %.3f %.3f" % (counts[0], counts[1], counts[2], counts[3], counts[4]))
    return result


def convert_bitArr_from_DNAs(DNAs: [DNAStr], conv: DNAConverter) -> [bytearray]:
    result = []
    conv.clear()
    LOG.Basic("DNA-DECODE", "Convert DNA->Bytes Start use: %s" % conv.name)
    for dna in DNAs:
        bits = conv.DNA_to_byteArray(dna)
        result.append(bits)
    LOG.Basic("DNA-DECODE", "Convert DNA->Bytes Finish")
    return result
