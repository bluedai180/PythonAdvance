class User:
    def __init__(self):
        self.id = None

    def set_id(self, id):
        if isinstance(id, int):
            self.id = id
        else:
            raise Exception('Wrong type')

    def get_id(self):
        return self.id

    ID = property(get_id, set_id)


if __name__ == "__main__":
    user = User()
    user.id = 1
    print(user.id)
    # user.set_id('123')
    user.set_id(1)
    print(user.ID)
    user.ID = 2
    print(user.ID)
