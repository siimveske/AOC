from __future__ import annotations
from collections import defaultdict, deque
from dataclasses import dataclass
import os

'''Inspired by: https://github.com/gjanee/advent-of-code-2022/blob/e51e9ccf14399ed451d24bd231b20c2a6fbd0e0c/23.py'''


@dataclass(frozen=True)
class Location:
    '''Contains Row and Column of Elf'''
    row: int
    col: int

    def __add__(self, other: Location) -> Location:
        return Location(self.row + other.row, self.col + other.col)


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    MIN_ROW = MIN_COL = float('inf')
    MAX_ROW = MAX_COL = float('-inf')
    elves = set()

    with open(input_file_path, 'r') as f:
        for r, line in enumerate(f):
            for c, character in enumerate(line):
                if character == '#':
                    elves.add(Location(r, c))
                    MIN_ROW, MIN_COL = min(MIN_ROW, r), min(MIN_COL, c)
                    MAX_ROW, MAX_COL = max(MAX_ROW, r), max(MAX_COL, c)

    return (elves, (MIN_ROW, MAX_ROW, MIN_COL, MAX_COL))


NORTH = [Location(-1, -1), Location(-1,  0), Location(-1,  1)]
SOUTH = [Location( 1, -1), Location( 1,  0), Location( 1,  1)]
WEST  = [Location(-1, -1), Location( 0, -1), Location( 1, -1)]
EAST  = [Location(-1,  1), Location( 0,  1), Location( 1,  1)]
DIRECTIONS = deque([NORTH, SOUTH, WEST, EAST])


def round(elves: set[Location], bbox: tuple):
    MIN_ROW, MAX_ROW, MIN_COL, MAX_COL = bbox
    proposals: dict[Location, list] = defaultdict(lambda:[])

    for elf in elves:
        occupied: list = []
        for direction in DIRECTIONS:
            is_occupied = any(elf+delta in elves for delta in direction)
            occupied.append(is_occupied)

        # We do nothing if no other elf is present or
        # No free location is present
        if True not in occupied or False not in occupied:
            continue

        first_valid_dir = occupied.index(False)
        new_location: Location = elf + DIRECTIONS[first_valid_dir][1]
        proposals[new_location].append(elf)

    for new_location, elf_list in proposals.items():
        if len(elf_list) == 1:
            elves.remove(elf_list[0])
            elves.add(new_location)
            MIN_ROW, MIN_COL = min(MIN_ROW, new_location.row), min(MIN_COL, new_location.col)
            MAX_ROW, MAX_COL = max(MAX_ROW, new_location.row), max(MAX_COL, new_location.col)

    DIRECTIONS.append(DIRECTIONS.popleft()) # move first item to the end of list
    return (elves, (MIN_ROW, MAX_ROW, MIN_COL, MAX_COL))

def part1(inputFile: str):
    elves, bbox = readInput(inputFile)

    for _ in range(10):
        elves, bbox = round(elves, bbox)

    MIN_ROW, MAX_ROW, MIN_COL, MAX_COL = bbox
    area = (MAX_ROW - MIN_ROW + 1) * (MAX_COL - MIN_COL + 1)
    empty_tiles = area - len(elves)
    return empty_tiles

def part2(inputFile: str):
    readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 110
    print('Part 1 OK')

    # assert part2(filename) == 5031
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 3766

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 144012


if __name__ == '__main__':
    test()
    main()
