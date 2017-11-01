from multiprocessing import Process, Pipe, Queue

q = Queue()
p1, p2 = Pipe()

p1.send('abc')
print(p2.recv())

p2.send('def')
print(p1.recv())

# def f(q):
#     print('start')
#     print(q.get())
#     print('end')
#
#
# if __name__ == "__main__":
#     Process(target=f, args=(q,)).start()
#     q.put(2)
