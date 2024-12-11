import os

def read_input(filename: str) -> list[list[int]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    grid = []
    with open(input_path, "r") as file:
        data = file.read().splitlines()
        for line in data:
            grid.append(list(map(int, line)))

    return grid


def get_trailheads(grid: list[list[int]]) -> list[int]:
    rows, cols = len(grid), len(grid[0])
    trailheads = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads


def get_neighbors(row: int, col: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    """
    Gets all neighbors of a given point in a grid that are one step higher in elevation.
    """
    neighbors = []
    num_rows, num_cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]

        if (0 <= next_row < num_rows) and (0 <= next_col < num_cols):
            current_elevation = grid[row][col]
            next_elevation = grid[next_row][next_col]

            if next_elevation == current_elevation + 1:
                neighbors.append((next_row, next_col))

    return neighbors


def walk(start, grid, memo):

    if start in memo:
        return memo[start]

    row, col = start
    if grid[row][col] == 9:
        r = set()
        r.add(start)
        return r

    result = set()
    neighbors = get_neighbors(row, col, grid)
    for neighbor in neighbors:
        result.update(walk(neighbor, grid, memo))

    memo[start] = result
    return result


def get_trailhead_score(start, grid):
    destinations = walk(start, grid, {})
    return len(destinations)


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    trailheads = get_trailheads(grid)
    trailhead_scores = []
    for trailhead in trailheads:
        trailhead_scores.append(get_trailhead_score(trailhead, grid))
    return sum(trailhead_scores)

def part2(input_file: str) -> int:
    pass

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 1

    filename = 'test_input2.txt'
    assert part1(filename) == 2

    filename = 'test_input3.txt'
    assert part1(filename) == 4

    filename = 'test_input4.txt'
    assert part1(filename) == 3

    filename = 'test_input5.txt'
    assert part1(filename) == 36

    print('Part 1 OK')

    # assert part2(filename) == 2858
    # print('Part 2 OK')

def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 782
    # assert solution_part2 == 6326952672104


if __name__ == '__main__':
    test()
    main()
