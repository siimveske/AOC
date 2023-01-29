from __future__ import annotations
from collections import deque, defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "test_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

OUTPUT_FOLDER = Path(SCRIPT_DIR, "output/")

@dataclass(frozen=True)
class Point():
    """ Point x,y which knows how to add another point,
    and how to return all adjacent points, including diagonals. """
    x: int
    y: int

    def all_neighbours(self) -> set[Point]:
        """ Return all adjacent orthogonal (not diagonal) Points """
        return {(self + vector.value) for vector in list(Vector)}

    def get_neighbours(self, directions: list[Vector]) -> set[Point]:
        return {(self + vector.value) for vector in list(directions)}

    def __add__(self, other) -> Point:
        """ Subtract other point from this point, returning new point vector """
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"P({self.x},{self.y})"

class Vector(Enum):
    """ Enumeration of 8 directions, and a rotating list of direction choices. """
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

        self._directions = deque([ # use a deque so we can rotate
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
        proposals: dict = {} # E.g. {elf point: proposed point}
        for elf_locn in self._elves: # for every existing elf location

            # check if this elf has any immediate neighbours
            if elf_locn.all_neighbours().isdisjoint(self._elves):
                continue # no neighbours are elves; this elf does nothing

            for direction_checks, proposed_direction in self._directions:
                if elf_locn.get_neighbours(direction_checks).isdisjoint(self._elves):
                    proposals[elf_locn] = elf_locn + proposed_direction.value
                    break # exit at the first matching direction

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
        total_tiles = (self._max_x+1-self._min_x) * (self._max_y+1 - self._min_y)
        elf_count = len(self._elves)

        return total_tiles - elf_count

    def __str__(self) -> str:
        lines = []
        for y in range(self._min_y, self._max_y+1):
            line = ""
            for x in range (self._min_x, self._max_x+1):
                line += "#" if Point(x,y) in self._elves else "."

            lines.append(line)

        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Grid(score={self.score})"


def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    # Part 1
    grid = Grid(data)
    current_round = 1
    for _ in range(10):
        grid.iterate()
        current_round += 1

    print(f"Part 1: score={grid.score()}")

    # Part 2
    while grid.iterate() > 0:
        current_round += 1

    print(f"Part 2: Stable at round {current_round}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")