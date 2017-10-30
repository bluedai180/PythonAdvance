import sys
class User1:
    def __init__(self, id, name, addr, sex):
        self.id = id
        self.name = name
        self.addr = addr
        self.sex = sex


class User2:
    __slots__ = ['id', 'name', 'addr', 'sex']

    def __init__(self, id, name, addr, sex):
        self.id = id
        self.name = name
        self.addr = addr
        self.sex = sex

if __name__ == "__main__":
    user1 = User1(1, 'dai', "bj", 'male')
    user2 = User2(2, 'blue', 'sy', 'male')
    print(set(dir(user1)) - set(dir(user2)))
    print(user1.__dict__)
    print(sys.getsizeof(user1.__dict__))
    print(sys.getsizeof(user2))
