import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        line = f.readline().split(',')
        return [int(i) for i in line]


def part1(inputFile: str, sim_length: int):
    fish_list = readInput(inputFile)

    for i in range(sim_length):
        new_fish_list = fish_list[:]
        for i, fish in enumerate(fish_list):
            if fish == 0:
                new_fish_list[i] = 6
                new_fish_list.append(8)
            else:
                new_fish_list[i] = fish - 1
        fish_list = new_fish_list

    return len(fish_list)


def part2(inputFile: str):
    input = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename, 80) == 5934
    print('Part 1 OK')
    #assert part2(filename) == 12
    #print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename, 80)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
