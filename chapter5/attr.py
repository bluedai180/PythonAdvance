class Attr:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError("wrong type!")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class User:
    name = Attr("name", str)
    age = Attr("age", int)


if __name__ == "__main__":
    user = User()
    user.name = 'blue'
    print(user.name)
    user.age = '11'

