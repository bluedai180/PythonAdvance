from inspect import signature


def type_assert(*ty_args, **ty_kargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kwargs):
            for name, obj in sig.bind(*args, **kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_assert(int, str, list)
def f(a, b, c):
    print(a, b, c)

f(1, 1, 1)

def test(a, b, c=1): pass


sig = signature(test)
print(sig.parameters)
print(sig.parameters['a'].name)
print(sig.parameters['a'].kind)
print(sig.parameters['c'].default)
bargs = sig.bind(str, int, int)
print(bargs.arguments['a'])
