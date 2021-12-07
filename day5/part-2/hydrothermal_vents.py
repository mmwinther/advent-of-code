import argparse
from collections import defaultdict, namedtuple
from typing import List


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        file = f.readlines()

    starts_raw = []
    ends_raw = []
    starts_cardinal = []
    ends_cardinal = []
    starts_diagonal = []
    ends_diagonal = []

    Coordinate = namedtuple("Coordinate", ["x", "y"])

    for line in file:
        parts = line.split("->")
        starts_raw.append(Coordinate(*[int(x) for x in parts[0].strip().split(",")]))
        ends_raw.append(Coordinate(*[int(x) for x in parts[-1].strip().split(",")]))

    # Sort horizontal and vertical lines from diagonal lines
    for i in range(len(starts_raw)):
        if starts_raw[i][0] == ends_raw[i][0] or starts_raw[i][-1] == ends_raw[i][-1]:
            starts_cardinal.append(starts_raw[i])
            ends_cardinal.append(ends_raw[i])
        else:
            starts_diagonal.append(starts_raw[i])
            ends_diagonal.append(ends_raw[i])

    points = defaultdict(int)

    for i in range(0, len(starts_cardinal)):
        x_low = min(starts_cardinal[i][0], ends_cardinal[i][0])
        x_high = max(starts_cardinal[i][0], ends_cardinal[i][0])
        y_low = min(starts_cardinal[i][-1], ends_cardinal[i][-1])
        y_high = max(starts_cardinal[i][-1], ends_cardinal[i][-1])
        for x in range(x_low, x_high + 1):
            for y in range(y_low, y_high + 1):
                point = Coordinate(x, y)
                points[point] += 1

    for i in range(0, len(starts_diagonal)):
        x_start = starts_diagonal[i][0]
        x_end = ends_diagonal[i][0]
        y_start = starts_diagonal[i][-1]
        y_end = ends_diagonal[i][-1]
        x_low = min(starts_diagonal[i][0], ends_diagonal[i][0])
        x_high = max(starts_diagonal[i][0], ends_diagonal[i][0])
        y_low = min(starts_diagonal[i][-1], ends_diagonal[i][-1])
        y_high = max(starts_diagonal[i][-1], ends_diagonal[i][-1])

        x_range = list(range(x_low, x_high + 1))
        y_range = list(range(y_low, y_high + 1))

        if x_start > x_end:
            x_range.reverse()

        if y_start > y_end:
            y_range.reverse()

        line_points = [Coordinate(x, y) for x, y in zip(x_range, y_range)]

        for point in line_points:
            points[point] += 1

    tally_of_overlapping_lines = len([v for v in points.values() if v > 1])

    print(f"Number of overlaps: {tally_of_overlapping_lines}")


if __name__ == "__main__":
    main()
