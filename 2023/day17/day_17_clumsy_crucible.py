import os
import sys
sys.setrecursionlimit(100000)


def read_input(filename: str) -> list[list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return [[int(value) for value in line] for line in f.read().splitlines()]


def calculate(pos, end, grid, memo, cnt, visited, coming_from):
    row, col = pos
    max_row, max_col = end
    up_row = row - 1
    down_row = row + 1
    left_col = col - 1
    right_col = col + 1
    u, d, l, r = cnt

    if pos in memo:
        return memo[pos]
    if pos == end:
        return grid[max_row][max_col]
    if pos in visited:
        return float('inf')
    if any([i > 3 for i in [u, d, l, r]]):
        return float('inf')

    if pos == (0, 0) and coming_from == (-1, -1):
        result = 0
    else:
        visited.add(pos)
        result = grid[row][col]

    min_udlr = float('inf')
    if coming_from != (up_row, col) and up_row >= 0:
        min_udlr = min(min_udlr, calculate((up_row, col), end, grid, memo, (u + 1, 0, 0, 0), visited, pos))
    if coming_from != (down_row, col) and down_row <= max_row:
        min_udlr = min(min_udlr, calculate((down_row, col), end, grid, memo, (0, d + 1, 0, 0), visited, pos))
    if coming_from != (row, left_col) and left_col >= 0:
        min_udlr = min(min_udlr, calculate((row, left_col), end, grid, memo, (0, 0, l + 1, 0), visited, pos))
    if coming_from != (row, right_col) and right_col <= max_col:
        min_udlr = min(min_udlr, calculate((row, right_col), end, grid, memo, (0, 0, 0, r + 1), visited, pos))

    memo[pos] = result + min_udlr

    return memo[pos]


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    result = calculate((0, 0), (rows, cols), grid, {}, (0, 0, 0, 0), set(), (-1,-1))
    return result


def part2(input_file: str) -> int:
    grid = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 102
    print('Part 1 OK')

    # assert part2(filename) == 51
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    #
    # assert solution_part1 == 7996
    # assert solution_part2 == 8239


if __name__ == '__main__':
    test()
    main()
