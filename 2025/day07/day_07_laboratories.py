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
    start = (0, grid[0].index("S"))

    queue = deque()
    queue.append(start)
    path_cnt = 0
    rows = len(grid)

    while queue:
        current = queue.popleft()

        current_row, current_col = current
        nxt_row = current_row + 1

        in_bounds = 0 <= nxt_row < rows
        if not in_bounds:
            path_cnt += 1
            continue

        if grid[nxt_row][current_col] == ".":
            queue.append((nxt_row, current_col))
            continue

        if grid[nxt_row][current_col] == "^":
            nxt_left = (nxt_row, current_col - 1)
            nxt_right = (nxt_row, current_col + 1)
            queue.append(nxt_left)
            queue.append(nxt_right)

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
    # assert solution_part2 == 7329921182115


if __name__ == "__main__":
    test()
    main()
