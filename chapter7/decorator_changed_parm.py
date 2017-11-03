from functools import wraps
import time
import logging
from random import randint


def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s ' % (func.__name__, used, timeout)
                logging.warning(msg)
            return res

        def set_timeout(k):
            nonlocal timeout
            timeout = k
        wrapper.set_timeout = set_timeout
        return wrapper

    return decorator


@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)


# for x in range(1, 31):
#     test()

test.set_timeout(1)

for x in range(1, 31):
    test()
