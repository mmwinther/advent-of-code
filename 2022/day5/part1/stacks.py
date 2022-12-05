import os
from pathlib import Path
import re
from typing import List


def add_stack_if_needed(stacks: List[List[str]], i: int) -> List[List[str]]:
    try:
        stacks[i]
    except IndexError:
        stacks.insert(i, [])
    return stacks


def get_crate(line: str, chunk_length: int, i: int) -> str:
    increment = chunk_length * i
    return line[0 + increment : chunk_length + increment]


def stack_crate(stacks: List[List[str]], crate: str, i: int):
    WHITESPACE = "^\s+$"
    CRATE_SYMBOL = "\[([A-Z])\]"
    if not re.match(WHITESPACE, crate):
        crate_symbol = re.search(CRATE_SYMBOL, crate).group(1)
        stacks[i].append(crate_symbol)
    return stacks


def get_starting_stacks(stacks_input: str) -> List[List[str]]:
    stacks_input = stacks_input.split("\n")
    stacks: List[List[str]] = []
    for line in reversed(stacks_input):
        if "[" not in line:
            continue
        else:
            # Work on chunks of characters
            CHUNK_LENGTH = 4
            for i in range(len(line) // CHUNK_LENGTH + 1):
                stacks = add_stack_if_needed(stacks, i)
                crate = get_crate(line, CHUNK_LENGTH, i)
                stacks = stack_crate(stacks, crate, i)

    return stacks


def make_move(move: str, stacks: List[List[str]]) -> List[List[str]]:
    details = move.split()
    number_of_crates = int(details[1])
    starting_stack = int(details[3])
    finishing_stack = int(details[5])

    for _ in range(number_of_crates):
        stacks[finishing_stack - 1].append(stacks[starting_stack - 1].pop())

    return stacks


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    with open(data_file) as f:
        data = f.read()
        stacks_input, moves_input = tuple(data.split("\n\n")[:2])

    stacks = get_starting_stacks(stacks_input)

    for move in moves_input.split("\n"):
        if not move:
            continue
        stacks = make_move(move, stacks)

    result = "".join([stack[-1] for stack in stacks])

    print(f"{result = }")


if __name__ == "__main__":
    main("test.txt")
