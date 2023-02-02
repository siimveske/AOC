import os
from itertools import product
from collections import deque

'''https://raw.githubusercontent.com/mebeim/aoc/master/2022/solutions/day18.py'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    cubes = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            coords = tuple(map(int, line.split(',')))
            cubes[coords] = 6
    return cubes


def neighbor(x, y, z):
    yield (x + 1, y, z)
    yield (x - 1, y, z)
    yield (x, y + 1, z)
    yield (x, y - 1, z)
    yield (x, y, z + 1)
    yield (x, y, z - 1)


def escape(cubes, node, rangex, rangey, rangez):
    queue = deque([node])
    visited = set()
    cnt = 0

    while queue:
        p = queue.popleft()
        if p in visited:
            continue

        x, y, z = p
        if x not in rangex or y not in rangey or z not in rangez:
            return (visited, 0)

        visited.add(p)

        for n in neighbor(x, y, z):
            if n in cubes:
                cnt += 1
            elif n not in visited:
                queue.append(n)

    return (visited, cnt)


def total_surface_area(cubes):
    for c in cubes:
        for n in neighbor(*c):
            if n in cubes:
                cubes[c] -= 1
    faces = sum(cubes.values())
    return faces


def bbox(cubes):
    minx = miny = minz = float('inf')
    maxx = maxy = maxz = float('-inf')
    for x, y, z in cubes:
        minx, maxx = min(x, minx), max(x, maxx)
        miny, maxy = min(y, miny), max(y, maxy)
        minz, maxz = min(z, minz), max(z, maxz)
    rangex = range(minx, maxx + 1)
    rangey = range(miny, maxy + 1)
    rangez = range(minz, maxz + 1)

    return (rangex, rangey, rangez)


def part1(inputFile: str):
    cubes = readInput(inputFile)
    faces = total_surface_area(cubes)
    return faces


def part2(inputFile: str):
    cubes = readInput(inputFile)
    faces = total_surface_area(cubes)
    rangex, rangey, rangez = bbox(cubes)
    all_visited = set()
    for n in product(rangex, rangey, rangez):
        if n not in all_visited and n not in cubes:
            visited, cnt = escape(cubes, n, rangex, rangey, rangez)
            all_visited |= visited
            faces -= cnt
    return faces


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 64

    print('Part 1 OK')
    assert part2(filename) == 58
    print('Part 2 OK\n')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 4580

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 2610


if __name__ == '__main__':
    test()
    main()
