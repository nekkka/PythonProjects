import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f'Coordinates {self.x}, {self.y}')
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(1, 2)
p2 = Point(4, 6)


p1.show()
p2.show()


p1.move(3, 4)
p2.move(-3, -4)


print("Point 1 after moving:")
p1.show()
print("Point 2 after moving:")
p2.show()


print("Distance between the points:", p1.dist(p2))
