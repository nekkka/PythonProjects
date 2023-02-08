class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght * self.lenght


s = Square(int(input()))

print("Area of the square:", s.area())

