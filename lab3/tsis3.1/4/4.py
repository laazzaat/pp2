import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, xplus, yplus):
        self.x += xplus
        self.y += yplus

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

x1 = int(input())
y1 = int(input())

point1 = Point(x1, y1)
point1.show()

point1.move(1, 1)
point1.show()

point2 = Point(10, 5)
distance = point1.dist(point2)
print(distance)