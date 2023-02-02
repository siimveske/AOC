# https://github.com/mebeim/aoc/blob/master/2022/solutions/day14.py

from operator import itemgetter


def autorange(a, b):
    return range(a, b + 1) if a <= b else range(a, b - 1, -1)


def range2d(a, b):
    ax, ay = a
    bx, by = b

    if ax == bx:
        for y in autorange(ay, by):
            yield ax, y
    else:
        for x in autorange(ax, bx):
            yield x, ay


def pour_sand(cave, maxy, floor=False, x=500, y=0):
    if y == maxy and not floor:
        return True

    if y <= maxy or not floor:
        newy = y + 1

        for newx in (x, x - 1, x + 1):
            if (newx, newy) not in cave and pour_sand(cave, maxy, floor, newx, newy):
                return True

    cave.add((x, y))
    return False


cave = set()

with open("input.txt", mode="rt") as fin:
    for line in fin:
        points = (tuple(map(int, p.split(','))) for p in line.split(' -> '))
        prev = next(points)

        for cur in points:
            cave.update(range2d(prev, cur))
            prev = cur

rocks = len(cave)
maxy = max(map(itemgetter(1), cave))

pour_sand(cave, maxy)
sand = len(cave) - rocks
print(f"Part 1: resting grains={sand}")


pour_sand(cave, maxy, True)
sand = len(cave) - rocks
print(f"Part 2: resting grains={sand}")
