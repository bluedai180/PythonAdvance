# 1. 过滤掉列表[9, 9, 7, 2, -10, -4, -7, -8, 3, 7]中的负数
# 2. 筛出字典中高于90的项
# 3. 筛出集合中能被3整除的元素

from random import randint

data_list = [randint(-10, 10) for x in range(10)]
print(data_list)
print(list(filter(lambda x: x >= 0, data_list)))
print([x for x in data_list if x >= 0])

print("=============================================")
data_dict = {x: randint(60, 100) for x in range(10)}
test = {10: 3}
print(data_dict)
print({k: v for k, v in data_dict.items() if v >= 90})

print("=============================================")
data_set = {randint(0, 10) for x in range(10)}
print(data_set)
print({x for x in data_set if x % 3 == 0})
