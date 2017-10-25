class FroatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        a = self.start
        while a <= self.end:
            yield a
            a += self.step

    def __reversed__(self):
        a = self.end
        while a >= self.start:
            yield a
            a -= self.step

if __name__ == "__main__":
    froat = FroatRange(0, 3, 0.5)
    for x in iter(froat):
        print(x)
    for y in reversed(froat):
        print(y)