#!/usr/bin/env python3
import random
from typing import Generator


def gen_event(players: list[str],
              actions: list[str]) -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[
        tuple[str, str], None, None]:
    while len(events) != 0:
        consume = random.choice(events)
        events.remove(consume)
        yield consume


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release", "use"]
    generator = gen_event(players, actions)
    events = []
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")
    for i in range(10):
        events.append(next(generator))
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
