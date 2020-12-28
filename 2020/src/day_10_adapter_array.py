import os
from collections import defaultdict


def load_program(file: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        jolts = sorted([int(line) for line in file])
        jolts = [0, *jolts, jolts[-1] + 3]

    return jolts


def get_diff(jolts):
    diffs = [0, 0, 0, 0]

    for i in range(1, len(jolts)):
        difference = jolts[i] - jolts[i - 1]
        diffs[difference] += 1

    return diffs[1] * diffs[3]


def get_paths(jolts):
    paths = defaultdict(int)
    paths[0] = 1

    for j in jolts[1:]:
        paths[j] = paths[j - 1] + paths[j - 2] + paths[j - 3]

    return paths[jolts[-1]]


def test():
    file = os.path.join('..', 'test', 'day_10_input.txt')

    jolts = load_program(file)
    diff = get_diff(jolts)
    paths = get_paths(jolts)

    assert diff == 35
    assert paths == 8


def main():
    file = os.path.join('..', 'data', 'day_10_input.txt')

    jolts = load_program(file)
    diff = get_diff(jolts)
    paths = get_paths(jolts)

    print('part1: ', diff)
    print('part2: ', paths)


if __name__ == '__main__':
    test()
    main()
