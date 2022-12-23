import os
from collections import deque


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, 'r') as f:
        for line in f:
            row = [character for character in line.strip()]
            grid.append(row)
    return grid


def get_height(grid: list, row: int, col: int) -> int:
    if grid[row][col] == 'S':
        height = ord('a')
    elif grid[row][col] == 'E':
        height = ord('z')
    else:
        height = ord(grid[row][col])
    return height


def get_neighbours(grid: list, row: int, col: int, visited: set) -> list:
    neighbours = []
    rows = len(grid)
    cols = len(grid[0])
    height = get_height(grid, row, col)
    up_down_left_right = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for neighbour in up_down_left_right:
        if neighbour in visited:
            continue

        nrow, ncol = neighbour
        row_inbounds = 0 <= nrow < rows
        col_inbounds = 0 <= ncol < cols
        if not row_inbounds or not col_inbounds:
            continue

        neighbour_height = get_height(grid, nrow, ncol)
        if neighbour_height - height > 1:
            continue

        neighbours.append(neighbour)

    return neighbours


def explore(grid: list, starting_row: int, starting_col: int) -> int:
    visited = set()
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == 'E':
            return distance

        for neighbour in get_neighbours(grid, row, col, visited):
            nrow, ncol = neighbour
            visited.add(neighbour)
            queue.append((nrow, ncol, distance + 1))

    return float('inf')


def get_starting_point(grid: list) -> tuple:
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                return (row, col)


def get_starting_points(grid: list) -> list:
    rows = len(grid)
    cols = len(grid[0])
    starting_points = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S' or grid[row][col] == 'a':
                starting_points.append((row, col))

    return starting_points


def part1(inputFile: str) -> int:
    grid = readInput(inputFile)
    row, col = get_starting_point(grid)
    distance = explore(grid, row, col)
    return distance


def part2(inputFile: str):
    grid = readInput(inputFile)
    starting_points = get_starting_points(grid)
    min_distance = float('inf')
    for row, col in starting_points:
        distance = explore(grid, row, col)
        min_distance = min(min_distance, distance)
    return min_distance


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 31
    print('Part 1 OK')

    assert part2(filename) == 29
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 528
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    # assert solution_part2 == 14106266886
    print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
