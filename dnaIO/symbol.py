
import random
from .basic import LOG
import numpy as np

class Symbol:
    __slots__ = ["index", "degree", "data", "neighbors"] # fixing attributes may reduce memory usage

    NUMPY_TYPE = np.uint64

    def __init__(self, index, degree, data):
        # seed
        self.index = index

        # 关联的block数量
        self.degree = degree
        self.data = data