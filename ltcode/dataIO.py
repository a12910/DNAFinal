import os
from . import blocks_read, encode, decode, core
from . import LOG


def load_files(fileName, blockSize, quantityRatio):
    file = open(fileName, 'rb')

    core.PACKET_SIZE = blockSize
    fileSize = os.path.getsize(fileName)

    LOG.Basic("INIT", "Filesize: {} bytes".format(fileSize))
    fileBlocks = blocks_read(file, fileSize)
    fileBlocksN = len(fileBlocks)
    dropQuantity = fileBlocksN * quantityRatio

    LOG.Basic("INIT", "Blocks: {} -> {} * {} bytes".format(fileBlocksN, dropQuantity, core.PACKET_SIZE))

    file.close()
    return fileBlocks, fileBlocksN, dropQuantity, fileSize


def create_symbols(fileBlocks, dropQuantity):
    LOG.Basic("ENCODE", "Start Encode")
    fileSymbols = []
    for symbol in encode(fileBlocks, drops_quantity=dropQuantity):
        fileSymbols.append(symbol)
    LOG.Basic("ENCODE", "End Encode")
    return fileSymbols


def decode_from_symbols(symbols, blocks_quantity):
    LOG.Basic("DECODE", "Start Decode")
    recoveredBlocks, recoverdN = decode(symbols, blocks_quantity=blocks_quantity)
    LOG.Basic("DECODE", "End Decode")
    return recoveredBlocks, recoverdN
