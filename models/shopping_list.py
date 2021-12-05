from models.items import *

item1 = Items("PS5", 500, 1, False)
item2 = Items("TV", 700, 1, False)
item3 = Items("Red Ribbon", 2, 2, False)
item4 = Items("iPhone", 1000, 1, True)

items=[item1, item2, item3, item4]

def add_new_item(item):
    items.append(item)

def total_amount(item):
    for item in items:
        total = 0
        total += item
    return total