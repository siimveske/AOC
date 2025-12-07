from collections import deque
import os


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, "r") as f:
        for line in f.read().splitlines():
            grid.append(list(line))

    return grid


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    start = (0, grid[0].index("S"))

    queue = deque()
    queue.append(start)
    split_cnt = 0
    rows = len(grid)
    visited = set()

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        current_row, current_col = current
        nxt_row = current_row + 1

        in_bounds = 0 <= nxt_row < rows
        if not in_bounds:
            continue

        if grid[nxt_row][current_col] == ".":
            queue.append((nxt_row, current_col))
            continue

        if grid[nxt_row][current_col] == "^":
            split_cnt += 1
            nxt_left = (nxt_row, current_col - 1)
            nxt_right = (nxt_row, current_col + 1)
            queue.append(nxt_left)
            queue.append(nxt_right)

    return split_cnt


def part2(input_file: str) -> int:
    grid = read_input(input_file)
    rows = len(grid)
    start = (0, grid[0].index("S"))
    memo = {}

    def count_paths(r, c):
        # # Base case: If we are at the last row, we have found one complete path.
        if r >= rows - 1:
            return 1

        # If we've already computed paths from this cell, return the stored value.
        if (r, c) in memo:
            return memo[(r, c)]

        # Recursive step:
        # If the cell below is a splitter '^', the number of paths is the sum
        # of paths from the two resulting positions (left and right).
        # Otherwise, it's the number of paths from the cell directly below.
        if grid[r + 1][c] == '^':
            result = count_paths(r + 1, c - 1) + count_paths(r + 1, c + 1)
        else:  # This will be '.'
            result = count_paths(r + 1, c)

        memo[(r, c)] = result
        return result

    path_cnt = count_paths(start[0], start[1])
    return path_cnt


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == 21
    print("Part 1 OK")

    assert part2(filename) == 40
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 1633
    assert solution_part2 == 34339203133559


if __name__ == "__main__":
    test()
    main()
