#!/usr/bin/env python3
"""Exercise 2: Position Tracker.

Track a player's 3D position using tuples, and compute distances
with the Euclidean distance formula.
"""

import math


def get_player_pos() -> tuple[float, float, float]:
    """Ask the user for 3D coordinates until valid ones are given.

    Returns:
        A tuple (x, y, z) with the player's coordinates as floats.
    """
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


def main() -> None:
    """Entry point of the program."""
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, "
        f"Y={first_pos[1]}, Z={first_pos[2]}"
    )

    distance_to_center = round(
        math.sqrt(
            first_pos[0] ** 2 + first_pos[1] ** 2 + first_pos[2] ** 2
        ),
        4,
    )
    print(f"Distance to center: {distance_to_center}")
    print()

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_between = round(
        math.sqrt(
            (second_pos[0] - first_pos[0]) ** 2
            + (second_pos[1] - first_pos[1]) ** 2
            + (second_pos[2] - first_pos[2]) ** 2
        ),
        4,
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between}")


if __name__ == "__main__":
    main()
