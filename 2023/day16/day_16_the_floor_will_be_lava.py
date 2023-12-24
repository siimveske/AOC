import collections
import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


directions = {
    'right': (0, -1),
    'left': (0, 1),
    'up': (1, 0),
    'down': (-1, 0)
}


def solve(grid, start) -> int:
    grid_size = len(grid)
    visited = set()
    tiles = set()
    queue = collections.deque([start])
    while queue:
        node = queue.popleft()
        current_r, current_c, coming_from = node

        row_in_bound = 0 <= current_r < grid_size
        col_in_bound = 0 <= current_c < grid_size

        if not row_in_bound or not col_in_bound or node in visited:
            continue

        # Mark current node as visited
        visited.add(node)
        tiles.add((current_r, current_c))
        grid_item = grid[current_r][current_c]

        # Continue existing direction
        if (grid_item == '.') or \
           (grid_item == '|' and coming_from in ['up', 'down']) or \
           (grid_item == '-' and coming_from in ['left', 'right']):

            # Calculate next grid position
            next_r = current_r + directions[coming_from][0]
            next_c = current_c + directions[coming_from][1]

            queue.append((next_r, next_c, coming_from))

        # Split to up and down
        elif grid_item == '|':
            queue.append((current_r - 1, current_c, 'down'))
            queue.append((current_r + 1, current_c, 'up'))

        # Split to left and right
        elif grid_item == '-':
            queue.append((current_r, current_c - 1, 'right'))
            queue.append((current_r, current_c + 1, 'left'))

        # Reflect 90 deg
        elif grid_item == '\\':
            if coming_from == 'left':
                queue.append((current_r + 1, current_c, 'up'))      # left -> down
            elif coming_from == 'down':
                queue.append((current_r, current_c - 1, 'right'))   # down -> left
            elif coming_from == 'up':
                queue.append((current_r, current_c + 1, 'left'))    # up -> right
            elif coming_from == 'right':
                queue.append((current_r - 1, current_c, 'down'))    # right -> up

        # Reflect 90 deg
        elif grid_item == '/':
            if coming_from == 'left':
                queue.append((current_r - 1, current_c, 'down'))    # left -> up
            elif coming_from == 'down':
                queue.append((current_r, current_c + 1, 'left'))    # down -> right
            elif coming_from == 'up':
                queue.append((current_r, current_c - 1, 'right'))   # up -> left
            elif coming_from == 'right':
                queue.append((current_r + 1, current_c, 'up'))      # right -> down

    return len(tiles)


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    start = (0, 0, 'left')
    result = solve(grid, start)
    return result


def part2(input_file: str) -> int:
    grid = read_input(input_file)
    grid_size = len(grid)
    solutions = []
    for i in range(grid_size):
        left_start = (i, 0, 'left')
        solutions.append(solve(grid, left_start))

        right_start = (i, grid_size - 1, 'right')
        solutions.append(solve(grid, right_start))

        up_start = (0, i, 'up')
        solutions.append(solve(grid, up_start))

        down_start = (grid_size - 1, i, 'down')
        solutions.append(solve(grid, down_start))

    result = max(solutions)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 46
    print('Part 1 OK')

    assert part2(filename) == 51
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 7996
    assert solution_part2 == 8239


if __name__ == '__main__':
    test()
    main()
