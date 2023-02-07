from __future__ import annotations
import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    tree = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            src, dst = line.split(' -> ')
            if src.isdecimal():
                src = int(src)
            tree[dst] = src

    return tree


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)
    circuit = dict()
    for line in commands:
        if 'AND' in line:
            parts = line.split(' ')
            a = parts[0]
            b = parts[2]
            dst = parts[4]
            circuit[dst] = a


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 1_000_000
    print('Part 1 OK')

    # assert part2('turn on 0,0 through 0,0') == 1
    # assert part2('toggle 0,0 through 999,999') == 2_000_000
    #
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 400410

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 15343601


if __name__ == '__main__':
    test()
    # main()
