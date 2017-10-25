class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_prime(k):
                yield k

if __name__ == "__main__":
    prime = PrimeNumbers(0, 10)
    for x in prime:
        print(x)