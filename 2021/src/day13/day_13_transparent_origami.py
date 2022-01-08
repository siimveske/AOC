import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    sheet = set()
    instructions = []
    with open(input_file_path, 'r') as f:

        # Parse coordinates
        for line in f:
            line = line.strip()
            if not line:
                break
            x, y = line.split(',')
            sheet.add((int(x), int(y)))

        # Parse fold instructions
        for line in f:
            line = line.replace('fold along', '').strip()
            key, value = line.split('=')
            instructions.append((key, int(value)))

    return (sheet, instructions)


def fold(sheet, instruction):
    result = set()
    axis, fold_point = instruction

    for x, y in sheet:
        if axis == 'x':
            if x > fold_point:
                delta = x - fold_point
                x = fold_point - delta
        else:
            if y > fold_point:
                delta = y - fold_point
                y = fold_point - delta
        result.add((x, y))

    return result


def print_sheet(sheet):
    width = 0
    height = 0
    for x, y in sheet:
        width = max(width, x)
        height = max(height, y)
    for y in range(height + 1):
        for x in range(width + 1):
            if (x, y) in sheet:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def part1(inputFile: str):
    sheet, instructions = readInput(inputFile)
    folded_sheet = fold(sheet, instructions[0])
    return len(folded_sheet)


def part2(inputFile: str):
    sheet, instructions = readInput(inputFile)
    for instruction in instructions:
        sheet = fold(sheet, instruction)
    return sheet


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 17
    print('Part 1 OK')
    solution_part2 = part2(filename)
    assert len(solution_part2) == 16
    print('Part 2 OK')
    print_sheet(solution_part2)


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2:')
    print_sheet(solution_part2)


if __name__ == '__main__':
    test()
    main()
