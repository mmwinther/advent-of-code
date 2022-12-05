from dataclasses import dataclass
from enum import Enum, auto
import os
from pathlib import Path
import re
from typing import List, Optional, Tuple


def split_assignments(assignment_pair: str) -> List[List[int]]:
    return [[int(i) for i in a.split("-")] for a in assignment_pair.split(",")]


def fully_contains(assignment_1, assignment_2) -> bool:
    expanded_1 = list(range(assignment_1[0], assignment_1[1] + 1))
    expanded_2 = list(range(assignment_2[0], assignment_2[1] + 1))
    if any([x in expanded_2 for x in expanded_1]) or any(
        [x in expanded_1 for x in expanded_2]
    ):
        return True
    else:
        return False


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    tally = 0
    with open(data_file) as f:
        for assignment_pair in f.readlines():
            assignment_1, assignment_2 = split_assignments(assignment_pair)
            if fully_contains(assignment_1, assignment_2):
                tally += 1

    print(f"{tally = }")


if __name__ == "__main__":
    main("test.txt")
