# def f(a, b=10):
#     ''' f test method
#
#     :param a:
#     :param b:
#     :return:
#     '''
#     d = 10
#     print("f")
#
# print(f.__doc__)
# print(f.__defaults__)
# print(f.__name__)
# print(f.__module__)

# def t():
#     a = 2
#     return lambda k: a ** k
#
# g = t()
# print(g.__closure__[0].cell_contents)

from functools import wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, update_wrapper

def my_decortor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper func """
        print("in wrapper")
        # update_wrapper(wrapper, func)
        func(*args, **kwargs)
    return wrapper

@my_decortor
def example():
    '''example func'''
    print("example func")

print(example.__doc__)
print(example.__name__)
# print(WRAPPER_UPDATES)
# print(WRAPPER_ASSIGNMENTS)
