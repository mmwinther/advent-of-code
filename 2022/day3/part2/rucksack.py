import os
from pathlib import Path
import re
from typing import List, Set


ITEM_PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_common_item(elf_group: List[str]) -> str:
    common: Set = {char for char in elf_group.pop()}
    for group in elf_group:
        common = common.intersection({char for char in group})
    return common.pop()


def get_item_value(item: str) -> int:
    return re.search(item, ITEM_PRIORITY).start() + 1


def group_full(index: int) -> bool:
    return (index + 1) % 3 == 0


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    priority_sum = 0
    current_group = []
    with open(data_file) as f:
        for i, sack in enumerate(f.readlines()):
            current_group.append(sack.strip())
            if group_full(i):
                common_item = find_common_item(current_group)
                priority_sum += get_item_value(common_item)
                current_group = []

    print(f"{priority_sum = }")


if __name__ == "__main__":
    main("test.txt")
