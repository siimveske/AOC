from collections import defaultdict
import itertools
import os


def read_input(filename: str) -> list[list[str]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    antennas = defaultdict(list)
    rows, cols = 0, 0
    with open(input_path, 'r') as file:
        grid = file.read().splitlines()
        rows, cols = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col != '.':
                    antennas[col].append((i, j))
    return antennas, rows, cols

def part1(input_file: str) -> int:
    graph, rows, cols = read_input(input_file)
    antinodes = set()
    for points in graph.values():
        for p1, p2 in itertools.combinations(points, 2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            antinode_1 = (p1[0]-dx, p1[1]-dy)
            antinode_2 = (p2[0]+dx, p2[1]+dy)
            if 0 <= antinode_1[0] < rows and 0 <= antinode_1[1] < cols:
                antinodes.add(antinode_1)
            if 0 <= antinode_2[0] < rows and 0 <= antinode_2[1] < cols:
                antinodes.add(antinode_2)
    return len(antinodes)

def part2(input_file: str) -> int:
    pass

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 14
    print('Part 1 OK')

    # assert part2(filename) == 6
    # print('Part 2 OK')

def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 4758
    # assert solution_part2 == 1670


if __name__ == '__main__':
    test()
    main()
