import os
from functools import cache

"""https://github.com/mebeim/aoc/blob/master/2023/solutions/day12.py"""


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        condition_records = [line.split() for line in f.read().splitlines()]
    return condition_records


@cache
def solve(record, groups, curlen=0):
    if not record:
        return not groups and curlen == 0 or len(groups) == 1 and groups[0] == curlen

    if groups and curlen > groups[0] or not groups and curlen:
        return False

    char, record = record[0], record[1:]
    total = 0

    if char in '#?':
        total += solve(record, groups, curlen + 1)

    if char in '.?':
        if not curlen:
            total += solve(record, groups, 0)
        elif curlen == groups[0]:
            total += solve(record, groups[1:], 0)

    return total


def part1(input_file: str) -> int:
    broken_records = read_input(input_file)

    total = 0
    for line in broken_records:
        records, groups = line
        groups = tuple(map(int, groups.split(',')))

        total += solve(records, groups)
        solve.cache_clear()
    return total


def part2(input_file: str) -> int:
    broken_records = read_input(input_file)

    total = 0
    for line in broken_records:
        records, groups = line
        groups = tuple(map(int, groups.split(',')))

        total += solve('?'.join([records] * 5), groups * 5)
        solve.cache_clear()
    return total


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 21

    print("Part 1 OK")

    assert part2(filename) == 525152

    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 7599
    assert solution_part2 == 15454556629917


if __name__ == "__main__":
    test()
    main()
