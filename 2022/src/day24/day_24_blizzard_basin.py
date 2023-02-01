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

    def __add__(self, other) -> Point:
        return Point(self.x + other.x, self.y + other.y)


class Vector(Enum):
    """ Enumeration of 8 directions """
    N = Point(0, -1)
    E = Point(1, 0)
    S = Point(0, 1)
    W = Point(-1, 0)


class Grid():
    """ Stores a dict of all blizzard locations """

    def __init__(self, data: list[str]) -> None:
        self._directions = {
            '^': Vector.N,
            '>': Vector.E,
            'v': Vector.S,
            '<': Vector.W
        }

        self._data = data
        self._grid = self._init_grid()
        self._set_bounds()
        self._set_start_stop()

    def _init_grid(self) -> dict[Point, Point]:
        """ From input, store all current elves - marked with '#' - as a set.
        Then define the bounds. """
        grid = dict()
        for y, row in enumerate(self._data[1:-1]):
            for x, val in enumerate(row[1:-1]):
                if val in self._directions:
                    grid[Point(x,y)] = [self._directions[val].value]
        return grid

    def _set_bounds(self):
        self._min_x = 0
        self._min_y = 0
        self._max_x = len(self._data[0]) - 2
        self._max_y = len(self._data) - 2

    def _set_start_stop(self):
        self._start = Point(0, -1)
        self._end = Point(self._max_x - 1, self._max_y)

    def update_blizzards(self):
        new_grid = {}

        for location, directions in self._grid.items():
            for direction in directions:
                dx = direction.x
                dy = direction.y
                new_x = (location.x + dx) % self._max_x
                new_y = (location.y + dy) % self._max_y

                key = Point(new_x, new_y)
                val = Point(dx, dy)

                if key in new_grid:
                    new_grid[key].append(val)
                else:
                    new_grid[key] = [val]


        self._grid = new_grid


    def get_neighbors(self, location: Point) -> Point:

        neighbors = set()
        # Check if we can move to final position
        if location.x == self._max_x - 1 and location.y == self._max_y - 1:
            neighbors.add(self._end)

        # For each of the 4 cardinal directions
        for vector in list(Vector):
            neighbor: Point = location + vector.value
            # Check if we are in bounds and if there is NO blizzard here.
            if self._min_x <= neighbor.x < self._max_x and self._min_y <= neighbor.y < self._max_y and neighbor not in self._grid:
                neighbors.add(neighbor)

        # We can stand still if no blizzard hits us
        if location not in self._grid:
            neighbors.add(location)

        return neighbors


    def bfs(self):
        positions = {self._start}
        time = 0

        # While the destination is not reached.
        while self._end not in positions:
            # Advance time and evolve blizzards moving them around.
            time += 1
            self.update_blizzards()

            # For each possible position we are tracking, calculate the next valid
            # positions, and add them to a new set.
            new_positions = set()
            for pos in positions:
                neighs = self.get_neighbors(pos)
                new_positions.update(neighs)

            # Track these new positions in the next iteration.
            positions = new_positions

        return time

def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read().splitlines()

    return data


def part1(inputFile: str):
    data = readInput(inputFile)
    grid = Grid(data)
    time = grid.bfs()
    return time


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

    assert part1(filename) == 18
    print('Part 1 OK')

    # assert part2(filename) == 20
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 314

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 954


if __name__ == '__main__':
    test()
    main()
