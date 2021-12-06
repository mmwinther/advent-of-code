import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        bingo_lines = f.read().splitlines()

    drawn_numbers = [int(i) for i in bingo_lines.pop(0).split(",")]
    print(drawn_numbers)
    boards = []
    board = []

    for line in bingo_lines:
        if not line.strip():
            continue
        else:
            board.append([int(i.strip()) for i in line.split()])
        if len(board) == 5:
            print(board)
            boards.append(board)
            board = []

    print(boards)


if __name__ == "__main__":
    main()
