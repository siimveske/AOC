from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


def part1(inputFile: str) -> int:
    data = readInput(inputFile)

    code_characters = 0
    value_characters = 0
    for line in data:
        code_characters += len(line)
        value_characters += len(eval(line))

    return code_characters - value_characters


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 12

    print('OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 1371

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 14134


if __name__ == '__main__':
    test()
    main()
