import os
import sys

sys.setrecursionlimit(5000)


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        grid = f.read().splitlines()
    return grid


def walk(pos, end, grid, size, visited, memo):
    row, col = pos

    if pos == end:
        return 0
    if pos in visited:
        return 0
    if pos in memo:
        return memo[pos]

    visited.add(pos)

    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    next_locations = []
    if up > 0:
        if grid[up][col] in '.^':
            next_locations.append((up, col))
    if down < size:
        if grid[down][col] in '.v':
            next_locations.append((down, col))
    if left > 0:
        if grid[row][left] in '.<':
            next_locations.append((row, left))
    if right < size:
        if grid[row][right] in '.>':
            next_locations.append((row, right))

    distances = [1 + walk(loc, end, grid, size, set(visited), memo) for loc in next_locations]

    max_distance = max(distances)
    memo[pos] = max_distance

    return max_distance


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    size = len(grid)
    start = (0, 1)
    end = (size - 1, size - 2)
    visited = set()
    memo = {}
    result = walk(start, end, grid, size, visited, memo)
    return result


def part2(input_file: str) -> int:
    lines = read_input(input_file)


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'

    assert part1(filename) == 94
    print('Part 1 OK')

    # assert part2(filename) == 7
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 2154
    # assert solution_part2 == 67468


if __name__ == '__main__':
    test()
    main()
