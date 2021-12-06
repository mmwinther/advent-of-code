from typing import List
import argparse


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

    days = int(args.number_of_days)
    starting_days = days
    while days > 0:
        days -= 1
        fish = new_day(fish)
        print(f"After {starting_days - days - 1} days: {len(fish)}")

    print(f"Number of fish: {len(fish)}")


if __name__ == "__main__":
    main()
