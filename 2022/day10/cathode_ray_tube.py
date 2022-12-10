from enum import Enum, auto
import os
from pathlib import Path
from pprint import pprint
from typing import Final, Optional
from copy import deepcopy

UNLIT_PIXEL = "."
LIT_PIXEL = "#"
OBSERVATION_CYCLES: Final[set[int]] = {20, 60, 100, 140, 180, 220}
ROW_LENGTH = 40
NUM_ROWS = 6
ROW = [UNLIT_PIXEL for _ in range(ROW_LENGTH)]
GRID = [deepcopy(ROW) for _ in range(NUM_ROWS)]
SPRITE = [-1, 0, 1]


class Command(Enum):
    ADDX = auto()
    NOOP = auto()
    UNKNOWN = auto()


def read_instruction(line: str) -> tuple[Command, Optional[int]]:
    split_line = line.strip().split()
    if len(split_line) == 2:
        command, value = split_line
    elif len(split_line) == 1:
        command = split_line[0]
    else:
        return Command.UNKNOWN, None
    match command:
        case "addx":
            return Command.ADDX, int(value)
        case "noop":
            return Command.NOOP, None
        case _:
            return Command.UNKNOWN, None


def calculate_row_idx(c: int) -> int:
    return c - ((c // ROW_LENGTH) * ROW_LENGTH)


def get_px(c: int, x: int) -> str:
    sprite_window = [x + offset for offset in SPRITE]

    if calculate_row_idx(c) in sprite_window:
        return LIT_PIXEL
    else:
        return UNLIT_PIXEL


def part1(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    with open(data_file) as f:
        signal_sum = 0
        c = 1
        x = 1
        val = None
        command_running = False
        while c <= max(OBSERVATION_CYCLES):
            if command_running and c - start_cycle == 2:
                x += val
                command_running = False

            if c in OBSERVATION_CYCLES:
                signal_sum += x * c

            if not command_running:
                cmd, val = read_instruction(f.readline())
                if cmd is Command.UNKNOWN:
                    break
                elif cmd is Command.ADDX:
                    command_running = True
                    start_cycle = c

            c += 1

    print("PART 1")
    print(f"Signal sum = {signal_sum}")


def part2(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    with open(data_file) as f:
        c = 0
        x = 1
        val = None
        command_running = False
        while c < NUM_ROWS * ROW_LENGTH:

            GRID[c // ROW_LENGTH][calculate_row_idx(c)] = get_px(c, x)

            if not command_running:
                cmd, val = read_instruction(f.readline())
                if cmd is Command.UNKNOWN:
                    break
                elif cmd is Command.ADDX:
                    command_running = True
                    start_cycle = c

            c += 1

            if command_running and (c - start_cycle == 2):
                x += val
                command_running = False

    print("Part 2")
    for row in GRID:
        print("".join(row))


if __name__ == "__main__":
    filename = "test.txt"
    part1(filename)
    part2(filename)
