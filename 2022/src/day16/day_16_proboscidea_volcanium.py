from __future__ import annotations
from dataclasses import dataclass
import os
import re


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    # Find four digits, preceeded by "not digit"
    pattern = re.compile(r"[\D]+x=(-?\d+)[\D]+y=(-?\d+)[\D]+x=(-?\d+)[\D]+y=(-?\d+)")
    sensor_to_beacon: dict[Point, Point] = {}

    with open(input_file_path, 'r') as f:
        for line in f:
            sx, sy, bx, by = map(int, pattern.findall(line)[0])
            sensor_to_beacon[Point(sx, sy)] = Point(bx, by)

    return sensor_to_beacon


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    return 0


def part2(inputFile: str):
    data = readInput(inputFile)
    return 0


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 26
    print('Part 1 OK')

    assert part2(filename) == 56000011
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    #assert solution_part1 == 4737443
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 11482462818989
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
