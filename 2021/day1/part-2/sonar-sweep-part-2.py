import os


def is_increase(previous_measurement: int, current_measurement: int) -> bool:
    return current_measurement > previous_measurement


def count_depth_increase(depths: list[str]) -> int:
    window = []
    previous = None
    increase_tally = 0

    for d in depths:
        d = int(d)
        window.append(d)
        window_size = len(window)

        if window_size < 3:
            continue
        elif window_size > 3:
            window.pop(0)

        window_sum = sum(window)
        if previous and is_increase(previous, window_sum):
            increase_tally += 1
        previous = window_sum
    return increase_tally


if __name__ == "__main__":
    file_name = input("File with depths: ")
    with open(file_name) as f:
        measurement_string = f.read()
    print(
        "Total increases: {}".format(count_depth_increase(measurement_string.split()))
    )
