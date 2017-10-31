from threading import Thread
from time import sleep
from queue import Queue


class Producer(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.queue = queue
        self.sid = sid

    def run(self):
        self.work()
        self.queue.put((self.sid, 'Producer'+str(self.sid)))

    def work(self):
        sleep(2)
        print("Producer work" + str(self.sid))


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            sid, data = self.queue.get()
            if sid == -1:
                break
            if data:
                print("Consumer received " + str(data))


if __name__ == "__main__":
    q = Queue()
    p_threads = [Producer(i, q) for i in range(1, 11)]
    c_thread = Consumer(q)
    for t in p_threads:
        t.start()
    c_thread.start()
    for t in p_threads:
        t.join()
    q.put((-1, None))
