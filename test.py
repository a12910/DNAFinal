import ltcode as lt
from ltcode import LOG
import pandas as pd
import dnaIO as dna
import os


if __name__ == "__main__":

    # data/bistreams 原始txt数据
    # data/bitfiles  txt数据转化为二进制数据
    # data/bitout    对应DNA结果

    files = list(os.walk("data/bistreams"))[0][2]
    data = []
    for fileName in files:
        inFile = "data/bistreams/" + fileName
        tmpFile = "data/bitfiles/" + fileName
        outFile = "data/bitout/" + fileName

        with open(inFile, "r") as obj:
            texts = obj.read().replace("\n", "").split(" ")
            bytes = bytearray([])
            for text in texts:
                if text == "":
                    continue
                byte = int(text, 2)
                bytes.append(byte)
            with open(tmpFile, "wb") as obj2:
                obj2.write(bytes)

        dnaConv = dna.DNAConverter2()
        byteConv = dna.AssembleConverter2()

        LOG.Basic("INIT", "File Name; %s" % fileName)

        hashInit = dna.compute_file_hash(tmpFile)
        LOG.Basic("INIT", "File Hash: %s" % hashInit)

        # 载入并切分文件
        fileBlocks, fileBlocksN, dropQuantity, fileSize = lt.load_files(tmpFile, 56, 2)

        # 生成喷泉码
        # fileBlocksN = fileBlocks * dropQuantity
        fileSymbols = lt.create_symbols(fileBlocks, dropQuantity)

        # 生成拼接比特流
        bitsArr = byteConv.convert_bytes_form_symbols(fileSymbols, fileSize, blocksN=fileBlocksN)

        # 生成DNAArr
        dnaArr = dna.convert_dnaArr_from_bitArr(bitsArr, conv=dnaConv)

        dnas = ""
        with open(outFile, "w") as obj:
            for dnaa in dnaArr:
                obj.write(dnaa.data + "\n")
                dnas += dnaa.data

        # 平均dna链长
        average_dna = len(dnas) / len(fileSymbols)

        countA = "%.4f" % (dnas.count('A') / len(dnas))
        countC = "%.4f" % (dnas.count('C') / len(dnas))
        countT = "%.4f" % (dnas.count('T') / len(dnas))
        countG = "%.4f" % (dnas.count('G') / len(dnas))

        compress = "%.4f" % (60 * 8 / average_dna)

        data.append([fileName, fileSize, fileBlocksN, len(fileSymbols), average_dna,
                     countA, countC, countT, countG, compress])

    df = pd.DataFrame(data, columns=['文件名', '文件大小', "文件块数", "lt码块数/DNA链数", "平均DNA长度",
                                     "A含量", "C含量", "T含量", "G含量", "byte压缩率"])
    df.to_csv("data/bitout/statics.csv")
