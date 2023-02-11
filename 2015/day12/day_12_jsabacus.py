from __future__ import annotations

import os
import re


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read()


def part1(data: str) -> int:
    numbers = re.findall(r"-?\d+", data)
    result = sum(int(i) for i in numbers)
    return result


def part2(inputFile: str) -> int:
    pass


def test():
    print("---- TEST ----")

    assert part1("[1,2,3]") == 6
    assert part1('{"a":2,"b":4}') == 6
    assert part1("[[[3]]]") == 3
    assert part1('{"a":{"b":4},"c":-1}') == 3
    assert part1('{"a":[-1,1]}') == 0
    assert part1('[-1,{"a":1}]') == 0
    assert part1("[]") == 0
    assert part1("{}") == 0

    print("OK\n")


def main():
    print("---- MAIN ----")

    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 141

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 736


if __name__ == "__main__":
    test()
    main()
