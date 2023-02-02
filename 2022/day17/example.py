from __future__ import annotations
from itertools import count
from operator import itemgetter

''' https://github.com/mebeim/aoc/blob/master/2022/original_solutions/day17.py '''


def loop(data):
    for i in count(0):
        yield data[i % len(data)]


def newrock(off: tuple[tuple[int, int]], topy: int) -> list[list[int, int]]:
    r = []
    for dx, dy in off:
        r.append([dx + 2, (topy + dy + 4)])
    return r


def left(r: list[tuple(int, int)]) -> None:
    for i, (x, y) in enumerate(r):
        r[i] = (x - 1, y)


def right(r: list[tuple(int, int)]) -> None:
    for i, (x, y) in enumerate(r):
        r[i] = (x + 1, y)


def down(r: list[tuple(int, int)]) -> None:
    for i, (x, y) in enumerate(r):
        r[i] = (x, y - 1)


def collision(rock: list[list[int, int]], direction: str) -> bool:
    if direction == 'l':
        if any(x == 0 for x, _ in rock):
            return True

        for x, y in rock:
            if (x - 1, y) in space:
                return True
    elif direction == 'r':
        if any(x == 6 for x, _ in rock):
            return True

        for x, y in rock:
            if (x + 1, y) in space:
                return True
    elif direction == 'd':
        if any(y == 1 for _, y in rock):
            return True

        for x, y in rock:
            if (x, y - 1) in space:
                return True
    return False


with open('input.txt', 'r') as f:
    data = f.read().strip()

offsets = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1))
]

# region part 1
moves = loop(data)
space = {(i, 0) for i in range(7)}
topy = 0

for n in range(2022):
    # eprint('=' * 20, 'rock', n + 1, '=' * 30)
    rock = newrock(offsets[n % len(offsets)], topy)

    while 1:
        move = next(moves)
        if move == '<' and not collision(rock, 'l'):
            left(rock)
        elif move == '>' and not collision(rock, 'r'):
            right(rock)

        if collision(rock, 'd'):
            space.update(map(tuple, rock))
            topy = max(map(itemgetter(1), space))
            break

        down(rock)
print(f'Solution for Part 1: {topy}')
# endregion

# region part 2
moves = loop(data)
space = {(i, 0) for i in range(7)}
topy = 0
previous = {}
n = 0
skipped = None
totrocks = 1000000000000
iteration = 0

while n < totrocks:
    rocktype = n % len(offsets)
    rock = newrock(offsets[rocktype], topy)

    while 1:
        move = next(moves)
        iteration += 1
        iteration %= len(data)

        if move == '<' and not collision(rock, 'l'):
            left(rock)
        elif move == '>' and not collision(rock, 'r'):
            right(rock)

        if collision(rock, 'd'):
            space.update(map(tuple, rock))
            topy = max(map(itemgetter(1), space))

            if skipped is None and topy > 1000:
                topchunk = []
                for x, y in space:
                    if y >= topy - 10:
                        topchunk.append((x, topy - y))

                state = (tuple(sorted(topchunk)), iteration, rocktype)

                if state in previous:
                    nn, yy = previous[state]
                    deltay = topy - yy
                    deltan = n - nn
                    print(f'pattern repeats every {deltan} rocks going up {deltay}')
                    print(f'jump fom rock {n} to {totrocks-n}')

                    steps = (totrocks - n) // deltan
                    skipped = deltay * steps
                    n += deltan * steps

                previous[state] = (n, topy)

            break

        down(rock)

    n += 1

topy += skipped
print(f'Solution for Part 2: {topy}')
# endregion
