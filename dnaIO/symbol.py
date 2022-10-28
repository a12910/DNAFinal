
import hashlib
import numpy as np

class Symbol:
    # __slots__ = ["index", "degree", "data", "datahash"]
    # fixing attributes may reduce memory usage

    NUMPY_TYPE = np.uint64

    def __init__(self, index, degree, data, fileSize, blocksN):
        # seed
        self.index = index

        # 关联的block数量
        self.degree = degree
        self.data = data
        self.datahash = self.get_byteHash(data)
        self.fileSize = fileSize
        self.blocksN = blocksN

    def get_byteHash(self, arr: bytearray) -> int:
        md5 = hashlib.md5(arr).hexdigest()
        md5Value = int(md5, 16)
        return md5Value
