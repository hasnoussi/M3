#!/usr/bin/env python3

#!/usr/bin/env python3
"""Exercise 6: Data Alchemist.

Use list and dictionary comprehensions to transform and filter
game player data efficiently.
"""

import random


def main() -> None:
    """Entry point of the program."""
    print("=== Game Data Alchemist ===")
    print()

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    already_capitalized = [
        name for name in players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {already_capitalized}")
    print()

    scores = {
        name: random.randint(1, 999) for name in all_capitalized
    }
    print(f"Score dict: {scores}")

    total = sum(scores[name] for name in scores)
    average = total / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: scores[name] for name in scores if scores[name] > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()