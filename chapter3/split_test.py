import re

s = 'ab;cd|efg|hi,jklmn\topq;rst;uvw\txyz'

print(re.split('[,;|\t]+', s))