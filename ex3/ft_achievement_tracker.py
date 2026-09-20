#!/usr/bin/env python3

 
import random
 
ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]
 
PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]
 
def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(4, len(achievements) - 5)
    picked = random.sample(achievements, count)
    return set(picked)
    
all_achievements: set[str] = set()
for achievements in player_sets:
    all_achievements = all_achievements.union(achievements)

    common = player_sets[0]
index = 1
while index < len(player_sets):
    common = common.intersection(player_sets[index])
    index += 1

   only_mine = player_sets[index].difference(others)
    missing = set(ACHIEVEMENTS).difference(player_sets[index])



   #!/usr/bin/env python3

def main() -> None:
    """Main function demonstrating achievement tracking with sets"""
    print("=== Achievement Tracker System ===")

    alice: set[str] = set()
    alice.add("first_kill")
    alice.add("level_10")
    alice.add("treasure_hunter")
    alice.add("speed_demon")
    print(f"Player alice achievements: {alice}")

    bob: set[str] = set()
    bob.add("first_kill")
    bob.add("level_10")
    bob.add("boss_slayer")
    bob.add("collector")
    print(f"Player bob achievements: {bob}")

    charlie: set[str] = set()
    charlie.add("level_10")
    charlie.add("treasure_hunter")
    charlie.add("boss_slayer")
    charlie.add("speed_demon")
    charlie.add("perfectionist")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    achievements: set[str] = alice.union(bob, charlie)
    common: set[str] = alice.intersection(bob, charlie)

    # Find rare achievements (owned by only 1 player) - using only methods
    alice_only: set[str] = alice.difference(bob, charlie)
    bob_only: set[str] = bob.difference(alice, charlie)
    charlie_only: set[str] = charlie.difference(alice, bob)
    rarest: set[str] = alice_only.union(bob_only, charlie_only)

    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}")

    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rarest}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main() 
