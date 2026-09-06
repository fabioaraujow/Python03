#!/usr/bin/env python3
import sys


def ft_validade_data(data: list[str]) -> list[int]:
    scores = []
    for to_verify in data:
        try:
            scores.append(int(to_verify))
        except ValueError:
            print(f"Invalid parameter: '{to_verify}'")
    return scores


if __name__ == "__main__":

    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        scores = ft_validade_data(sys.argv[1:])
        players = len(scores)
        if players > 0:
            print(f"Scores processed: {scores}")
            print(f"Total players: {players}")
            sum_scores = sum(scores)
            print(f"Total score: {sum_scores}")
            print(f"Average score: {(sum_scores / players):.1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print("No scores provided. "
                  "Usage: python3 ft_score_analytics.py <score1> <score2> ...")

    else:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
