from dataclasses import dataclass
from enum import Enum, auto
import os
from pathlib import Path
from typing import List, Optional, Tuple


class ShapeNames(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Result(Enum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()


result_points = {
    Result.WIN: 6,
    Result.DRAW: 3,
    Result.LOSS: 0,
}


@dataclass
class Shape:
    name: str
    points: int
    codes: Tuple[str]
    _beats: Tuple["ShapeNames"]

    def play(self, other: "Shape") -> Result:
        if self == other:
            return Result.DRAW
        elif other.name in self._beats:
            return Result.WIN
        else:
            return Result.LOSS


rock = Shape(ShapeNames.ROCK, 1, ("A", "X"), (ShapeNames.SCISSORS))
paper = Shape(ShapeNames.PAPER, 2, ("B", "Y"), (ShapeNames.ROCK))
scissors = Shape(ShapeNames.SCISSORS, 3, ("C", "Z"), (ShapeNames.PAPER))

shapes = [rock, paper, scissors]


def get_shape_from_code(code: str) -> Optional[Shape]:
    for s in shapes:
        if code in s.codes:
            return s


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    player_2_score = 0
    with open(data_file) as f:
        for line in f.readlines():
            player_1_shape, player_2_shape = [
                get_shape_from_code(code) for code in line.split()
            ]
            print(f"{player_1_shape.name} {player_2_shape.name}")
            result = player_2_shape.play(player_1_shape)
            points = result_points[result]
            player_2_score = player_2_score + points + player_2_shape.points

    print(f"{player_2_score = }")


if __name__ == "__main__":
    main("test.txt")
