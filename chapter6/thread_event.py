from queue import Queue
from threading import Thread, Event
from time import sleep


class Producer(Thread):
    def __init__(self, sid, queue, s_event, r_event):
        Thread.__init__(self)
        self.queue = queue
        self.sid = sid
        self.s_event = s_event
        self.r_event = r_event

    def run(self):
        self.work()
        self.queue.put((self.sid, 'Producer' + str(self.sid)))

    def work(self):
        sleep(2)
        print("Producer work" + str(self.sid))


class Consumer(Thread):
    def __init__(self, queue, s_event, r_event):
        Thread.__init__(self)
        self.queue = queue
        self.s_event = s_event
        self.r_event = r_event

    def run(self):
        while True:
            sid, data = self.queue.get()
            if sid == -1:
                break
            if data:
                print("Consumer received " + str(data))


class Service(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            pass


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
