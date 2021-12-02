def is_increase(previous_measurement: int, current_measurement: int) -> bool:
    return current_measurement > previous_measurement


def count_depth_increase(depths: list[str]) -> int:
    previous = None
    increase_tally = 0
    for d in depths:
        d = int(d)
        if previous and is_increase(previous, d):
            increase_tally += 1
        previous = d
    return increase_tally


if __name__ == "__main__":
    file_name = input("File with depths: ")
    with open(file_name) as f:
        measurement_string = f.read()
    print(
        "Total increases: {}".format(count_depth_increase(measurement_string.split()))
    )
