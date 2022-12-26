import os
from functools import cmp_to_key


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    packets = []
    with open(input_file_path, 'r') as f:
        for packet in f.read().split('\n\n'):
            packets.append(list(map(eval, packet.splitlines())))
    return packets


def part1(inputFile: str) -> int:
    packets = readInput(inputFile)


def part2(inputFile: str):
    pairs = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    # assert part2(filename) == 140
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 5555
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 22852
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
