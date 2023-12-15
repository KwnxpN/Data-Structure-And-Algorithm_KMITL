class Rectangle:
    def __init__(self, height, weight):
        self.soong = height
        self.nakk = weight
    def get_soong(self):
        print(self.soong)
    def cal(self):
        return self.soong + self.nakk

def main():
    rec01 = Rectangle(10, 20)
    rec01.get_soong()
    print(rec01.cal())
main()
