from queue import Queue
from threading import Thread, Event
from time import sleep


class Producer(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.queue = queue
        self.sid = sid

    def run(self):
        self.work()
        self.queue.put((self.sid, 'Producer' + str(self.sid)))

    def work(self):
        sleep(2)
        # print("Producer work" + str(self.sid))


class Consumer(Thread):
    def __init__(self, queue, s_event, r_event):
        Thread.__init__(self)
        self.queue = queue
        self.s_event = s_event
        self.r_event = r_event

    def run(self):
        count = 0
        while True:
            sid, data = self.queue.get()
            if sid == -1:
                self.r_event.set()
                self.s_event.wait()
                break
            if data:
                count += 1
                print("Consumer received " + str(data))
                if count == 3:
                    self.r_event.set()
                    print('r_event.set')
                    self.s_event.wait()
                    self.s_event.clear()
                    count = 0


class Service(Thread):
    def __init__(self, s_event, r_event):
        Thread.__init__(self)
        self.s_event = s_event
        self.r_event = r_event
        self.setDaemon(True)

    def work(self):
        sleep(2)
        print("Service work")

    def run(self):
        while True:
            self.r_event.wait()
            self.work()
            self.r_event.clear()
            self.s_event.set()


if __name__ == "__main__":
    q = Queue()
    p_threads = [Producer(i, q) for i in range(1, 11)]
    s_event = Event()
    r_event = Event()
    c_thread = Consumer(q, s_event, r_event)
    service_thread = Service(s_event, r_event)
    service_thread.start()
    for t in p_threads:
        t.start()
    c_thread.start()
    for t in p_threads:
        t.join()
    q.put((-1, None))
