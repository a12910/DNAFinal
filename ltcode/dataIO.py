import os
from . import PACKET_SIZE, blocks_read, encode
from . import LOG

def load_files(fileName, blockSize):
    file = open(fileName, 'rb')

    PACKET_SIZE = blockSize
    fileSize = os.path.getsize(fileName)

    LOG.Basic("INIT", "Filesize: {} bytes".format(fileSize))
    fileBlocks = blocks_read(file, fileSize)
    fileBlocksN = len(fileBlocks)
    dropQuantity = fileBlocksN * 2

    LOG.Basic("INIT", "Blocks: {} -> {} * {} bytes".format(fileBlocksN, dropQuantity, PACKET_SIZE))

    file.close()
    return fileBlocks, fileBlocksN, dropQuantity

def create_symbols(fileBlocks, dropQuantity):
    LOG.Basic("ENCODE", "Start Encode")
    fileSymbols = []
    for symbol in encode(fileBlocks, drops_quantity=dropQuantity):
        fileSymbols.append(symbol)
    LOG.Basic("ENCODE", "End Encode")
    return fileSymbols
