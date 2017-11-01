from threading import Thread, local

l = local()
l.x = 1


def f():
    return print(l.x)


f()
t = Thread(target=f)
t.start()
