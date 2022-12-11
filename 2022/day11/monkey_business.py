from collections import defaultdict, deque
import math
import os
from pathlib import Path
from pprint import pprint
from typing import Any, Callable, Deque
from parse import parse


class Monkey:
    def __init__(self, description: str) -> None:
        self.index: int = 0
        self.items: Deque
        self.operation: Callable
        self.test: Callable
        self.true_result: int
        self.false_result: int
        self.parsing: list[dict[str, Any]] = [
            {
                "attribute": "index",
                "pattern": "Monkey {}:",
                "parser": lambda x: int(x[0]),
            },
            {
                "attribute": "items",
                "pattern": "Starting items: {}",
                "parser": lambda x: deque([int(i) for i in x[0].split(", ")]),
            },
            {
                "attribute": "operation",
                "pattern": "Operation: new = old {} {}",
                "parser": lambda x: self.parse_operation(x),
            },
            {
                "attribute": "test",
                "pattern": "Test: divisible by {}",
                "parser": lambda x: int(x[0]),
            },
            {
                "attribute": "true_result",
                "pattern": "If true: throw to monkey {}",
                "parser": lambda x: int(x[0]),
            },
            {
                "attribute": "false_result",
                "pattern": "If false: throw to monkey {}",
                "parser": lambda x: int(x[0]),
            },
        ]
        self.parse_description(description)

    def parse_description(self, description):
        for line in description.split("\n"):
            for p in self.parsing:
                if result := parse(p["pattern"], line.strip()):
                    self.__setattr__(p["attribute"], p["parser"](result.fixed))
                    break

    def parse_operation(self, result):
        if result[0] == "*":
            if result[1] == "old":
                return lambda i: i * i
            else:
                return lambda i: i * int(result[1])

        if result[0] == "+":
            if result[1] == "old":
                return lambda i: i + i
            else:
                return lambda i: i + int(result[1])


def play_turn(i: int, monkeys: list[Monkey], manage_worry: bool) -> list[Monkey]:
    # LCM idea and code shamelessly "borrowed" from https://github.com/DanielElisenberg/aoc2022/blob/c211cafabfa009ae75b8f39ba7634c8d347f5d58/python/day11/day11.py#L23
    l_c_m = math.lcm(*[m.test for m in monkeys])
    m = monkeys[i]
    for _ in range(len(m.items)):
        item = m.operation(m.items.popleft())
        if manage_worry:
            item = item // 3
        else:
            item = item % l_c_m
        to_move = m.true_result if item % m.test == 0 else m.false_result
        monkeys[to_move].items.append(item)

    return monkeys


def main(file_name, part):
    data_file = Path(os.path.dirname(__file__)) / file_name
    monkeys: list[Monkey] = []
    with open(data_file) as f:
        for description in f.read().split("\n\n"):
            monkeys.append(Monkey(description))

    inspections: dict[int:int] = defaultdict(int)
    for round in range(part["rounds"]):
        print(f"{round = }")
        for i in range(len(monkeys)):
            inspections[monkeys[i].index] += len(monkeys[i].items)
            monkeys = play_turn(i, monkeys, part["manage_worry"])

    print("PART 1")
    sorted_inspections = sorted(inspections.values())
    pprint(sorted_inspections[-1] * sorted_inspections[-2])


if __name__ == "__main__":
    filename = "test.txt"
    part1 = {"manage_worry": True, "rounds": 20}
    part2 = {"manage_worry": False, "rounds": 10_000}
    main(filename, part2)
