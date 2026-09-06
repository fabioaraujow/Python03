#!/usr/bin/env python3
import random


def gen_player_achievements(achiv: list[str]) -> set[str]:
    achievements = set(random.sample(achiv,
                                     random.randint(4, (len(achiv)) - 3)))
    return achievements


if __name__ == "__main__":
    print("=== Game Achievement Tracker ===\n")
    achievements = ["Craft Genius", "Strategist",
                    "World Savior", "Speed Runner",
                    "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable",
                    "First Steps", "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"]
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    players = [("Alice", alice), ("Bob", bob),
               ("Charlie", charlie), ("Dylan", dylan)]
    for name, player_set in players:
        print(f"Player {name}: {player_set}")
    print(f"All distinct achievements: "
          f"{set.union(alice, bob, charlie, dylan)}\n")
    print(f"Common achievements: "
          f"{set.intersection(alice, bob, charlie, dylan)}\n")
    for player, player_set in players:
        other: set[str] = set()
        for other_player, other_set in players:
            if other_player != player:
                other = other.union(other_set)
        print(f"Only {player} has: {player_set.difference(other)}")
    print()
    all_achiev = set(achievements)
    for player, player_set in players:
        print(f"{player} is missing: {all_achiev.difference(player_set)}")
