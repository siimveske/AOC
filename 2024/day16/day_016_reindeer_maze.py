import os
import sys
sys.setrecursionlimit(10**6)

def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = None
    with open(file_path, "r") as file:
        grid = file.read().splitlines()
        for r, row in enumerate(grid):
            if start:
                break
            for c, char in enumerate(row):
                if char == "S":
                    start = (r, c)
                    break

    return grid, start


def rotate(vector, steps: int) -> tuple:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index = directions.index(vector)
    rotated_index = (index + steps) % len(directions)
    return directions[rotated_index]


def calculate(grid, start, direction, cost, visited):
    r, c = start
    dr, dc = direction

    if grid[r][c] == "E":
        return cost

    if grid[r][c] == "#" or start in visited:
        return float("inf")

    # Move forward
    if start == (7, 3) and direction == (-1, 0):
        pass
    next_cell = (r + dr, c + dc)
    min_cost = calculate(grid, next_cell, direction, cost + 1, visited | {(start)})

    # Rotate 90 degrees left
    next_direction = rotate(direction, -1)
    next_cell = (r + next_direction[0], c + next_direction[1])
    min_cost = min(min_cost, calculate(grid, next_cell, next_direction, cost + 1000 + 1, visited | {start}))

    # Rotate 90 degrees right
    next_direction = rotate(direction, 1)
    next_cell = (r + next_direction[0], c + next_direction[1])
    min_cost = min(min_cost, calculate(grid, next_cell, next_direction, cost + 1000 + 1, visited | {start}))

    # Rotate 180 degrees
    next_direction = rotate(direction, 2)
    next_cell = (r + next_direction[0], c + next_direction[1])
    min_cost = min(min_cost, calculate(grid, next_cell, next_direction, cost + 2000 + 1, visited | {start}))

    return min_cost


def part1(input_file: str) -> int:
    grid, start = read_input(input_file)
    direction = (0, 1)
    result = calculate(grid, start, direction, 0, set())
    return result


# def part2(input_file: str) -> int:
#     grid, commands, start_position = read_input(input_file)
#     pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 7036

    filename = "test_input2.txt"
    assert part1(filename) == 11048

    print("Part 1 OK")

    # assert part2(filename) == 618
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    # assert solution_part1 == 1517819
    # assert solution_part2 == 1538862


if __name__ == "__main__":
    test()
    main()
