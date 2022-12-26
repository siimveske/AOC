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

# https://github.com/mebeim/aoc/blob/master/2022/README.md#day-13---distress-signal


def compare(left, right):
    left_is_int = type(left) is int
    right_is_int = type(right) is int

    # Both integers.
    if left_is_int and right_is_int:
        return left - right

    # One is an integer, wrap it into a list and re-check.
    if left_is_int != right_is_int:
        if left_is_int:
            return compare([left], right)
        else:
            return compare(left, [right])

    # Both lists, check their items pairwise, stop at the first conclusive result.
    for x, y in zip(left, right):
        res = compare(x, y)
        if res != 0:
            return res

    # We ran out of items before coming to a conclusion. Now what matters is
    # which list was longer (according to rule number 2).
    return len(left) - len(right)


def part1(inputFile: str) -> int:
    packets = readInput(inputFile)
    answer = 0
    for idx, packet in enumerate(packets, start=1):
        if compare(*packet) < 0:
            answer += idx
    return answer


def part2(inputFile: str):
    pairs = readInput(inputFile)
    packets = []
    divider_packets = [[[2]], [[6]]]
    for packet in pairs:
        packets += packet
    packets += divider_packets
    sorted_packages = sorted(packets, key=cmp_to_key(compare))

    result = 1
    for idx, pkg in enumerate(sorted_packages, start=1):
        if pkg in divider_packets:
            result *= idx
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    assert part2(filename) == 140
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 5555
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    assert solution_part2 == 22852
    print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
