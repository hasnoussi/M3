#!/usr/bin/env python3
"""Exercise 5: Stream Wizard.

Use Python generators to produce a stream of game events on demand,
without storing everything in memory.
"""

import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "walk", "jump", "eat", "sleep", "swim", "climb",
    "grab", "release", "move", "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Endlessly yield random (player, action) game events."""
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    """Yield and remove random events from a list until it is empty.

    Args:
        events: The list of events to consume. It is mutated in
            place as events are picked and removed.
    """
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event


def main() -> None:
    """Entry point of the program."""
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_stream))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
