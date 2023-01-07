from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        pass


def part1(inputFile: str) -> int:
    data = readInput(inputFile)


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 3068
    print('Part 1 OK')

    # assert part2(filename) == 1707
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    # assert solution_part1 == 2320
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 2967
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
