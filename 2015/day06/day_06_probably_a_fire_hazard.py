from __future__ import annotations
import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


def parse_line(line: str) -> list:
        line = line.replace('turn on', 'on')
        line = line.replace('turn off', 'off')
        line = line.replace(' through ', ',')
        parts = line.split(' ')
        x1, y1, x2, y2 = list(map(int, parts[1].split(',')))
        return (parts[0], (x1, y1, x2, y2))


def parse_lines(commands):
    result = []
    for cmd in commands:
        result.append(parse_line(cmd))
    return result


def solve(commands: list) -> int:
    grid = defaultdict(bool)
    for cmd, args in commands:
        x1, y1, x2, y2 = args
        x_min = min(x1, x2)
        x_max = max(x1, x2) + 1
        y_min = min(y1, y2)
        y_max = max(y1, y2) + 1
        for row in range(y_min, y_max):
            for col in range(x_min, x_max):
                key = (row, col)
                if cmd == 'on':
                    grid[key] = True
                elif cmd == 'off':
                    grid[key] = False
                else:
                    grid[key] = not grid[key]

    lights_on = 0
    for light in grid.values():
        if light == True:
            lights_on += 1

    return lights_on


def part1(inputFile: str) -> int:
    if inputFile.endswith('txt'):
        commands = readInput(inputFile)
    else:
        commands = [inputFile]

    parsed_input = parse_lines(commands)
    return solve(parsed_input)


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')

    assert part1('turn on 0,0 through 999,999') == 1_000_000
    assert part1('toggle 0,0 through 999,0') == 1000
    assert part1('turn off 499,499 through 500,500') == 0
    print('Part 1 OK')

    # assert is_nice2('qjhvhtzxzqqjkmpb') == True
    # assert is_nice2('xxyxx') == True
    # assert is_nice2('uurcxstgmygtbstg') == False
    # assert is_nice2('ieodomkazucvgmuy') == False
    #
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 400410

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
