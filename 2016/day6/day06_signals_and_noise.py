import os
from collections import Counter


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def part1(filename: str) -> str:
    message = read_input(filename)

    # Create list of letter counts {'e': 3, 'd': 2, 'v': 2, 'a': 1}
    counts = [Counter(column) for column in zip(*message)] # list of

    # Create list of most common letters
    result = [counter.most_common(1)[0][0] for counter in counts]

    return "".join(result)


def part2(filename: str) -> str:
    instructions = read_input(filename)


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == "easter"
    print("Part 1: OK")
    #
    # assert part2(filename) == "5DB3"
    # print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "xhnqpqql"

    # solution_part1 = part2(filename)
    # print(f"Solution for Part 2: {solution_part1}")
    # assert solution_part1 == "74CD2"


if __name__ == "__main__":
    test()
    main()
