from concurrent.futures import ThreadPoolExecutor
import time

excutor = ThreadPoolExecutor(3)


def f(a, b):
    time.sleep(5)
    return a ** b


result = excutor.submit(f, 2, 3)
print(result.result())

for x in excutor.map(f, [2, 4, 6], [3, 5, 7]):
    print(x)

for x in excutor.map(f, [2, 4, 6, 8, 10], [3, 5, 7, 9, 11]):
    print(x)
