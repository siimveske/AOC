import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, 'r') as f:
        grid = [list(line.strip()) for line in f]

    return grid


def get_movable_positions(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    movable_positions = []
    for r_idx in range(rows):
        for c_idx in range(cols):
            if grid[r_idx][c_idx] != '@':
                continue

            # Count paper rolls in the eight adjacent positions
            neighbours_cnt = 0
            for dr, dc in directions:
                nr, nc = r_idx + dr, c_idx + dc
                if (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == '@'):
                    neighbours_cnt += 1
            if neighbours_cnt < 4:
                movable_positions.append((r_idx, c_idx))

    return movable_positions


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    movable_rolls = get_movable_positions(grid)
    return len(movable_rolls)


def part2(input_file: str) -> int:
    grid = read_input(input_file)
    removable_count = 0

    removable_rolls = get_movable_positions(grid)
    while removable_rolls:
        for r_idx, c_idx in removable_rolls:
            grid[r_idx][c_idx] = '.'
            removable_count += 1
        removable_rolls = get_movable_positions(grid)

    return removable_count


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    assert part2(filename) == 43
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1356
    assert solution_part2 == 8713


if __name__ == '__main__':
    test()
    main()
