#!/usr/bin/env python3

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)

    for i in range(1000):
    player, action = next(event_stream)
    print(f"Event {i}: Player {player} did action {action}")

     def consume_event(events: list[tuple[str, str]]) -> typing.Generator[...]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event

        