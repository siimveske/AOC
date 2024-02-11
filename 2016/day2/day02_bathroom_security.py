import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def part1(filename: str) -> str:
    instructions = read_input(filename)
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    code = []
    r, c = 1, 1
    length = len(keypad)
    for line in instructions:
        for direction in line:
            dr, dc = directions[direction]
            if (0 <= r + dr < length) and (0 <= c + dc < length):
                r += dr
                c += dc
        code.append(keypad[r][c])
    return "".join(map(str, code))


def part2(filename: str) -> str:
    instructions = read_input(filename)
    keypad = [
        ["", "", 1, "", ""],
        ["", 2, 3, 4, ""],
        [5, 6, 7, 8, 9],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""],
    ]
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    code = []
    row, col = 2, 0
    length = len(keypad)
    for line in instructions:
        for direction in line:
            dr, dc = directions[direction]
            r, c = row + dr, col + dc
            if (0 <= r < length) and (0 <= c < length) and (keypad[r][c] != ""):
                row, col = r, c
        code.append(keypad[row][col])
    return "".join(map(str, code))


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == "1985"
    print("Part 1: OK")

    assert part2(filename) == "5DB3"
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "52981"

    solution_part1 = part2(filename)
    print(f"Solution for Part 2: {solution_part1}")
    assert solution_part1 == "74CD2"


if __name__ == "__main__":
    test()
    main()
