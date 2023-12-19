import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w= w
        self.h = h

    def area(self):
        return self.w* self.h

c = Circle(3)
r = Rectangle(4,6)

print(f"Area Circle: {c.area():.2f}")
print("Area Rectangle:",r.area())




