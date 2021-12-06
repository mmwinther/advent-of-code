import argparse
from typing import Dict, Tuple, List
import numpy as np
from typing import TypedDict

Number = TypedDict("Number", {"number": int, "drawn": bool})


def parse_bingo_boards(bingo_lines: List[str]) -> List[List[List[Number]]]:
    boards = []
    board = []

    for line in bingo_lines:
        if not line.strip():
            continue
        else:
            board.append(
                [{"number": int(i.strip()), "drawn": False} for i in line.split()]
            )
        if len(board) == 5:
            boards.append(board)
            board = []

    return boards


def has_board_won(board: List[List[Number]]) -> bool:
    column_one = []
    column_two = []
    column_three = []
    column_four = []
    column_five = []
    for row in board:
        if all((x["drawn"] for x in row)):
            return True
        column_one.append(row[0]["drawn"])
        column_two.append(row[1]["drawn"])
        column_three.append(row[2]["drawn"])
        column_four.append(row[3]["drawn"])
        column_five.append(row[4]["drawn"])

    return any(
        [
            all(column)
            for column in [
                column_one,
                column_two,
                column_three,
                column_four,
                column_five,
            ]
        ]
    )


def mark_boards_with_drawn_number(
    boards: List[List[List[Number]]], drawn_number: int
) -> None:
    for board in boards:
        for row in board:
            for number in row:
                if number["number"] == drawn_number:
                    number["drawn"] = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        bingo_lines = f.read().splitlines()

    drawn_numbers = [int(i) for i in bingo_lines.pop(0).split(",")]
    print(drawn_numbers)
    boards = parse_bingo_boards(bingo_lines)
    won = False
    winning_board = None
    draw = None

    while won == False and drawn_numbers:
        draw = drawn_numbers.pop(0)
        print(f"Drawing: {draw}")
        mark_boards_with_drawn_number(boards, draw)
        for i, board in enumerate(boards):
            if has_board_won(board):
                print(f"Board {i + 1} won!")
                print(board)
                winning_board = board
                won = True
                break

    unmarked_number_sum = 0
    for row in winning_board:
        unmarked_number_sum += sum([x["number"] for x in row if not x["drawn"]])

    print(f"Result: {draw * unmarked_number_sum}")


if __name__ == "__main__":
    main()
