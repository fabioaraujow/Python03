#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    arg_parsing = sys.argv[1:]
    inventory = {}
    items = []
    bigger = 0
    b_name = ""
    for current in arg_parsing:
        try:
            key, quantity = current.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{current}'")
            continue
        try:
            value = int(quantity)
        except ValueError as err:
            print(f"Quantity error for '{key}': {err}")
            continue
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        if bigger < value:
            bigger = value
            b_name = key
        inventory[key] = value
        items.append(key)
    sum_quantity = sum(inventory.values())
    sum_items = len(inventory)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {sum_items} items: {sum_quantity}")
    for current in inventory:
        print(f"Item {current} represents "
              f"{(inventory[current]/sum_quantity) * 100:.1f}%")
    print(f"Item most abundant: {b_name} with quantity {bigger}")
    least = bigger
    l_name = b_name
    for current in inventory:
        if least > inventory[current]:
            least = inventory[current]
            l_name = current
    print(f"Item least abundant: {l_name} with quantity {least}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
