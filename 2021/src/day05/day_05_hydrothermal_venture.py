import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    input = []
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip().replace(' -> ', ',').split(',')
            input.append([int(i) for i in line])
    return input


def filter_lines(lines: list):
    result = []
    for x0, y0, x1, y1 in lines:
        if x0 == x1 or y0 == y1:
            result.append([x0, y0, x1, y1])
    return result


def part1(inputFile: str):
    input = readInput(inputFile)
    input = filter_lines(input)

    line_count = defaultdict(int)
    for x0, y0, x1, y1 in input:
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                line_key = '%s,%s' % (x0, y)
                line_count[line_key] += 1
        else:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                line_key = '%s,%s' % (x, y0)
                line_count[line_key] += 1

    result = 0
    for value in line_count.values():
        if value >= 2:
            result += 1

    return result


def part2(inputFile: str):
    input = readInput(inputFile)

    line_count = defaultdict(int)
    for x0, y0, x1, y1 in input:

        x_step = 1 if x0 < x1 else -1
        y_step = 1 if y0 < y1 else -1

        if x0 == x1:
            for y in range(y0, y1 + y_step, y_step):
                line_key = '%s,%s' % (x0, y)
                line_count[line_key] += 1
        elif y0 == y1:
            for x in range(x0, x1 + x_step, x_step):
                line_key = '%s,%s' % (x, y0)
                line_count[line_key] += 1
        else:
            x_cords = []
            y_cords = []
            for x in range(x0, x1 + x_step, x_step):
                x_cords.append(x)
            for y in range(y0, y1 + y_step, y_step):
                y_cords.append(y)
            for i in range(len(x_cords)):
                line_key = '%s,%s' % (x_cords[i], y_cords[i])
                line_count[line_key] += 1

    result = 0
    for value in line_count.values():
        if value >= 2:
            result += 1

    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 5
    print('Part 1 OK')
    assert part2(filename) == 12
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
