#!/usr/bin/env python3

def get_player_pos() -> tuple[float, float, float]:
    while True:
        prompt = "Enter new coordinates as floats in format 'x,y,z': "
        raw = input(prompt)
        parts = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        values: list[float] = []
        conversion_failed = False
        for part in parts:
            cleaned = part.strip()
            try:
                values.append(float(cleaned))
            except ValueError as error:
                print(f"Error on parameter '{cleaned}': {error}")
                conversion_failed = True
                break

        if conversion_failed:
            continue

        return (values[0], values[1], values[2])