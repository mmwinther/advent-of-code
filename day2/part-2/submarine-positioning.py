import enum
import argparse


class Axis(enum.Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Direction(object):
    def __init__(self, axis: Axis, sign: int):
        self.axis = axis
        self.sign = sign


class Directions(enum.Enum):
    FORWARD = Direction(Axis.HORIZONTAL, 1)
    UP = Direction(Axis.VERTICAL, -1)
    DOWN = Direction(Axis.VERTICAL, 1)


def calculate_position(commands: str):
    structured_commands = []
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    for line in commands.splitlines():
        split_line = line.split(" ")
        structured_commands.append(
            {
                "direction": Directions[split_line[0].upper()].value,
                "magnitude": int(split_line[1]),
            }
        )

    for command in structured_commands:
        if command["direction"].axis is Axis.VERTICAL:
            aim += command["magnitude"] * command["direction"].sign
        else:
            horizontal_position += command["magnitude"] * command["direction"].sign
            vertical_position += command["magnitude"] * aim

    return horizontal_position, vertical_position


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name) as f:
        commands = f.read()

    horizontal, vertical = calculate_position(commands)

    print("Result: {}".format(horizontal * vertical))
