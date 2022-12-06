from collections import deque
import os
from pathlib import Path
import re
from typing import List


def find_message_start(message: str, number_unique_characters: int = 4) -> int:
    buff = deque([], number_unique_characters)
    for i, char in enumerate(message):
        while char in buff:
            buff.popleft()
        buff.append(char)
        if len(buff) == buff.maxlen:
            return i + 1


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    for part, number_unique_characters in {"Part 1": 4, "Part 2": 14}.items():
        print(part)
        with open(data_file) as f:
            for message in f.readlines():
                message_start = find_message_start(message, number_unique_characters)
                print(f"{message_start = }")


if __name__ == "__main__":
    main("test.txt")
