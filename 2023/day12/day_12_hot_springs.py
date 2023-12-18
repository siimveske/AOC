import os
from itertools import combinations
from typing import List, Tuple, Any


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        condition_records = [line.split() for line in f.read().splitlines()]
    return condition_records


def valid_patterns(input_string, pattern):
    # Split the input string and pattern
    input_list = list(input_string)
    pattern = list(map(int, pattern.split(',')))

    # Recursive function to generate combinations
    def generate_combinations(line):
        if '?' not in line:
            return [''.join(line)]
        else:
            i = line.index('?')
            line[i] = '.'
            result_dot = generate_combinations(line[:])
            line[i] = '#'
            result_hash = generate_combinations(line[:])
            return result_dot + result_hash

    # Function to check if a combination is valid
    def is_valid(combination, target_pattern):
        groups = [len(group) for group in combination.split('.') if group]
        return groups == target_pattern

    # Generate all combinations and filter valid ones
    new_combinations = generate_combinations(input_list)
    valid_combinations = [combination for combination in new_combinations if is_valid(combination, pattern)]

    return valid_combinations


def part1(input_file: str) -> int:
    broken_records = read_input(input_file)
    total = 0
    for input_string, pattern in broken_records:
        patterns = valid_patterns(input_string, pattern)
        total += len(patterns)
    return total


def part2(input_file: str) -> int:
    galaxy_map = read_input(input_file)
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 21

    print("Part 1 OK")

    # assert part2(filename) == 1030
    #
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 7599
    # assert solution_part2 == 857986849428


if __name__ == "__main__":
    test()
    main()
