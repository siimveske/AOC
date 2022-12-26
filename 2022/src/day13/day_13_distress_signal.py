import os
from itertools import zip_longest


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    packets = []
    with open(input_file_path, 'r') as f:
        for packet in f.read().split('\n\n'):
            packets.append(list(map(eval, packet.splitlines())))
    return packets


def check(packet):
    a, b = packet
    if type(a) == list and type(b) == list:
        for left, right in zip_longest(a, b, fillvalue=None):
            if not left and right:
                return -1
            if left and not right:
                return 1

            if type(left) == int and type(right) == int:
                if left < right:
                    return -1
                elif left > right:
                    return 1
            else:
                if type(left) == int:
                    left = [left]
                if type(right) == int:
                    right = [right]
                res = check([left, right])
                if res != 0:
                    return res

    return 0


def part1(inputFile: str) -> int:
    packets = readInput(inputFile)
    correct_packages = []
    for idx, packet in enumerate(packets, 1):
        if check(packet) == -1:
            correct_packages.append(idx)
    return sum(correct_packages)


def part2(inputFile: str):
    grid = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    # assert part2(filename) == 29
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    #assert solution_part1 == 13
    # 2651 is too low
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # # assert solution_part2 == 14106266886
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
