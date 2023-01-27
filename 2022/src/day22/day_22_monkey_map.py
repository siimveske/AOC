from functools import lru_cache
import os

'''https://github.com/mebeim/aoc/tree/master/2022#day-22---monkey-map'''


WALL, FREE, EMPTY = '#. '
RIGHT, DOWN, LEFT, UP = range(4)

DIRMAP = [
    (0, 1),  # moving right
    (1, 0),  # moving down
    (0, -1),  # moving left
    (-1, 0),  # moving up
]

FACES = (
    # rmin, rmax, cmin, cmax
    (1, 50, 51, 100),
    (1, 50, 101, 150),
    (51, 100, 51, 100),
    (101, 150, 1, 50),
    (101, 150, 51, 100),
    (151, 200, 1, 50)
)

GRID = []
MOVES = []
HEIGHT, WIDTH = 0, 0


def readInput(filename: str):
    global GRID, MOVES, HEIGHT, WIDTH

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        GRID = f.read().splitlines()

    MOVES = GRID[-1]  # Take last line with movement instructions.
    GRID = GRID[:-2]  # Throw away last two lines.

    # Make the map square and
    # Add two empty columns left and right.
    HEIGHT, WIDTH = len(GRID), max(map(len, GRID))
    for i in range(HEIGHT):
        GRID[i] = EMPTY + GRID[i].ljust(WIDTH, EMPTY) + EMPTY

    HEIGHT += 2
    WIDTH += 2

    # Add two empty rows at the top and at the bottom.
    GRID = [EMPTY * WIDTH] + GRID + [EMPTY * WIDTH]

    MOVES = MOVES.replace('R', ' R ').replace('L', ' L ').split()
    MOVES = tuple(map(lambda m: m if m in 'LR' else int(m), MOVES))


@lru_cache()
def leftmost_col(r):
    # Scan from left to right
    return next(c for c in range(WIDTH) if GRID[r][c] != EMPTY)


@lru_cache()
def rightmost_col(r):
    # Scan from right to left
    return next(c for c in range(WIDTH - 1, -1, -1) if GRID[r][c] != EMPTY)


@lru_cache()
def top_row(c):
    # Scan from top to bottom
    return next(r for r in range(HEIGHT) if GRID[r][c] != EMPTY)


@lru_cache()
def bottom_row(c):
    # Scan from bottom to top
    return next(r for r in range(HEIGHT - 1, -1, -1) if GRID[r][c] != EMPTY)


def step_grid(r, c, direction):
    dr, dc = DIRMAP[direction]
    r += dr
    c += dc

    if GRID[r][c] == EMPTY:
        # We fell off the edge of the grid, we need to wrap to the opposite side.
        if direction == RIGHT:
            c = leftmost_col(r)
        elif direction == LEFT:
            c = rightmost_col(r)
        elif direction == DOWN:
            r = top_row(c)
        elif direction == UP:
            r = bottom_row(c)

    return r, c, direction


def face(r, c):
    for face_id, (rmin, rmax, cmin, cmax) in enumerate(FACES, 1):
        if rmin <= r <= rmax and cmin <= c <= cmax:
            return face_id, r - rmin + 1, c - cmin + 1


def step_cube(r, c, direction):
    dr, dc = DIRMAP[direction]
    newr = r + dr
    newc = c + dc

    if GRID[newr][newc] != EMPTY:
        return newr, newc, direction

    face_id, fr, fc = face(r, c)

    if face_id == 1:
        if direction == UP:         # face 6 going right
            return fc + 150, 1, RIGHT
        # direction == LEFT        -> face 4 going right
        return (51 - fr) + 100, 1, RIGHT

    if face_id == 2:
        if direction == UP:         # face 6 going up
            return 200, fc, UP
        if direction == DOWN:       # face 3 going left
            return fc + 50, 100, LEFT
        # direction == RIGHT       -> face 5 going left
        return (51 - fr) + 100, 100, LEFT

    if face_id == 3:
        if direction == LEFT:       # face 4 going down
            return 101, fr, DOWN
        # direction == RIGHT       -> face 2 going up
        return 50, fr + 100, UP

    if face_id == 4:
        if direction == UP:         # face 3 going right
            return fc + 50, 51, RIGHT
        # direction == LEFT        -> face 1 going right
        return (51 - fr), 51, RIGHT

    if face_id == 5:
        if direction == RIGHT:      # face 2 going left
            return (51 - fr), 150, LEFT
        # direction == DOWN        -> face 6 going left
        return fc + 150, 50, LEFT

    # face_id == 6
    if direction == LEFT:           # face 1 going down
        return 1, fr + 50, DOWN
    if direction == RIGHT:          # face 5 going up
        return 150, fr + 50, UP
    else:  # direction == DOWN      -> face 2 going down
        return 1, fc + 100, DOWN


def walk(grid, moves, step_func=step_grid):
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
                newr, newc, newd = step_func(r, c, d)

                # Stop if we hit a wall.
                if grid[newr][newc] == WALL:
                    break

                # Otherwise just keep going.
                r, c, d = newr, newc, newd

    return 1000 * r + 4 * c + d


def part1(inputFile: str):
    readInput(inputFile)
    answer = walk(GRID, MOVES)
    return answer


def part2(inputFile: str):
    readInput(inputFile)
    answer = walk(GRID, MOVES, step_cube)
    return answer


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 6032
    print('Part 1 OK')

    # assert part2(filename) == 5031
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 76332

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 144012


if __name__ == '__main__':
    test()
    main()
