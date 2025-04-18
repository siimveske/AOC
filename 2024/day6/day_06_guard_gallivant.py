import os


def read_input(filename: str) -> list[list[str]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    grid = []
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            grid.append([*line.strip()])
    return grid

def inbound(point: tuple[int, int], rows: int, cols: int) -> bool:
    return 0 <= point[0] < rows and 0 <= point[1] < cols

def find_guard_location(grid: list[str]) -> tuple[int, int]:
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                return (i, j)

DIRECTIONS = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1)   # left
    ]

def move_guard(grid: list[list[str]], guard: tuple[int, int]) -> set[tuple[int, int]]:

    # setup variables to move and track guard
    rows, cols = len(grid), len(grid[0])
    visited = set()
    visited.add(guard)
    current_direction = 0

    # move guard
    while True:
        new_row = guard[0] + DIRECTIONS[current_direction][0]
        new_col = guard[1] + DIRECTIONS[current_direction][1]

        if not inbound((new_row, new_col), rows, cols):
            break

        if grid[new_row][new_col] == '#':
            current_direction = (current_direction + 1) % 4
        else:
            guard = (new_row, new_col)
            visited.add(guard)

    return visited

def part1(input_file: str) -> int:
    grid = read_input(input_file)
    guard = find_guard_location(grid)
    visited = move_guard(grid, guard)
    return len(visited)


def part2(input_file: str) -> int:
    grid = read_input(input_file)
    rows, cols = len(grid), len(grid[0])

    # Find start position of guard
    guard_start = find_guard_location(grid)

    # Initialize variables
    loop_count = 0
    path = move_guard(grid, guard_start)

    # Iterate over all points in the guard path
    for i, j in path:

        # Save grid value @ (i, j) and replace with '#'
        original_value = grid[i][j]
        grid[i][j] = '#'

        # Initialize variables to move and track guard
        guard = guard_start
        current_direction = 0
        visited = set()
        visited.add((current_direction, guard))

        # Move guard
        while True:
            new_row = guard[0] + DIRECTIONS[current_direction][0]
            new_col = guard[1] + DIRECTIONS[current_direction][1]

            if not inbound((new_row, new_col), rows, cols):
                break
            if (current_direction, (new_row, new_col)) in visited:
                loop_count += 1
                break
            if grid[new_row][new_col] == '#':
                current_direction = (current_direction + 1) % 4
            else:
                guard = (new_row, new_col)
                visited.add((current_direction, guard))

        # Restore original value
        grid[i][j] = original_value

    return loop_count


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 41
    print('Part 1 OK')

    assert part2(filename) == 6
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 4758
    assert solution_part2 == 1670


if __name__ == '__main__':
    test()
    main()
