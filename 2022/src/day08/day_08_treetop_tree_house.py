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

    rows = len(grid)
    cols = len(grid[0])
    tree_height = grid[row][col]

    # Test if tree is visible from UP
    idx = row
    while idx > 0:
        if grid[idx - 1][col] >= tree_height:
            break
        idx -= 1
    if idx == 0:
        return True

    # Test if tree is visible from RIGHT
    idx = col
    while idx < (cols - 1):
        if grid[row][idx + 1] >= tree_height:
            break
        idx += 1
    if idx == (cols - 1):
        return True

    # Test if tree is visible from BOTTOM
    idx = row
    while idx < (rows - 1):
        if grid[idx + 1][col] >= tree_height:
            break
        idx += 1
    if idx == (rows - 1):
        return True

    # Test if tree is visible from LEFT
    idx = col
    while idx > 0:
        if grid[row][idx - 1] >= tree_height:
            break
        idx -= 1
    if idx == 0:
        return True

    return False


def get_scenic_score(grid: list, row: int, col: int) -> int:

    rows = len(grid)
    cols = len(grid[0])
    scenic_score = 0
    tree_height = grid[row][col]

    # Test how many trees are visible from UP
    idx = row
    up_score = 0
    while idx > 0:
        if grid[idx - 1][col] >= tree_height:
            up_score += 1
            break
        up_score += 1
        idx -= 1

    # Test how many trees are visible from BOTTOM
    idx = row
    down_score = 0
    while idx < (rows - 1):
        if grid[idx + 1][col] >= tree_height:
            down_score += 1
            break
        down_score += 1
        idx += 1

    # Test how many trees are visible from LEFT
    idx = col
    left_score = 0
    while idx > 0:
        if grid[row][idx - 1] >= tree_height:
            left_score += 1
            break
        left_score += 1
        idx -= 1

    # Test how many trees are visible from RIGHT
    idx = col
    right_score = 0
    while idx < (cols - 1):
        if grid[row][idx + 1] >= tree_height:
            right_score += 1
            break
        right_score += 1
        idx += 1

    scenic_score = up_score * down_score * left_score * right_score
    return scenic_score


def part1(inputFile: str) -> int:
    grid = readInput(inputFile)

    # All of the trees around the edge of the grid are visible
    can_be_seen = 2 * len(grid)
    can_be_seen += 2 * (len(grid[0]) - 2)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if is_visible(grid, row, col):
                can_be_seen += 1
    return can_be_seen


def part2(inputFile: str) -> int:
    grid = readInput(inputFile)

    scenic_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
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
