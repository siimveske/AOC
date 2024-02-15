import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        pass


def part1(filename: str) -> int:
    addesses = read_input(filename)


def part2(filename: str) -> int:
    addesses = read_input(filename)


def test():
    print("---- TEST ----")
    print("Part 1: OK")
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 115
    #
    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 231


if __name__ == "__main__":
    test()
    main()
