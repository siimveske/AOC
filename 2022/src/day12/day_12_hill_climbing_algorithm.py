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


def explore(grid: list, starting_row: int, starting_col: int) -> int:
    visited = set()
    queue = deque([(starting_row, starting_col, 0, ord('a'))])

    while queue:
        row, col, distance, height = queue.popleft()

        row_inbounds = 0 <= row < len(grid)
        col_inbounds = 0 <= col < len(grid[0])

        if (row, col) in visited:
            continue
        if not row_inbounds or not col_inbounds:
            continue

        if grid[row][col] == 'S':
            current_height = ord('a')
        elif grid[row][col] == 'E':
            current_height = ord('z')
        else:
            current_height = ord(grid[row][col])
        if abs(current_height - height) > 1:
            continue

        if grid[row][col] == "E":
            return distance

        visited.add((row, col))

        queue.append((row + 1, col, distance + 1, current_height))
        queue.append((row - 1, col, distance + 1, current_height))
        queue.append((row, col + 1, distance + 1, current_height))
        queue.append((row, col - 1, distance + 1, current_height))

    return -1


def get_starting_point(grid: list) -> tuple:
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                return (row, col)


def part1(inputFile: str) -> int:
    grid = readInput(inputFile)
    row, col = get_starting_point(grid)
    distance = explore(grid, row, col)
    return distance


def part2(inputFile: str):
    monkeys = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 31
    print('Part 1 OK')

    # assert part2(filename) == 2713310158
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    # assert solution_part1 == 57348
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 14106266886
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
