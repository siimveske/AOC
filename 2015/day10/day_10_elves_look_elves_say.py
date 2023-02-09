from __future__ import annotations

import os
from collections import defaultdict
import itertools


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read()


def process(data: str) -> str:
    cnt = 1
    current = None
    result = []
    for i in range(1, len(data)):
        current = data[i]
        prev = data[i - 1]
        if current != prev:
            result.append(str(cnt))
            result.append(str(prev))
            cnt = 1
        else:
            cnt += 1
    else:
        result.append(str(cnt))
        result.append(str(current))
    return "".join(result)


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    for _ in range(40):
        data = process(data)
    return len(data)


def part2(inputFile: str) -> int:
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    # assert part1(filename) == "11"
    assert process("11") == "21"
    assert process("21") == "1211"
    assert process("1211") == "111221"
    assert process("111221") == "312211"
    # assert part2(filename) == 982

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 141

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 736


if __name__ == "__main__":
    test()
    main()
