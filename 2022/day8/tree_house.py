from functools import reduce
import os
from pathlib import Path
from pprint import pprint
from typing import List


def tree_visible(x: int, y: int, tree: int, row: List[int], column: List[int]) -> bool:
    return (
        x in [0, len(row) - 1]
        or y in [0, len(column) - 1]
        or all([i < tree for i in row[:x]])
        or all([i < tree for i in row[x + 1 :]])
        or all([i < tree for i in column[:y]])
        or all([i < tree for i in column[y + 1 :]])
    )


def calculate_scenic_score(
    x: int, y: int, tree: int, row: List[int], column: List[int]
) -> int:
    if x in [0, len(row) - 1] or y in [0, len(column) - 1]:
        # We know one direction will be 0 so just return 0
        return 0
    else:
        scores = []
        for direction in [
            reversed(row[:x]),
            row[x + 1 :],
            reversed(column[:y]),
            column[y + 1 :],
        ]:
            i = 0
            for neighbour in direction:
                i += 1
                if tree <= neighbour:
                    break
            scores.append(i)
        return reduce(lambda x, y: x * y, scores)


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    tree_heights: List[List[int]] = []
    with open(data_file) as f:
        for line in f.readlines():
            tree_heights.append([int(h) for h in line.strip()])

    visible_trees = 0
    scenic_scores = []
    for y, row in enumerate(tree_heights):
        for x, tree in enumerate(row):
            column = [row[x] for row in tree_heights]
            visible = tree_visible(x, y, tree, row.copy(), column)
            scenic_scores.append(calculate_scenic_score(x, y, tree, row.copy(), column))
            if visible:
                visible_trees += 1

    print(f"PART 1: {visible_trees = }")
    print(f"PART 2: Highest scenic score = {max(scenic_scores)}")


if __name__ == "__main__":
    main("test.txt")
