import weakref

class Data:
    def __init__(self, value, owner):
        self.value = value
        self.owner = weakref.ref(owner)

    def __del__(self):
        print('data del')

    def __str__(self):
        print(self.owner())

class Node:
    def __init__(self, value):
        self.value = Data(value, self)

    def __del__(self):
        print('node del')

if __name__ == "__main__":
    node = Node(100)
    input("wait...")
