"""KKK"""
import json

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

def knapsack(amount, itemlist):
    """knapsack"""
    res = []
    weight = amount
    while True:
        most_value = 0
        most_val_item = None
        for item in itemlist:
            if item.get_cost() > most_value:
                most_value = item.get_cost()
                most_val_item = item
        if len(itemlist) == 0 or weight - most_val_item.get_weight() < 0:
            break
        res.append(most_val_item)
        weight -= most_val_item.get_weight()
        itemlist.remove(most_val_item)
    sum_price = 0
    print("Knapsack Size:", amount, "kg")
    print("===============================")
    for i in res:
        print(i.get_name(), "->", i.get_weight(), "kg ->", i.get_price(), "THB")
        sum_price += i.get_price()
    print("Total:", sum_price, "THB")

def main():
    """main"""
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)
main()
