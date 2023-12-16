"""KKK"""

class Point:
    """class Point"""
    def __init__(self, point_x, point_y):
        """get x and y"""
        self.set_cordinate(point_x, point_y)

    def set_cordinate(self, point_x, point_y):
        """set x and y point"""
        self.point_x = point_x
        self.point_y = point_y

    def calculate(self, other):
        """calculate distance"""
        return ((other.point_x - self.point_x)**2 + (other.point_y - self.point_y)**2) ** 0.5

def get_the_distance(boss_x, boss_y, art_x, art_y):
    """get the distance between boss and art"""
    boss_point = Point(boss_x, boss_y)
    art_point = Point(art_x, art_y)
    distance = boss_point.calculate(art_point)
    print("%.2f"%distance)
get_the_distance(float(input()), float(input()), float(input()), float(input()))
