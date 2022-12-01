import os
from pathlib import Path


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    with open(data_file) as f:
        calories_per_elf = [0]
        elf = 0
        for line in f.readlines():
            if line == "\n":
                calories_per_elf.append(0)
                elf += 1
            else:
                calories_per_elf[elf] += int(line.strip())

        calories_per_elf.sort()
        top_3 = calories_per_elf[-3:]
        print(f"Top 3 elves: {top_3}\nSum: {sum(top_3)}\nOverview:{calories_per_elf}")


if __name__ == "__main__":
    main("test.txt")
