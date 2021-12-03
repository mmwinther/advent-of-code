from typing import List
import argparse


def sum_list_of_lists(list_of_lists: List[List[int]]) -> List[int]:
    """Sum the first elements in each list, the second elements, and so on"""
    return [sum(i) for i in zip(*list_of_lists)]


def one_big_string_to_list_of_lists(one_big_string: str) -> List[List[int]]:
    list_of_lists = []
    for line in one_big_string.splitlines():
        list_of_lists.append([int(i) for i in line])
    return list_of_lists


def calculate_gamma_rate(sum_of_elements: List[int], number_of_samples: int) -> int:
    return int("".join([str(round(x / number_of_samples)) for x in sum_of_elements]), 2)


def calculate_epsilon_rate(sum_of_elements: List[int], number_of_samples: int) -> int:
    return int(
        "".join([str(round(1 - (x / number_of_samples))) for x in sum_of_elements]), 2
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        diagnostic_report = f.read()

    list_of_lists = one_big_string_to_list_of_lists(diagnostic_report)
    gamma_rate = calculate_gamma_rate(
        sum_list_of_lists(list_of_lists), len(list_of_lists)
    )
    epsilon_rate = calculate_epsilon_rate(
        sum_list_of_lists(list_of_lists), len(list_of_lists)
    )

    print(bin(gamma_rate))

    print(
        f"Gamma rate: {gamma_rate} | Epsilon rate: {epsilon_rate} | Multiplied: {gamma_rate * epsilon_rate}"
    )


if __name__ == "__main__":
    main()
