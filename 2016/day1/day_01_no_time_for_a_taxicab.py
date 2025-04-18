import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().split(", ")


def turn(current_direction, turn_direction):
    #  2d vector (x, y) rotated counter clockwise (L) by 90 degrees is (-y, x)
    #  2d vector (x, y) rotated clockwise (R) by 90 degrees is (y, -x)
    x, y = current_direction
    return (-y, x) if turn_direction == "L" else (y, -x)


def calculate_distance(commands: list[str], return_on_revisit=False) -> int:
    x, y = 0, 0
    current_direction = (0, 1)
    visited = set()

    for cmd in commands:
        turn_direction, amount = cmd[0], int(cmd[1:])
        current_direction = turn(current_direction, turn_direction)
        dx, dy = current_direction
        for i in range(amount):
            x, y = x + dx, y + dy
            if return_on_revisit and (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    if return_on_revisit:
        raise Exception("No solution found")
    else:
        return abs(x) + abs(y)


def part1(filename: str) -> int:
    commands = read_input(filename)
    distance = calculate_distance(commands)
    return distance


def part2(filename: str) -> int:
    commands = read_input(filename)
    distance = calculate_distance(commands, return_on_revisit=True)
    return distance


def test():
    print("---- TEST ----")
    assert calculate_distance(["R2", "L3"]) == 5
    assert calculate_distance(["R2", "R2", "R2"]) == 2
    assert calculate_distance(["R5", "L5", "R5", "R3"]) == 12
    print("Part 1: OK")

    assert calculate_distance(["R8", "R4", "R4", "R8"], return_on_revisit=True) == 4
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
