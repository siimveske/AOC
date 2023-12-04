import math
import os
import re
from collections import defaultdict


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    engine_schematic = []
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            engine_schematic.append(line)

    return engine_schematic


def part1(input_file: str) -> int:
    engine_schematic = read_input(input_file)
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])

    numbers = {}
    p = re.compile(r'\d+')
    for idx, row in enumerate(engine_schematic):
        for match in p.finditer(row):
            value = int(match.group())
            start, end = match.span()
            location = (idx, start, end - 1)
            numbers[location] = value

    sum_of_part_numbers = 0
    for cords, number in numbers.items():
        row, start, stop = cords
        done = False
        for r in range(row - 1, row + 2):
            if done:
                break
            for c in range(start - 1, stop + 2):
                if 0 <= r < rows and 0 <= c < cols:
                    item = engine_schematic[r][c]
                    if not item.isdigit() and item != '.':
                        sum_of_part_numbers += number
                        done = True
                        break

    return sum_of_part_numbers


def get_neighbours(row: int, col: int):
    top = (row - 1, col)
    top_right = (row - 1, col + 1)
    right = (row, col + 1)
    bottom_right = (row + 1, col + 1)
    bottom = (row + 1, col)
    bottom_left = (row + 1, col - 1)
    left = (row, col - 1)
    top_left = (row - 1, col - 1)
    return [top, top_right, right, bottom_right, bottom, bottom_left, left, top_left]


def part2(input_file: str) -> int:
    engine_schematic = read_input(input_file)

    stars = []
    numbers = defaultdict(list)
    digit_pattern = re.compile(r'\d+')
    star_pattern = re.compile(r'\*')
    for row, line in enumerate(engine_schematic):
        for match in digit_pattern.finditer(line):
            value = int(match.group())
            start_col, end_col = match.span()
            numbers[row].append(([(row, i) for i in range(start_col, end_col)], value))
        for match in star_pattern.finditer(line):
            column, _ = match.span()
            location = (row, column)
            stars.append(location)

    sum_of_gear_ratios = 0
    for r, c in stars:
        candidates = [numbers[i] for i in range(r - 1, r + 2) if i in numbers]
        neighbours = get_neighbours(r, c)
        gear_set = set()
        for neighbour in neighbours:
            for i in candidates:
                for j in i:
                    if neighbour in j[0]:
                        gear_set.add(j[1])
        if len(gear_set) == 2:
            sum_of_gear_ratios += math.prod(gear_set)

    return sum_of_gear_ratios


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 4361
    print('Part 1 OK')

    assert part2(filename) == 467835
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 549908
    assert solution_part2 == 81166799


if __name__ == '__main__':
    test()
    main()
