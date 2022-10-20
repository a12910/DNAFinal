
import ltcode as lt
from ltcode import LOG
import dnaIO as dna

if __name__ == "__main__":
    fileName = "data/hat-768x512.png"
    outFile = "data/hat-768x512-out.png"

    hashInit = dna.compute_file_hash(fileName)
    LOG.Basic("INIT", "File Hash: %s" % hashInit)

    # 载入并切分文件
    fileBlocks, fileBlocksN, dropQuantity, fileSize = lt.load_files(fileName, 512)

    # 生成喷泉码
    fileSymbols = lt.create_symbols(fileBlocks, dropQuantity)

    # 生成拼接比特流
    bitsArr = dna.convert_bytes_form_symbols(fileSymbols, fileSize, blocksN=fileBlocksN)

    # 生成DNAArr
    dnaArr = dna.convert_dnaArr_from_bitArr(bitsArr)

    # 进行模拟损毁
    dnaArrOut = dna.destory_DNAs(dnaArr, 0.05, 10)

    # 使用DNA进行恢复为比特流
    bitsArrOut = dna.convert_bitArr_from_DNAs(dnaArrOut)

    # 从比特流恢复到喷泉码
    symbolsOut, fileSizeOut, fileBlocksNOut = dna.convert_symbols_from_bitArray(bitsArrOut)

    # 使用喷泉码进行恢复
    recoveredBlocks, recoverdN = lt.decode_from_symbols(symbolsOut, fileBlocksNOut)

    # 导出恢复的文件
    with open(outFile, "wb") as file:
        lt.blocks_write(recoveredBlocks, file, fileSizeOut)

    hashOut = dna.compute_file_hash(outFile)
    LOG.Basic("FINISH", "OutFile Hash: %s" % hashOut)
