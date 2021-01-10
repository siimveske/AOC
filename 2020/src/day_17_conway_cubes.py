import os
from itertools import product


def parse_input(file, N):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        grid = [line.strip() for line in file]

    cube = set()
    zeroes = [0] * (N - 2)
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '#':
                cube.add((x, y, *zeroes))

    return cube


def neighbors(coords):
    ranges = ((c - 1, c, c + 1) for c in coords)
    yield from product(*ranges)


def count_active_neighbors(cube, coords):
    active_cnt = 0
    for n in neighbors(coords):
        if (n in cube) and (n != coords):
            active_cnt += 1

    return active_cnt


def all_neighbors(cube):
    return set(neighbor for coord in cube for neighbor in neighbors(coord))


def evolve(cube):
    new_cube = set()
    for neighbor in all_neighbors(cube):
        active_cnt = count_active_neighbors(cube, neighbor)

        if neighbor in cube:
            if active_cnt == 2 or active_cnt == 3:
                # alive cell stays alive only if exactly 2 or 3 neighbors are alive
                new_cube.add(neighbor)
        elif active_cnt == 3:
            # dead cell becomes alive only if exactly 3 neighbors are alive
            new_cube.add(neighbor)

    return new_cube


def solve(file, N):
    cube = parse_input(file, N)
    for _ in range(6):
        cube = evolve(cube)
    active_cnt = len(cube)
    return active_cnt


def part1(file):
    active_cnt = solve(file, N=3)
    print('Part 1:', active_cnt)
    return active_cnt


def part2(file):
    active_cnt = solve(file, N=4)
    print('Part 2:', active_cnt)
    return active_cnt


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_17_input.txt')
    assert part1(file) == 112
    assert part2(file) == 848


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_17_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    #test()
    main()
