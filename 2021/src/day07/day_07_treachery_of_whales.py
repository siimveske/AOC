import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        line = f.readline().split(',')
        return [int(i) for i in line]


def solve(inputFile: str):
    positions = readInput(inputFile)
    solution_map = defaultdict(int)
    for i in positions:
        if not solution_map[i]:
            for j in positions:
                solution_map[i] += abs(i - j)

    # find the minimum by comparing the second element of each tuple
    result = min(solution_map.items(), key=lambda x: x[1])
    return result[1]


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert solve(filename) == 37
    print('Part 1 OK')
    # assert solve(filename, 256) == 26984457539
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = solve(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = solve(filename, 256)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
