from . import DNAStr, LOG
import random

def destory_DNAs(DNAs: [DNAStr], lost: float, pcr: int) -> [DNAStr]:
    result = []
    for index in range(pcr):
        for dna in DNAs:
            if random.random() > lost:
                result.append(dna)
    LOG.Basic("DESTORY", "Destroy DNA %d --PCR-> %d --Destory(%f)-> %d" % (len(DNAs), len(DNAs) * pcr, lost, len(result)))
    return result
