from . import DNAStr, LOG
import random

def destory_DNAs(DNAs: [DNAStr], lost: float, pcr: int, replace: float) -> [DNAStr]:
    result = []
    for index in range(pcr):
        for dna in DNAs:
            if random.random() > lost:
                if random.random() < replace:
                    result.append(replace_DNA(dna, replace))
                else:
                    result.append(dna)

    LOG.Basic("DESTORY", "Destroy DNA %d --PCR-> %d --Destory(%f)-> %d" % (len(DNAs), len(DNAs) * pcr, lost, len(result)))
    return result


def replace_DNA(dna: DNAStr, ratio: float) -> DNAStr:
    data = ""
    for d in dna.data:
        result = d
        if random.random() < ratio:
            choice = random.randrange(0, 3)
            # 替换
            if choice == 0:
                result = random.choice("ACTG")

            # 增加
            if choice == 1:
                result += random.choice("ACTG")

            # 删除
            if choice == 2 < ratio:
                result = ""
        data += result
    return DNAStr(data)
