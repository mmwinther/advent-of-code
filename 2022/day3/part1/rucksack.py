from dataclasses import dataclass
from enum import Enum, auto
import os
from pathlib import Path
import re
from typing import List, Optional, Tuple


ITEM_PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def split_compartments(sack: str) -> Tuple[str, str]:
    sack = sack.strip()
    half_index = len(sack) // 2
    return (sack[:half_index], sack[half_index:])


def find_common_item(compartment1: str, compartment2: str) -> str:
    return (
        {char for char in compartment1}
        .intersection({char for char in compartment2})
        .pop()
    )


def get_item_value(item: str) -> int:
    return re.search(item, ITEM_PRIORITY).start() + 1


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    priority_sum = 0
    with open(data_file) as f:
        for sack in f.readlines():
            compartment1, compartment2 = split_compartments(sack)
            common_item = find_common_item(compartment1, compartment2)
            priority_sum += get_item_value(common_item)

    print(f"{priority_sum = }")


if __name__ == "__main__":
    main("test.txt")
