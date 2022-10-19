
import ltcode as lt
from ltcode import LOG


if __name__ == "__main__":
    fileName = "data/hat-768x512.png"

    fileBlocks, fileBlocksN, dropQuantity = lt.load_files(fileName, 512)

    fileSymbols = lt.create_symbols(fileBlocks, dropQuantity)



    LOG.Basic("DECODE", "Start Decode")

    recoveredBlocks, recoverdN = lt.decode(fileSymbols, blocks_quantity=fileBlocksN)

    LOG.Basic("DECODE", "End Decode")
