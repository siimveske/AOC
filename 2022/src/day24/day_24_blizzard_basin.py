from __future__ import annotations
from collections import deque, defaultdict
from dataclasses import dataclass
from enum import Enum
import os

'''Inspired by: https://aoc.just2good.co.uk/2022/23'''


@dataclass(frozen=True)
class Point():

    x: int
    y: int

    def all_neighbours(self) -> set[Point]:
        return {(self + vector.value) for vector in list(Vector)}

    def get_neighbours(self, directions: list[Vector]) -> set[Point]:
        return {(self + vector.value) for vector in list(directions)}

    def __add__(self, other) -> Point:
        return Point(self.x + other.x, self.y + other.y)


class Vector(Enum):
    """ Enumeration of 8 directions """
    N = Point(0, -1)
    NE = Point(1, -1)
    E = Point(1, 0)
    SE = Point(1, 1)
    S = Point(0, 1)
    SW = Point(-1, 1)
    W = Point(-1, 0)
    NW = Point(-1, -1)


class Grid():
    """ Stores a set of all elf positions. """

    def __init__(self, grid: list[str]) -> None:
        self._grid = grid
        self._elves: set[Point] = set()
        self._initialise_elves()

        self._directions = deque([  # use a deque so we can rotate
            ([Vector.N, Vector.NE, Vector.NW], Vector.N),
            ([Vector.S, Vector.SE, Vector.SW], Vector.S),
            ([Vector.W, Vector.NW, Vector.SW], Vector.W),
            ([Vector.E, Vector.NE, Vector.SE], Vector.E)
        ])

    def _initialise_elves(self):
        """ From input, store all current elves - marked with '#' - as a set.
        Then define the bounds. """
        for y, row in enumerate(self._grid):
            for x, val in enumerate(row):
                if val == "#":
                    self._elves.add(Point(x, y))

    def _set_bounds(self):
        self._min_x = min(point.x for point in self._elves)
        self._max_x = max(point.x for point in self._elves)
        self._min_y = min(point.y for point in self._elves)
        self._max_y = max(point.y for point in self._elves)

    def iterate(self) -> int:
        """ Perform a single iteration by following the rules.
        Returns: the number of elves that moved. """
        proposals: dict = {}  # E.g. {elf point: proposed point}
        for elf_locn in self._elves:  # for every existing elf location

            # check if this elf has any immediate neighbours
            if elf_locn.all_neighbours().isdisjoint(self._elves):
                continue  # no neighbours are elves; this elf does nothing

            for direction_checks, proposed_direction in self._directions:
                if elf_locn.get_neighbours(direction_checks).isdisjoint(self._elves):
                    proposals[elf_locn] = elf_locn + proposed_direction.value
                    break  # exit at the first matching direction

        # turn into {proposed locn: [elf1_locn, elf2_locn, ...], ...}
        elves_per_proposal = defaultdict(list)
        for elf_locn, proposal in proposals.items():
            elves_per_proposal[proposal] += [elf_locn]

        # Only move elves that have made a unique proposal
        for add, rem in elves_per_proposal.items():
            if len(rem) == 1:
                self._elves.add(add)
                self._elves.remove(rem[0])

        self._rotate_direction()

        return len(elves_per_proposal)

    def _rotate_direction(self):
        """ Rotate our directions.  I.e. direction n+1 becomes direction n, etc. """
        self._directions.rotate(-1)

    def score(self) -> int:
        """ Count empty squares within the bounds """
        self._set_bounds()
        total_tiles = (self._max_x + 1 - self._min_x) * (self._max_y + 1 - self._min_y)
        elf_count = len(self._elves)

        return total_tiles - elf_count


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read().splitlines()

    return data


def part1(inputFile: str):
    data = readInput(inputFile)
    grid = Grid(data)

    current_round = 1
    for _ in range(10):
        grid.iterate()
        current_round += 1

    return grid.score()


def part2(inputFile: str):
    data = readInput(inputFile)
    grid = Grid(data)

    current_round = 1
    while grid.iterate() > 0:
        current_round += 1

    return current_round


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 110
    print('Part 1 OK')

    assert part2(filename) == 20
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 3766

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 954


if __name__ == '__main__':
    test()
    main()
