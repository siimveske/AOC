import os
import re


def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            a, b = [int(i) for i in re.findall(r"(\d+)", line)]
            coordinates.append((a, b))

    return coordinates


def find_shortest_path(memory: list[list[str]]) -> int:
    """
    Find shortest path from top left grid to bottom right grid.
    """
    rows, cols = len(memory), len(memory[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    seen = [[False] * cols for _ in range(rows)]
    queue = [(0, 0, 0)]  # (x, y, steps)

    while queue:
        x, y, steps = queue.pop(0)

        if x == cols - 1 and y == rows - 1:
            return steps

        if seen[y][x]:
            continue

        seen[y][x] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < cols) and (0 <= ny < rows) and not seen[ny][nx] and memory[ny][nx] != "#":
                queue.append((nx, ny, steps + 1))

    return -1


def part1(input_file: str, rows: int, cols: int, steps: int) -> int:
    coordinates = read_input(input_file)

    grid = [["."] * cols for _ in range(rows)]
    for i in range(steps):
        x, y = coordinates[i]
        grid[y][x] = '#'

    result = find_shortest_path(grid)
    return result


def part2(input_file: str, rows: int, cols: int) -> str:
    coordinates = read_input(input_file)
    grid = [["."] * cols for _ in range(rows)]
    for x, y in coordinates:
        grid[y][x] = "#"
        result = find_shortest_path(grid)
        if result == -1:
            break
    return f"{x},{y}"


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename, rows=7, cols=7, steps=12) == 22
    print("Part 1 OK")

    assert part2(filename, rows=7, cols=7) == "6,1"
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename, rows=71, cols=71, steps=1024)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename, rows=71, cols=71)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 276
    assert solution_part2 == "60,37"


if __name__ == "__main__":
    test()
    main()
