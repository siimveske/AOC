from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    cubes = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            coords = tuple(map(int, line.split(',')))
            cubes[coords] = 6
    return cubes


def neighbours(x: int, y: int, z: int) -> tuple:
    yield (x + 1, y, z)
    yield (x - 1, y, z)
    yield (x, y + 1, z)
    yield (x, y + 1, z)
    yield (x, y, z + 1)
    yield (x, y, z - 1)


def part1(inputFile: str) -> int:
    cubes: dict = readInput(inputFile)
    for cube in cubes:
        for neighbour in neighbours(*cube):
            if neighbour in cubes:
                cubes[cube] -= 1

    return sum(cubes.values())


def part2(inputFile: str) -> int:
    pattern = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 64
    print('Part 1 OK')

    # assert part2(filename) == 1514285714288
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    # assert solution_part1 == 3200
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 1584927536247
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
