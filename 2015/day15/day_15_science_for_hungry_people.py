from __future__ import annotations

import math
import os
import re
from collections import defaultdict


def readInput(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    ingredients = []
    numbers = re.compile("-?\d+")
    with open(input_file_path, "r") as f:
        for line in f:
            items = tuple(map(int, re.findall(numbers, line)))
            ingredients.append(items)

    ingredients = tuple(zip(*ingredients))  # swap rows to cols
    return ingredients


def calc_score(amounts, property):
    return sum(amount * property for amount, property in zip(amounts, property))


def calc_scores(amounts, properties):
    return math.prod(
        max(0, calc_score(amounts, property)) for property in properties[:-1]
    )


def combinations() -> tuple[int, int, int, int]:
    TOTAL = 100
    for a in range(TOTAL):
        for b in range(TOTAL - a):
            for c in range(TOTAL - a - b):
                d = TOTAL - a - b - c
                yield (a, b, c, d)


def part1(properties: list) -> int:
    pt1 = pt2 = 0
    for combination in combinations():
        score = calc_scores(combination, properties)
        pt1 = max(pt1, score)
        if score > pt2 and calc_score(combination, properties[-1]) == 500:
            pt2 = score
    return pt1, pt2


def part2(data: list) -> int:
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    data = readInput(filename)

    part1(data)
    # part2(data)

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 2660

    # solution_part2 = part2(data)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 1256


if __name__ == "__main__":
    test()
    main()
