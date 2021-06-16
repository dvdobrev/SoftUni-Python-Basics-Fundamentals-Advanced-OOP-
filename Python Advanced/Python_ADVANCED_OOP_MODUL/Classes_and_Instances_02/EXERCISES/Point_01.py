import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        distance = math.hypot(x - self.x, y - self.y)
        return distance


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))