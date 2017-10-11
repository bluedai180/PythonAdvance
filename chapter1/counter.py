from collections import Counter
from random import randint

data = [randint(0, 20) for _ in range(1, 15)]

print(Counter(data).items())
print(Counter(data).most_common(3))
print(isinstance(Counter(data), dict))

import re
zen = """
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!"""
data_zen = re.split("\W+", zen)
print(Counter(data_zen).most_common(10))