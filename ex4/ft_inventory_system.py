#!/usr/bin/env python3

def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for argument in arguments:
        parts = argument.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name, quantity_str = parts[0], parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity
    return inventory
    