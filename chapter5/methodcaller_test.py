from operator import methodcaller

s = "adb123qwer456"

print(s.find('q', 3))
print(methodcaller('find', 'q', 3)(s))