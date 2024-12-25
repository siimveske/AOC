import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            a, b = [int(i) for i in re.findall(r"(\d+)", line)]
            coordinates.append((a, b))

    return coordinates


def simulate(coordinates, rows, cols, steps):
    memory = [["."] * cols for _ in range(rows)]

    for i in range(steps):
        x, y = coordinates[i]
        memory[y][x] = '#'
    return memory


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
    memory = simulate(coordinates, rows, cols, steps)
    result = find_shortest_path(memory)
    for row in memory:
        print("".join(row))
    return result


# def part2(input_file: str) -> int:
#     _, program = read_input(input_file)
#     result = find_quine_input(0, 0, program)
#     return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename, rows=7, cols=7, steps=12) == 22
    print("Part 1 OK")

    # filename = "test_input2.txt"
    # assert part2(filename) == 117440
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename, rows=71, cols=71, steps=1024)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 276
    # assert solution_part2 == 190384113204239


if __name__ == "__main__":
    test()
    main()
