import os
from pathlib import Path
from pprint import pprint


def calculate_head_pos(head_pos: tuple[int, int], direction) -> tuple[int, int]:
    match direction:
        case "R":
            return head_pos[0] + 1, head_pos[1]
        case "L":
            return head_pos[0] - 1, head_pos[1]
        case "U":
            return head_pos[0], head_pos[1] + 1
        case "D":
            return head_pos[0], head_pos[1] - 1


def calculate_tail_pos(
    head_pos: tuple[int, int], tail_pos: tuple[int, int]
) -> tuple[int, int]:
    x_diff = head_pos[0] - tail_pos[0]
    x_tail_pos = tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]
    y_tail_pos = tail_pos[1]

    if (x_diff != 0 and abs(y_diff) > 1) or (y_diff != 0 and abs(x_diff) > 1):
        # Diagonal
        x_tail_pos = tail_pos[0] + (x_diff // abs(x_diff))
        y_tail_pos = tail_pos[1] + (y_diff // abs(y_diff))
    elif abs(x_diff) > 1:
        # Horizontal
        x_tail_pos = tail_pos[0] + (x_diff // abs(x_diff))
    elif abs(y_diff) > 1:
        # Vertical
        y_tail_pos = tail_pos[1] + (y_diff // abs(y_diff))

    return x_tail_pos, y_tail_pos


def part1(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    positions_tail_visited: set[tuple[int, int]] = set()
    head_pos: tuple[int, int] = (0, 0)
    tail_pos: tuple[int, int] = (0, 0)
    with open(data_file) as f:
        for line in f.readlines():
            direction, steps = line.strip().split()
            for _ in range(int(steps)):
                positions_tail_visited.add(tail_pos)
                head_pos = calculate_head_pos(head_pos, direction)
                tail_pos = calculate_tail_pos(head_pos, tail_pos)

    positions_tail_visited.add(tail_pos)
    print(f"PART 1: {len(positions_tail_visited)}")


def part2(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    positions_tail_visited: set[tuple[int, int]] = set()
    positions = [(0, 0) for _ in range(10)]
    with open(data_file) as f:
        for line in f.readlines():
            direction, steps = line.strip().split()
            for _ in range(int(steps)):
                positions_tail_visited.add(positions[-1])
                positions[0] = calculate_head_pos(positions[0], direction)
                for i, pos in enumerate(positions[1:]):
                    positions[i + 1] = calculate_tail_pos(positions[i], pos)

    positions_tail_visited.add(positions[-1])
    print(f"PART 2: {len(positions_tail_visited)}")


if __name__ == "__main__":
    filename = "test.txt"
    part1(filename)
    part2(filename)
