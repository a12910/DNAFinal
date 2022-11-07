
def map0():
    ATMap = {
        "A": ["TA", "TC", "TT", "TG"],
        "C": ["TA", "TC", "AT", "TG"],
        "T": ["AA", "AC", "AT", "AG"],
        "G": ["AT", "AC", "TA", "TG"]
    }
    CGMap = {
        "A": ["CA", "GC", "CT", "CG"],
        "C": ["GA", "GC", "GT", "GG"],
        "T": ["GA", "GC", "GT", "CG"],
        "G": ["CA", "CC", "CT", "CG"]
    }
    # grade 293
    # CG 0.445 0.473 0.475 0.478 0.504

def map1():
    ATMap = {
        "A": ["TA", "C", "TC", "G"],
        "C": ["A", "TC", "TG", "G"],
        "T": ["AT", "C", "AG", "G"],
        "G": ["A", "C", "TA", "TG"]
    }
    CGMap = {
        "A": ["CA", "CG", "T", "G"],
        "C": ["A", "GC", "T", "GA"],
        "T": ["A", "C", "GT", "GC"],
        "G": ["A", "CA", "T", "CG"]
    }
    # grade: 266
    # CG: 0.401 0.471 0.481 0.496 0.542

def map2():
    ATMap = {
        "A": ["A", "T", "C", "G"],
        "C": ["A", "TC", "TG", "G"],
        "T": ["A", "T", "C", "G"],
        "G": ["A", "C", "TA", "TG"]
    }
    CGMap = {
        "A": ["CA", "CG", "T", "G"],
        "C": ["A", "T", "C", "G"],
        "T": ["A", "C", "GT", "GC"],
        "G": ["A", "T", "C", "G"]
    }
    # grade 257
    # CG 0.446 0.484 0.495 0.510 0.555

def map3():
    ATMap = {
        "A": ["A", "T", "C", "G"],
        "C": ["A", "C", "T", "G"],
        "T": ["A", "T", "C", "G"],
        "G": ["A", "C", "TA", "TG"]
    }
    CGMap = {
        "A": ["A", "T", "C", "G"],
        "C": ["A", "T", "C", "G"],
        "T": ["A", "C", "GT", "GC"],
        "G": ["A", "T", "C", "G"]
    }
    # grade 247
    # CG 0.390 0.460 0.476 0.488 0.516

