from .distributions import *
from .basic import LOG
from .symbol import Symbol as Sym
import random

def get_degrees_from(distribution_name, N, k):
    """ Returns the random degrees from a given distribution of probabilities.
    The degrees distribution must look like a Poisson distribution and the 
    degree of the first drop is 1 to ensure the start of decoding.
    """

    if distribution_name == "ideal":
        probabilities = ideal_distribution(N)
    elif distribution_name == "robust":
        probabilities = robust_distribution(N)
    else:
        probabilities = None

    random.seed(N)
    population = list(range(0, N+1))
    return [1] + random.choices(population, probabilities, k=k-1)
   
def encode(blocks, drops_quantity):
    """ Iterative encoding - Encodes new symbols and yield them.
    Encoding one symbol is described as follow:

    1.  Randomly choose a degree according to the degree distribution, save it into "deg"
        Note: below we prefer to randomly choose all the degrees at once for our symbols.

    2.  Choose uniformly at random 'deg' distinct input blocs. 
        These blocs are also called "neighbors" in graph theory.
    
    3.  Compute the output symbol as the combination of the neighbors.
        In other means, we XOR the chosen blocs to produce the symbol.
    """

    # Display statistics
    blocks_n = len(blocks)
    assert blocks_n <= drops_quantity, "Because of the unicity in the random neighbors, it is need to drop at least the same amount of blocks"

    LOG.Basic("LT-ENCODE", "Generating graph...")
    start_time = time.time()

    # Generate random indexes associated to random degrees, seeded with the symbol id
    # [1] + 以robust概率分布选择1到n中k个可重复元素
    # [1, 2, 2, 4, 1, ...]

    random_degrees = get_degrees_from("robust", blocks_n, k=blocks_n * 2)
    LOG.Basic("LT-ENCODE", "Ready for encoding.")

    for i in range(drops_quantity):
        
        # Get the random selection, generated precedently (for performance)
        # i: 生成的第i个元素
        # degrees[i]:上面生成了drops个元素 也就是每个生成block是由几个文件block生成的
        # n:block总数
        # selection: 在k个blocks中选择一些元素
        # deg: seed值: 使用seed初始化random 然后random.sample进行抽样
        selection_indexes, deg = generate_indexes(i, random_degrees[i % (blocks_n * 2)], blocks_n)

        # Xor each selected array within each other gives the drop (or just take one block if there is only one selected)
        drop = blocks[selection_indexes[0]]
        for n in range(1, deg):
            drop = np.bitwise_xor(drop, blocks[selection_indexes[n]])
            # drop = drop ^ blocks[selection_indexes[n]] # according to my tests, this has the same performance

        # Create symbol, then log the process
        symbol = Sym(index=i, degree=deg, data=drop, fileSize=0, blocksN=0)

        # log("Encoding", i, drops_quantity, start_time)

        yield symbol
    LOG.Basic("LT-ENCODE", "Correctly dropped {} symbols (packet size={})".format(drops_quantity, PACKET_SIZE))
