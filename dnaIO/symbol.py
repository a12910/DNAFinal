
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

    def log(self, blocks_quantity):
        neighbors, _ = self.generate_indexes(self.index, self.degree, blocks_quantity)
        LOG.Basic("SYMBOL", "symbol_{} degree={}\t {}".format(self.index, self.degree, neighbors))

    def generate_indexes(self, symbol_index, degree, blocks_quantity):
        """Randomly get `degree` indexes, given the symbol index as a seed

        Generating with a seed allows saving only the seed (and the amount of degrees)
        and not the whole array of indexes. That saves memory, but also bandwidth when paquets are sent.

        The random indexes need to be unique because the decoding process uses dictionnaries for performance enhancements.
        Additionnally, even if XORing one block with itself among with other is not a problem for the algorithm,
        it is better to avoid uneffective operations like that.

        To be sure to get the same random indexes, we need to pass
        """
        if symbol_index < blocks_quantity:
            indexes = [symbol_index]
            degree = 1
        else:
            random.seed(symbol_index)
            indexes = random.sample(range(blocks_quantity), degree)

        return indexes, degree