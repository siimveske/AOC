from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().strip()


class Point:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Point):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


DIRMAP = {
        '^': Point(0, -1),
        '>': Point(1, 0),
        'v': Point(0, 1),
        '<': Point(-1, 0),
    }


def travel(directions: str) -> dict[Point, int]:
    location = Point(0, 0)
    memo = set([location])
    for d in directions:
        location = location + DIRMAP[d]
        memo.add(location)
    return memo


def travel2(directions: str) -> dict[Point, int]:
    loc1 = Point(0, 0)
    loc2 = Point(0, 0)
    memo = set([loc1])

    for idx, d in enumerate(directions):
        if idx % 2 == 0:
            loc1 = loc1 + DIRMAP[d]
            memo.add(loc1)
        else:
            loc2 = loc2 + DIRMAP[d]
            memo.add(loc2)

    return memo


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    memo = travel(data)
    houses_with_one_present = len(memo)
    return houses_with_one_present


def part2(inputFile: str) -> int:
    data = readInput(inputFile)
    memo = travel2(data)
    houses_with_one_present = len(memo)
    return houses_with_one_present


def test():
    print('---- TEST ----')

    assert len(travel('>')) == 2
    assert len(travel('^>v<')) == 4
    assert len(travel('^v^v^v^v^v')) == 2
    print('Part 1 OK')

    assert len(travel2('^v')) == 3
    assert len(travel2('^>v<')) == 3
    assert len(travel2('^v^v^v^v^v')) == 11
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
