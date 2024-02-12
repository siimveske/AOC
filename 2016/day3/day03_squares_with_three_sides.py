import os


def read_input(filename: str) -> list[tuple[int, int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    triangles = []
    with open(input_file_path, "r") as f:
        for line in f:
            sides = line.strip().split()
            a, b, c = map(int, sides)
            triangles.append((a, b, c))
    return triangles


def part1(filename: str) -> int:
    triangles = read_input(filename)
    filtered_triangles = []
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            filtered_triangles.append((a, b, c))
    return len(filtered_triangles)


def part2(filename: str) -> str:
    instructions = read_input(filename)


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
    assert solution_part1 == 993
    #
    # solution_part1 = part2(filename)
    # print(f"Solution for Part 2: {solution_part1}")
    # assert solution_part1 == "74CD2"


if __name__ == "__main__":
    # test()
    main()
