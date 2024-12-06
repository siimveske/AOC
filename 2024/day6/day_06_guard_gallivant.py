import os


def read_input(filename: str) -> list[str]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    with open(input_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def inbound(point: tuple[int, int], rows: int, cols: int) -> bool:
    return 0 <= point[0] < rows and 0 <= point[1] < cols

def part1(input_file: str) -> int:
    grid = read_input(input_file)
    rows = len(grid)
    cols = len(grid[0])

    # find guard location
    guard = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                guard = (i, j)
                break

    # setup variables to move and track guard
    visited = set()
    visited.add(guard)
    current_direction = 0
    directions = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1)   # left
    ]

    # move guard
    while True:
        new_row = guard[0] + directions[current_direction][0]
        new_col = guard[1] + directions[current_direction][1]

        if not inbound((new_row, new_col), rows, cols):
            break

        if grid[new_row][new_col] == '#':
            current_direction = (current_direction + 1) % 4
        else:
            guard = (new_row, new_col)
            visited.add(guard)

    return len(visited)


def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 41
    print('Part 1 OK')

    # assert part2(filename) == 123
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 4814
    # assert solution_part2 == 5448


if __name__ == '__main__':
    test()
    main()
