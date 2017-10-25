a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

for index in range(len(a)):
    print(a[index])
    print(b[index])

print(zip(a, b))
for x in zip(a, b):
    print(x)
for x, y in zip(a, b):
    print(x)
    print(y)

from itertools import chain

for x in chain(a, b):
    print(x)

