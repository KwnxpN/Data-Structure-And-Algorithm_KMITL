"""KKK"""

class LaewTaeApp:
    """แล้วแต่งับ ไอฉงน"""
    def __init__(self):
        """Attribute"""
        self.foods_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.random_times = 0
    def random_foods(self):
        """random the food from list"""
        self.random_times += 1
    def list_foods(self):
        """list of foods"""
        self.foods_list = sorted(self.foods_list)
        print(self.foods_list)
    
def main():
    """main"""
    laewtae = LaewTaeApp()
    laewtae.list_foods()
main()
