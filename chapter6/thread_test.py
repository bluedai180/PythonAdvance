from threading import Thread


def test(x):
    print(x)


t = Thread(target=test, args=("dai",))
t.start()


class Test(Thread):
    def __init__(self, value):
        Thread.__init__(self)
        self.value = value

    def run(self):
        test(self.value)


t = Test("blue")
t.start()

thread = []
for i in range(1, 11):
    t = Test(i)
    thread.append(t)
    t.start()
for t in thread:
    t.join()

print("main thread")
