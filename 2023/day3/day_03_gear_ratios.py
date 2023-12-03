import os
import re


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


def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 4361
    print('Part 1 OK')

    # assert part2(filename) == 2286
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 549908
    # assert solution_part2 == 72422


if __name__ == '__main__':
    test()
    main()
