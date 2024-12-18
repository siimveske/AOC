from collections import deque
import os


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = None
    with open(file_path, 'r') as file:
        raw_map, moves = file.read().split("\n\n")

        # parse map
        _map = raw_map.split("\n")
        for r, line in enumerate(_map):
            grid.append(list(line))
            if start:
                continue
            for c, char in enumerate(line):
                if char == "@":
                    start = (r, c)

        # parse moves
        moves_dict = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        cmds = []
        for move in moves:
            if move in moves_dict:
                cmds.append(moves_dict[move])

    return grid, cmds, start


def part1(input_file: str) -> int:
    grid, commands, start_position = read_input(input_file)
    move_queue = deque(commands)

    current_row, current_col = start_position
    while move_queue:
        delta_row, delta_col = move_queue.popleft()
        new_row, new_col = current_row + delta_row, current_col + delta_col

        if grid[new_row][new_col] == "#":
            continue

        if grid[new_row][new_col] == ".":
            grid[new_row][new_col] = "@"
            grid[current_row][current_col] = "."
            current_row, current_col = new_row, new_col
            continue

        obstacle_stack = []
        temp_row, temp_col = new_row, new_col
        while grid[temp_row][temp_col] == "O":
            obstacle_stack.append((temp_row, temp_col))
            temp_row, temp_col = temp_row + delta_row, temp_col + delta_col
        if grid[temp_row][temp_col] == "#":
            continue
        else:
            while obstacle_stack:
                temp_row, temp_col = obstacle_stack.pop()
                grid[temp_row + delta_row][temp_col + delta_col] = "O"
            grid[new_row][new_col] = "@"
            grid[current_row][current_col] = "."
            current_row, current_col = new_row, new_col

    total_score = 0
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "O":
                total_score += 100 * row_index + col_index
    return total_score


# def part2(input_file: str) -> int:
#     configurations = read_input(input_file)

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 2028

    filename = 'test_input2.txt'
    assert part1(filename) == 10092
    print('Part 1 OK')

    # assert part2(filename) == 875318608908
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1517819
    # assert solution_part2 == 102718967795500


if __name__ == '__main__':
    test()
    main()
