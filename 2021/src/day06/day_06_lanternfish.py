import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        line = f.readline().split(',')
        return [int(i) for i in line]


def solve(inputFile: str, sim_length: int):
    input = readInput(inputFile)
    state = defaultdict(int)
    for i in input:
        state[i] += 1

    for _ in range(sim_length):
        new_state = defaultdict(int)
        for idx, val in state.items():
            idx -= 1

            if idx < 0:
                new_state[6] += val
                new_state[8] += val
            else:
                new_state[idx] += val

        state = new_state

    lanternfish_cnt = sum(state.values())
    return lanternfish_cnt


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert solve(filename, 80) == 5934
    print('Part 1 OK')
    assert solve(filename, 256) == 26984457539
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = solve(filename, 80)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = solve(filename, 256)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
