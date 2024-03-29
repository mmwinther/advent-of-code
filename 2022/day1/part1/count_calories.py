from pathlib import Path
import os


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

        print(f"Max calories: {max(calories_per_elf)}\nOverview:{calories_per_elf}")


if __name__ == "__main__":
    main("calories.txt")
