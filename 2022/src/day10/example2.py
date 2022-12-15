import os
import sys


def solve(input, target_cycles=None):
    x_register = {}
    cycle = 1
    x = 1

    def save():
        if (target_cycles is None) or (cycle in target_cycles):
            x_register[cycle] = x

    for instruction in input:
        if instruction.startswith('noop'):
            save()
            cycle += 1
        else:
            op, v = instruction.split()
            if op == 'addx':
                save()
                cycle += 1
                save()
                cycle += 1
                x += int(v)
            else:
                raise Exception('Unknown instruction:', instruction)

    return x_register


def part1(input):
    target_cycles = [20, 60, 100, 140, 180, 220]
    x_register = solve(input, target_cycles)
    return sum(x_register[c] * c for c in target_cycles)


def part2(input):
    def overlap(pixel_pos, sprite_pos):
        return sprite_pos - 1 <= pixel_pos <= sprite_pos + 1

    CRT_WIDTH = 40
    CRT_HEIGHT = 6
    x_registers = solve(input)
    cycle = 1

    for row in range(CRT_HEIGHT):
        for pixel_pos in range(CRT_WIDTH):
            pixel = '▓' if overlap(pixel_pos, x_registers[cycle]) else '░'
            print(pixel, end='')
            cycle += 1

        print('')

    return ''


def main():
    file = 'input.txt'
    with open(file, 'r') as f:
        input = [line.rstrip() for line in f.readlines()]

    print(f'Part 1 {part1(input)}')
    print('Part 2:')
    part2(input)


if __name__ == '__main__':
    main()
