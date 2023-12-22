"""KKK"""

class Rectangle:
    """rectangle class"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        """find the area of rectangle"""
        return self.height * self.width
    def perimeter(self):
        """find the perimeter of rectangle"""
        return (self.height + self.width) * 2

def main(height, width, condi):
    """main"""
    rectangle = Rectangle(height, width)
    if condi == "area":
        print("%.2f"%rectangle.area())
    elif condi == "perimeter":
        print("%.2f"%rectangle.perimeter())
main(float(input()), float(input()), str(input()))
