import os
from collections import defaultdict

'''
part 2 fast solution taken from:
https://github.com/mebeim/aoc/tree/master/2021#day-7---the-treachery-of-whales
'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        line = f.readline().split(',')
        return [int(i) for i in line]


def part1(inputFile: str):
    positions = readInput(inputFile)
    solution_map = defaultdict(int)
    start = min(positions)
    end = max(positions) + 1

    for i in range(start, end):
        for j in positions:
            if i == j:
                continue
            solution_map[i] += abs(i - j)

    # find the minimum by comparing the second element of each tuple
    result = min(solution_map.items(), key=lambda x: x[1])
    return result[1]


def part2(inputFile: str):
    positions = readInput(inputFile)
    solution_map = defaultdict(int)
    start = min(positions)
    end = max(positions) + 1

    for i in range(start, end):  # all valid places
        for j in positions:  # number to be moved
            if i == j:
                continue
            delta = abs(i - j)
            cost = (delta * (delta + 1)) // 2
            solution_map[i] += cost

    result = min(solution_map.items(), key=lambda x: x[1])
    return result[1]


def sum_distances(nums, x):
    tot = 0
    for n in nums:
        delta = abs(n - x)
        tot += (delta * (delta + 1)) // 2
    return tot


def part2_fast(inputFile: str):
    positions = readInput(inputFile)
    mean = sum(positions) // len(positions)
    a = sum_distances(positions, mean)
    b = sum_distances(positions, mean + 1)
    answer = min(sum_distances(positions, mean), sum_distances(positions, mean + 1))
    return answer


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 37
    print('Part 1 OK')
    assert part2(filename) == 168
    print('Part 2 OK')
    assert part2_fast(filename) == 168
    print('Part 2 Fast OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
