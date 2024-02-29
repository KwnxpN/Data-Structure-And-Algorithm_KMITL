"""KKK"""

class Item:
    """Items"""
    def __init__(self, name, price, weight):
        """att con"""
        self.name = name
        self.price = price
        self.weight = weight
    def get_name(self):
        """getter name"""
        return self.name
    def get_price(self):
        """getter price"""
        return self.price
    def get_weight(self):
        """getter weight"""
        return self.weight
    def get_cost(self):
        """calculate cost"""
        return self.price / self.weight

def main():
    """main"""
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')
main()
