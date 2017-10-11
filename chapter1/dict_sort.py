from random import randint

data = {x: randint(60, 100) for x in "abcdefg"}
print(sorted(data))
print(sorted(zip(data.values(), data.keys())))
print(sorted(data.items(), key=lambda x: x[1]))
