import os
import json


# this is the actual item that will show up in a players inventory
class Item:
    def __init__(self, id=None, name=None, value=None, weight=None, stack_size=None, consumable=None, nutrition=None):
        self.id = id
        self.name = name
        self.value = value
        self.weight = weight
        self.stack_size = stack_size
        self.consumable = consumable
        self.nutrition = nutrition

def populate_items_dict(paths):
    items = {}
    for path in paths:
        with open(path) as f:
            data = json.load(f)
            for item in data:
                items[item["id"]] = Item(**item)
    return items

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

def transfer_item(item, source_inventory, target_inventory):
    source_inventory.remove_item(item)
    target_inventory.add_item(item)

if __name__ == "__main__":
    inv1 = Inventory()
    inv2 = Inventory()

    inv1.add_item(Item(id=1, name="Sword", value=100, weight=5, stack_size=1, consumable=False, nutrition=0))
    inv1.add_item(Item(id=1, name="Sword", value=100, weight=5, stack_size=1, consumable=False, nutrition=0))
    inv1.add_item(Item(id=1, name="Sword", value=100, weight=5, stack_size=1, consumable=False, nutrition=0))

    for item in inv1.items:
        print(item.name)

    transfer_item(inv1.items[0], inv1, inv2)

    for item in inv2.items:
        print(item.name)
