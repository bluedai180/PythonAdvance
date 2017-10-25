from itertools import islice

a = range(0, 10)
t = iter(a)
for x in islice(t, 0, 5):
    print(x)
print("========================")
for y in t:
    print(y)


