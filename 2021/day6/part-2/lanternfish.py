from typing import List
import argparse
from collections import defaultdict


def new_day(fish: List[int]) -> List[int]:
    new_day_fish = fish
    for i, f in enumerate(fish):
        if f == 0:
            new_day_fish[i] = 6
            new_day_fish.append(9)
        else:
            new_day_fish[i] -= 1

    return fish


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_days")
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        fish = [int(i) for i in f.read().strip().split(",")]

    lanternfish = defaultdict(int)

    for f in fish:
        lanternfish[f] += 1

    days = int(args.number_of_days)
    starting_days = days
    while days > 0:
        days -= 1
        next_day = defaultdict(int)
        for timer, tally in lanternfish.items():
            print(f"Timer: {timer}, Tally: {tally}")
            if timer == 0:
                next_day[6] += tally
                next_day[8] += tally
            else:
                next_day[timer - 1] += tally

        lanternfish = next_day

        print(
            f"After {starting_days - days - 1} days: {sum(list(lanternfish.values()))}"
        )

    print(f"Number of fish: {sum(list(lanternfish.values()))}")


if __name__ == "__main__":
    main()
