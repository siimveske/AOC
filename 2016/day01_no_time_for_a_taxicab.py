import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().split(", ")


def calculate_distance(commands: list[str]) -> int:
    directions = ["N", "E", "S", "W"]
    compass = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
    x, y = 0, 0
    current_direction = "N"

    for cmd in commands:
        turn, amount = cmd[0], int(cmd[1:])
        if turn == "L":
            idx = (directions.index(current_direction) - 1) % 4
        else:
            idx = (directions.index(current_direction) + 1) % 4
        current_direction = directions[idx]
        dx, dy = compass[current_direction]
        x += dx * amount
        y += dy * amount

    distance = abs(x) + abs(y)
    return distance


def part1(filename: str) -> int:
    commands = read_input(filename)
    distance = calculate_distance(commands)
    return distance


def test():
    print("---- TEST ----")
    assert calculate_distance(["R2", "L3"]) == 5
    assert calculate_distance(["R2", "R2", "R2"]) == 2
    assert calculate_distance(["R5", "L5", "R5", "R3"]) == 12
    print("OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 307


if __name__ == "__main__":
    test()
    main()
