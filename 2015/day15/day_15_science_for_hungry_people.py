from __future__ import annotations

import math
import os
import re


def readInput(filename: str) -> list[tuple[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    ingredients = []
    numbers = re.compile("-?\d+")
    with open(input_file_path, "r") as f:
        for line in f:
            items = tuple(map(int, re.findall(numbers, line)))
            ingredients.append(items)

    ingredients = list(zip(*ingredients))  # swap rows to cols
    return ingredients


def calc_score(amounts: tuple, property: tuple) -> int:
    return sum(amount * property for amount, property in zip(amounts, property))


def calc_scores(amounts: tuple, properties: tuple) -> int:
    return math.prod(
        max(0, calc_score(amounts, property)) for property in properties[:-1]
    )

def combinations(n: int, total: int) -> list[tuple[int]]:
    '''generate all possible combinations of n numbers that sum to total'''
    if n == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for c in combinations(n - 1, total - i):
                yield (i,) + c

def part1(properties: list) -> int:
    result = 0
    num_of_teaspoons = 100
    num_of_ingredients = len(properties[0])
    for combination in combinations(num_of_ingredients, num_of_teaspoons):
        score = calc_scores(combination, properties)
        result = max(result, score)
    return result


def part2(properties: list) -> int:
    result = 0
    num_of_teaspoons = 100
    max_calories = 500
    num_of_ingredients = len(properties[0])
    for combination in combinations(num_of_ingredients, num_of_teaspoons):
        score = calc_scores(combination, properties)
        if score > result and calc_score(combination, properties[-1]) == max_calories:
            result = score
    return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    data = readInput(filename)

    assert part1(data) == 62842880
    assert part2(data) == 57600000

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 222870

    solution_part2 = part2(data)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 117936


if __name__ == "__main__":
    test()
    main()
