import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().split(", ")


def calculate_distance(commands: list[str]) -> int:
    compass = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    directions = list(compass.keys())
    x, y, current_direction = 0, 0, 0

    for cmd in commands:
        turn, amount = cmd[0], int(cmd[1:])
        current_direction = (current_direction + (1 if turn == "R" else -1)) % 4
        dx, dy = compass[directions[current_direction]]
        x += dx * amount
        y += dy * amount

    return abs(x) + abs(y)


def calculate_distance2(commands):
    compass = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    directions = list(compass.keys())
    x, y, current_direction = 0, 0, 0
    visited = set()

    for cmd in commands:
        turn, amount = cmd[0], int(cmd[1:])
        current_direction = (current_direction + (1 if turn == "R" else -1)) % 4
        dx, dy = compass[directions[current_direction]]
        for i in range(amount):
            x += dx
            y += dy
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    raise Exception("No solution found")


def part1(filename: str) -> int:
    commands = read_input(filename)
    distance = calculate_distance(commands)
    return distance


def part2(filename: str) -> int:
    commands = read_input(filename)
    distance = calculate_distance2(commands)
    return distance


def test():
    print("---- TEST ----")
    assert calculate_distance(["R2", "L3"]) == 5
    assert calculate_distance(["R2", "R2", "R2"]) == 2
    assert calculate_distance(["R5", "L5", "R5", "R3"]) == 12
    print("Part 1: OK")

    assert calculate_distance2(["R8", "R4", "R4", "R8"]) == 4
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 307

    solution_part1 = part2(filename)
    print(f"Solution for Part 2: {solution_part1}")
    assert solution_part1 == 165


if __name__ == "__main__":
    test()
    main()
