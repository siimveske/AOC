from functools import lru_cache
import os

WALL, FREE, EMPTY = '#. '
RIGHT, DOWN, LEFT, UP = range(4)

DIRMAP = [
    (0, 1),  # moving right
    (1, 0),  # moving down
    (0, -1),  # moving left
    (-1, 0),  # moving up
]

grid = []
moves = []
HEIGHT, WIDTH = 0, 0


def readInput(filename: str):
    global grid, moves, HEIGHT, WIDTH

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        grid = f.read().splitlines()

    moves = grid[-1]  # Take last line with movement instructions.
    grid = grid[:-2]  # Throw away last two lines.

    # Make the map square and
    # Add two empty columns left and right.
    HEIGHT, WIDTH = len(grid), max(map(len, grid))
    for i in range(HEIGHT):
        grid[i] = EMPTY + grid[i].ljust(WIDTH, EMPTY) + EMPTY

    HEIGHT += 2
    WIDTH += 2

    # Add two empty rows at the top and at the bottom.
    grid = [EMPTY * WIDTH] + grid + [EMPTY * WIDTH]

    moves = moves.replace('R', ' R ').replace('L', ' L ').split()
    moves = tuple(map(lambda m: m if m in 'LR' else int(m), moves))


@lru_cache()
def leftmost_col(r):
    # Scan from left to right
    return next(c for c in range(WIDTH) if grid[r][c] != EMPTY)


@lru_cache()
def rightmost_col(r):
    # Scan from right to left
    return next(c for c in range(WIDTH - 1, -1, -1) if grid[r][c] != EMPTY)


@lru_cache()
def upmost_row(c):
    # Scan from top to bottom
    return next(r for r in range(HEIGHT) if grid[r][c] != EMPTY)


@lru_cache()
def downmost_row(c):
    # Scan from bottom to top
    return next(r for r in range(HEIGHT - 1, -1, -1) if grid[r][c] != EMPTY)


def step(r, c, direction):
    dr, dc = DIRMAP[direction]
    r += dr
    c += dc

    if grid[r][c] == EMPTY:
        # We fell off the edge of the grid, we need to wrap to the opposite side.
        if direction == RIGHT:
            c = leftmost_col(r)
        elif direction == LEFT:
            c = rightmost_col(r)
        elif direction == DOWN:
            r = upmost_row(c)
        elif direction == UP:
            r = downmost_row(c)

    return r, c


def walk(grid, moves):
    r = 1
    c = grid[1].index(FREE)  # Find The cell to start from
    d = RIGHT

    for move in moves:
        if move == 'L':
            d = (d - 1) % 4
        elif move == 'R':
            d = (d + 1) % 4
        else:
            for _ in range(move):
                newr, newc = step(r, c, d)

                # Stop if we hit a wall.
                if grid[newr][newc] == WALL:
                    break

                # Otherwise just keep going.
                r, c = newr, newc

    return r, c, d


def part1(inputFile: str):
    readInput(inputFile)
    row, col, direction = walk(grid, moves)
    return 1000 * row + 4 * col + direction


def part2(inputFile: str):
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 6032
    print('Part 1 OK')

    # assert part2(filename) == 301
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 76332

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 3715799488132


if __name__ == '__main__':
    test()
    main()
