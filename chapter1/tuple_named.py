from collections import namedtuple

student = namedtuple('student', ['name', 'age', 'sex', 'addr'])

s = student('Dai', '22', 'male', 'beijing')
print(s)
print(s.name)
print(isinstance(s, tuple))