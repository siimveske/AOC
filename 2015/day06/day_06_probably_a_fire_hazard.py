from __future__ import annotations
import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    commands = []

    if filename.endswith('txt'):
        with open(input_file_path, 'r') as f:
            for line in f:
                commands.append(parse_line(line.strip()))
    else:
        commands.append(parse_line(filename))

    return commands


def parse_line(line: str) -> list:
        line = line.replace('turn on', 'on')
        line = line.replace('turn off', 'off')
        line = line.replace(' through ', ',')
        cmd, args = line.split(' ')
        x1, y1, x2, y2 = list(map(int, args.split(',')))

        return (cmd, (x1, y1, x2, y2))


def toggle_lights(commands: list) -> dict[tuple(int, int), int]:
    lights = defaultdict(int)
    for cmd, args in commands:
        x1, y1, x2, y2 = args
        for row in range(y1, y2 + 1):
            for col in range(x1, x2 + 1):
                key = (row, col)
                if cmd == 'on':
                    lights[key] = True
                elif cmd == 'off':
                    lights[key] = False
                else:
                    lights[key] = not lights[key]
    return lights


def toggle_lights2(commands: list) -> dict[tuple(int, int), int]:
    lights = defaultdict(int)
    for cmd, args in commands:
        x1, y1, x2, y2 = args
        for row in range(y1, y2 + 1):
            for col in range(x1, x2 + 1):
                key = (row, col)
                if cmd == 'on':
                    lights[key] += 1
                elif cmd == 'off':
                    lights[key] = max(0, lights[key] - 1)
                else:
                    lights[key] += 2
    return lights


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)
    lights = toggle_lights(commands)
    lights_on = sum(lights.values())
    return lights_on


def part2(inputFile: str) -> int:
    commands = readInput(inputFile)
    lights = toggle_lights2(commands)
    total_brightness = sum(lights.values())
    return total_brightness


def test():
    print('---- TEST ----')

    assert part1('turn on 0,0 through 999,999') == 1_000_000
    assert part1('toggle 0,0 through 999,0') == 1000
    assert part1('turn off 499,499 through 500,500') == 0
    print('Part 1 OK')

    assert part2('turn on 0,0 through 0,0') == 1
    assert part2('toggle 0,0 through 999,999') == 2_000_000

    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 400410

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 15343601


if __name__ == '__main__':
    test()
    main()
