#!/usr/bin/env python3
import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    players = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")
    capitalized = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized}")
    only_cap = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")
    score_dict = {player: random.randint(1, 1000) for player in capitalized}
    print(f"Score dict: {score_dict}")
    average = sum([score_dict[player]
                   for player in score_dict]) / len(score_dict)
    print(f"Score average is {average:.2f}")
    high_scores = {player: score_dict[player]
                   for player in score_dict if score_dict[player] > average}
    print(f"High scores: {high_scores}")
