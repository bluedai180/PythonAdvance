from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

if __name__ == "__main__":
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(4, 5)
    print(rect1 > rect2)
    print(rect1 != rect2)