from random import randint, sample
from functools import reduce

data1 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}
data2 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}
data3 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}
print(data1.keys() & data2.keys() & data3.keys())
print(reduce(lambda a, b: a & b, map(dict.keys, [data1, data2, data3])))
