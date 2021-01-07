import os
from itertools import product


def parse_input(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        grid = [line.strip() for line in file]

    cube = set()
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '#':
                cube.add((x, y, 0))

    return cube


def neighbors(x, y, z):
    for px in range(x - 1, x + 2):
        for py in range(y - 1, y + 2):
            for pz in range(z - 1, z + 2):
                yield px, py, pz


def alive_neighbors(cube, coords):
    alive = 0
    for n in neighbors(*coords):
        if (n in cube) and (n != coords):
            alive += 1

    return alive


def all_neighbors(cube):
    return set(n for p in cube for n in neighbors(*p))


def evolve(cube):
    new_cube = set()
    for neighbor in all_neighbors(cube):
        alive_cnt = alive_neighbors(cube, neighbor)

        if neighbor in cube:
            if alive_cnt == 2 or alive_cnt == 3:
                # alive cell stays alive only if exactly 2 or 3 neighbors are alive
                new_cube.add(neighbor)
        elif alive_cnt == 3:
            # dead cell becomes alive only if exactly 3 neighbors are alive
            new_cube.add(neighbor)

    return new_cube


def part1(file):
    cube = parse_input(file)
    for _ in range(6):
        cube = evolve(cube)

    total_alive = len(cube)
    print('Part 1:', total_alive)
    return total_alive


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_17_input.txt')
    assert part1(file) == 112


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_17_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    main()
