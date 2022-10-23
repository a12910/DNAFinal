class DNAStr:
    # A C T G
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        self.data += other.data
        return self

    def __repr__(self):
        return self.data

    def slice(self, start, step):
        return DNAStr(self.data[start:start + step])

    def add(self, char):
        self.data += char
