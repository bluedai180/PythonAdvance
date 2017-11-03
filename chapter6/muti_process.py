from multiprocessing import Process, Pipe, Queue

q = Queue()
p1, p2 = Pipe()

def f_pipe(p):
    p.send(p.recv() * 2)


def f_queue(q):
    print('start')
    print(q.get())
    print('end')


if __name__ == "__main__":
    # Process(target=f, args=(q,)).start()
    # q.put(2)
    Process(target=f_pipe, args=(p2,)).start()
    p1.send(55)
    print(p1.recv())
