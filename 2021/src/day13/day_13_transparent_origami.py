import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    coordinates = set()
    instructions = []
    width = 0
    height = 0
    with open(input_file_path, 'r') as f:

        # Parse coordinates
        for line in f:
            line = line.strip()
            if not line:
                break

            x, y = line.split(',')
            x, y = int(x), int(y)
            width = max(x, width)
            height = max(y, height)
            coordinates.add((x, y))

        # Parse fold instructions
        for line in f:
            line = line.replace('fold along', '').strip()
            key, value = line.split('=')
            instructions.append((key, int(value)))

    return (coordinates, instructions, width, height)


def fold(coordinates, instruction):
    result = set()
    axis, fold_point = instruction

    for x, y in coordinates:
        if axis == 'x':
            if x < fold_point:
                result.add((x, y))
            else:
                delta = x - fold_point
                result.add((fold_point - delta, y))
        else:
            if y < fold_point:
                result.add((x, y))
            else:
                delta = y - fold_point
                result.add((x, fold_point - delta))

    return result


def part1(inputFile: str):
    coordinates, instructions, width, height = readInput(inputFile)
    folded_coordinates = fold(coordinates, instructions[0])
    return len(folded_coordinates)


def part2(inputFile: str):
    graph = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 17
    print('Part 1 OK')
    # assert part2(filename) == 36
    # print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
