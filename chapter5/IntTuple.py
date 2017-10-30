class IntTuple(tuple):

    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(IntTuple, self).__init__()


if __name__ == "__main__":
    int_tuple = IntTuple([-1, 1, 3, [3, 4, 5], 8])
    print(int_tuple)