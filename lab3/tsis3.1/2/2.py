class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)
    
dlina=int(input())
shirina = int(input())
s = Rectangle(dlina, shirina)

s.area()