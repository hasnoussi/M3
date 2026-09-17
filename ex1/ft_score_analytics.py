#!/usr/bin/env python3
"""Exercise 1: Score Cruncher.

Read game scores from the command line, filter out invalid values,
store the valid ones in a list, and compute basic statistics.
"""

import sys

USAGE = "No scores provided. Usage: python3 ft_score_analytics.py " \
    "<score1> <score2> ..."


def main() -> None:
    """Entry point of the program."""
    print("=== Player Score Analytics ===")

    scores: list[int] = []
    for raw_value in sys.argv[1:]:
        try:
            scores.append(int(raw_value))
        except ValueError:
            print(f"Invalid parameter: '{raw_value}'")

    if len(scores) == 0:
        print(USAGE)
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
