from typing import List, Callable
import argparse


def sum_list_of_lists(list_of_lists: List[List[int]]) -> List[int]:
    """Sum the first elements in each list, the second elements, and so on"""
    return [sum(i) for i in zip(*list_of_lists)]


def one_big_string_to_list_of_lists(one_big_string: str) -> List[List[int]]:
    list_of_lists = []
    for line in one_big_string.splitlines():
        list_of_lists.append([int(i) for i in line])
    return list_of_lists


def find_lists_with_value_commonality(
    lists: List[List[int]], index, commonality_function: Callable
) -> List[List[int]]:

    lists_with_commonality = commonality_function(lists, index)

    index += 1

    if len(lists_with_commonality) > 1:
        lists_with_commonality = find_lists_with_value_commonality(
            lists_with_commonality, index, commonality_function
        )

    return lists_with_commonality


def lists_with_most_common_bit(
    list_of_lists: List[List[int]], index: int
) -> List[List[int]]:
    index_tally = sum_list_of_lists(list_of_lists)
    division_result = index_tally[index] / len(list_of_lists)
    if division_result == 0.5:
        most_common_bit = 1
    else:
        most_common_bit = round(division_result)
    return [l for l in list_of_lists if l[index] == most_common_bit]


def lists_with_least_common_bit(
    list_of_lists: List[List[int]], index: int
) -> List[List[int]]:
    index_tally = sum_list_of_lists(list_of_lists)
    division_result = 1 - (index_tally[index] / len(list_of_lists))
    if division_result == 0.5:
        most_common_bit = 0
    else:
        most_common_bit = round(division_result)
    return [l for l in list_of_lists if l[index] == most_common_bit]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        diagnostic_report = f.read()

    list_of_lists = one_big_string_to_list_of_lists(diagnostic_report)

    oxygen_generator_rating_binary = find_lists_with_value_commonality(
        list_of_lists, 0, lists_with_most_common_bit
    )

    co2_scrubber_rating_binary = find_lists_with_value_commonality(
        list_of_lists, 0, lists_with_least_common_bit
    )

    oxygen_generator_rating = int(
        "".join([str(i) for i in oxygen_generator_rating_binary[0]]), 2
    )
    co2_scrubber_rating = int(
        "".join([str(i) for i in co2_scrubber_rating_binary[0]]), 2
    )

    print(
        f"Oxygen Generator: {oxygen_generator_rating} | CO2 Scrubber: {co2_scrubber_rating} | Multiplied: {oxygen_generator_rating * co2_scrubber_rating}"
    )


if __name__ == "__main__":
    main()
