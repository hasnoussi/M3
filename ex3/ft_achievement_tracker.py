#!/usr/bin/env python3
"""Exercise 3: Achievement Hunter.

Use sets to track unique achievements across several players, and
combine them with union, intersection, and difference.
"""

import random

ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]

PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements(achievements: list[str]) -> set[str]:
    """Randomly build a set of achievements for one player.

    Args:
        achievements: The full pool of possible achievements.

    Returns:
        A set containing a random subset of achievements.
    """
    count = random.randint(4, len(achievements) - 5)
    picked = random.sample(achievements, count)
    return set(picked)


def main() -> None:
    """Entry point of the program."""
    print("=== Achievement Tracker System ===")
    print()

    player_sets: list[set[str]] = []
    for player in PLAYERS:
        achievements = gen_player_achievements(ACHIEVEMENTS)
        player_sets.append(achievements)
        print(f"Player {player}: {achievements}")
    print()

    all_achievements: set[str] = set()
    for achievements in player_sets:
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")
    print()

    common = player_sets[0]
    index = 1
    while index < len(player_sets):
        common = common.intersection(player_sets[index])
        index += 1
    print(f"Common achievements: {common}")
    print()

    index = 0
    for player in PLAYERS:
        others: set[str] = set()
        other_index = 0
        for achievements in player_sets:
            if other_index != index:
                others = others.union(achievements)
            other_index += 1
        only_mine = player_sets[index].difference(others)
        print(f"Only {player} has: {only_mine}")
        index += 1
    print()

    index = 0
    for player in PLAYERS:
        missing = set(ACHIEVEMENTS).difference(player_sets[index])
        print(f"{player} is missing: {missing}")
        index += 1


if __name__ == "__main__":
    main()
