from __future__ import annotations

import os
import functools


def readInput(filename: str) -> str:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read()


@functools.cache
def next_number(number: str) -> str:
    """Generate next Look-and-Say Sequence number
    url: https://youtu.be/_1Wp4Bww8Rs"""
    result = []
    i = 0
    while i < len(number):
        cnt = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            i += 1
            cnt += 1
        result.append(str(cnt))
        result.append(number[i])
        i += 1
    return "".join(result)


def nth_number(number: str, iterations: int) -> str:
    for _ in range(iterations):
        number = next_number(number)
    return number


def part1(inputFile: str) -> int:
    number = readInput(inputFile)
    result = nth_number(number, 40)
    return len(result)


def part2(inputFile: str) -> int:
    number = readInput(inputFile)
    result = nth_number(number, 50)
    return len(result)


def test():
    print("---- TEST ----")
    assert next_number("11") == "21"
    assert next_number("21") == "1211"
    assert next_number("1211") == "111221"
    assert next_number("111221") == "312211"
    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 329356

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 4666278


if __name__ == "__main__":
    test()
    main()
