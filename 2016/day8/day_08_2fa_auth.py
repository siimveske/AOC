from collections import deque
import os
import re


def read_input(filename: str) -> list[tuple[str, int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    commands = []
    pattern_rect = r"rect (\d+)x(\d+)"
    pattern_row = r"rotate row y=(\d+) by (\d+)"
    pattern_col = r"rotate column x=(\d+) by (\d+)"

    with open(input_file_path, "r") as f:
        for line in f:
            if match := re.search(pattern_rect, line):
                x, y = match.groups()
                commands.append(("rect", int(x), int(y)))
            elif match := re.search(pattern_row, line):
                y, amount = match.groups()
                commands.append(("row", int(y), int(amount)))
            elif match := re.search(pattern_col, line):
                x, amount = match.groups()
                commands.append(("col", int(x), int(amount)))

    return commands


def rotate_column(matrix: list[list[int]], column: int, amount: int) -> list[list[int]]:
    # Convert the column to a deque for easy rotation
    column_values = deque([row[column] for row in matrix])

    # Rotate the deque
    column_values.rotate(amount)

    # Replace the values in the original matrix
    for i, row in enumerate(matrix):
        row[column] = column_values[i]

    return matrix


def rotate_row(matrix: list[list[int]], row: int, amount: int) -> list[list[int]]:

    new_row = matrix[row][-amount:] + matrix[row][:-amount]
    matrix[row] = new_row

    return matrix


def draw_rectangle(matrix: list[list[int]], width: int, height: int) -> list[list[int]]:
    for i in range(height):
        for j in range(width):
            matrix[i][j] = 1
    return matrix


def part1(filename: str) -> int:
    commands = read_input(filename)
    grid = [[0] * 50 for _ in range(6)]
    for cmd, arg1, arg2 in commands:
        if cmd == "rect":
            grid = draw_rectangle(grid, arg1, arg2)
        elif cmd == "row":
            grid = rotate_row(grid, arg1, arg2)
        elif cmd == "col":
            grid = rotate_column(grid, arg1, arg2)
    return sum(sum(row) for row in grid)


def part2(filename: str) -> int:
    addesses = read_input(filename)


def print_grid(grid):
    for row in grid:
        print(row)


def test():
    print("---- TEST ----")

    print("rect 3x2")
    grid = [[0] * 7 for _ in range(3)]
    grid = draw_rectangle(grid, 3, 2)
    print_grid(grid)

    print("rotate column x=1 by 1")
    grid = rotate_column(grid, 1, 1)
    print_grid(grid)

    print("rotate row y=0 by 4")
    grid = rotate_row(grid, 0, 4)
    print_grid(grid)

    print("rotate column x=1 by 1")
    grid = rotate_column(grid, 1, 1)
    print_grid(grid)

    print("OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 128

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 231


if __name__ == "__main__":
    test()
    main()
