import os
from collections import defaultdict

'''
part 2 solution taken from
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
    for i in positions:
        if not solution_map[i]:
            for j in positions:
                solution_map[i] += abs(i - j)

    # find the minimum by comparing the second element of each tuple
    result = min(solution_map.items(), key=lambda x: x[1])
    return result[1]


def sum_distances(nums, x):
    tot = 0
    for n in nums:
        delta = abs(n - x)
        tot += (delta * (delta + 1)) // 2
    return tot


def part2(inputFile: str):
    positions = readInput(inputFile)
    mean = sum(positions) // len(positions)
    a = sum_distances(positions, mean)
    b = sum_distances(positions, mean + 1)
    answer = min(sum_distances(positions, mean), sum_distances(positions, mean + 1))
    return answer
    '''
    solution_map = defaultdict(int)
    for i in positions:
        if not solution_map[i]:
            for j in positions:
                if i == j:
                    continue
                a = 1
                n = abs(i - j)
                #cost = ((a + n) / 2) * n
                cost = n * (n + 1) // 2
                solution_map[i] += cost

    # find the minimum by comparing the second element of each tuple
    result = min(solution_map.items(), key=lambda x: x[1])
    return result[1]
    '''


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 37
    print('Part 1 OK')
    assert part2(filename) == 168
    print('Part 2 OK\n')


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
