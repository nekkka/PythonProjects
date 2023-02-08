class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width


    def area(self):
        return self.lenght * self.width


s = Rectangle(10, 3)

print("Area of the rectangle:", s.area())

