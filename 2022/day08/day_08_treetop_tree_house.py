import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, 'r') as f:
        for line in f:
            trees = [int(tree) for tree in line.strip()]
            grid.append(trees)
    return grid


def is_visible(grid: list, row: int, col: int) -> bool:

    tree = grid[row][col]
    visible_from_east = (tree > t for t in grid[row][col + 1:])
    visible_from_west = (tree > t for t in grid[row][:col])
    visible_from_south = (tree > grid[r][col] for r in range(row + 1, len(grid)))
    visible_from_north = (tree > grid[r][col] for r in range(row - 1, -1, -1))

    return all(visible_from_east) or all(visible_from_west) or all(visible_from_south) or all(visible_from_north)


def get_scenic_score(grid: list, row: int, col: int) -> int:

    rows = len(grid)
    cols = len(grid[0])
    tree = grid[row][col]

    for east in range(col + 1, cols):
        if grid[row][east] >= tree:
            break

    for west in range(col - 1, -1, -1):
        if grid[row][west] >= tree:
            break

    for south in range(row + 1, rows):
        if grid[south][col] >= tree:
            break

    for north in range(row - 1, -1, -1):
        if grid[north][col] >= tree:
            break

    east_score = east - col
    west_score = col - west
    south_score = south - row
    nort_score = row - north

    scenic_score = east_score * west_score * south_score * nort_score
    return scenic_score


def part1(inputFile: str) -> int:
    grid = readInput(inputFile)

    # All of the trees around the edge of the grid are visible
    visible = 2 * len(grid)
    visible += 2 * (len(grid[0]) - 2)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if is_visible(grid, row, col):
                visible += 1
    return visible


def part2(inputFile: str) -> int:
    grid = readInput(inputFile)
    height, width = len(grid), len(grid[0])
    maxr, maxc = height - 1, width - 1
    scenic_score = 0
    for row in range(1, maxr):
        for col in range(1, maxc):
            score = get_scenic_score(grid, row, col)
            scenic_score = max(score, scenic_score)
    return scenic_score


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 21
    print('Part 1 OK')

    assert part2(filename) == 8
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 1695
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    assert solution_part2 == 287040
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
