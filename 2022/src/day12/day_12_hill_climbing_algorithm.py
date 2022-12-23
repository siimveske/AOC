import os
from collections import deque
from math import lcm


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        monkeys = f.read()
        monkeys = monkeys.split('\n\n')

    return parsed_monkeys


def part1(inputFile: str) -> int:
    monkeys = readInput(inputFile)


def part2(inputFile: str):
    monkeys = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 10605
    print('Part 1 OK')

    # assert part2(filename) == 2713310158
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 57348
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 14106266886
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
