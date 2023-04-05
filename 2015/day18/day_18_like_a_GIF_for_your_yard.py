import os


def readInput(filename: str) -> list[list[bool]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        grid = [[1 if char == '#' else 0 for char in line.strip()] for line in f]
    return grid


def part1_solver(grid: list[list[int]], row: int, col: int) -> int:
    neighbours = [
        [row-1, col-1], [row-1, col], [row-1, col+1],
        [row,   col-1],               [row,   col+1],
        [row+1, col-1], [row+1, col], [row+1, col+1],
    ]

    grid_size = len(grid)
    lights_on = sum(grid[r][c] for r,c in neighbours if 0 <= r < grid_size and 0 <= c < grid_size)

    if grid[row][col]:
        return 1 if lights_on in [2,3] else 0
    else:
        return 1 if lights_on == 3 else 0


def part2_solver(grid: list[list[int]], row: int, col: int) -> int:
    edge = len(grid) - 1
    if (row, col) in [(0, 0), (0, edge), (edge, 0), (edge, edge)]:
        return 1
    return part1_solver(grid, row, col)


def evolve(grid: list, solver: callable):
    iterations = 100
    grid_size = len(grid)
    for _ in range(iterations):
        grid = [[solver(grid, row, col) for col in range(grid_size)] for row in range(grid_size)]
    return grid


def part1(grid: list[list[int]]) -> int:
    grid = evolve(grid, part1_solver)
    return sum(sum(grid, []))


def part2(grid: list[list[int]]) -> int:
    # initialize four always ON corners
    grid_size = len(grid) - 1
    grid[0][0] = grid[0][grid_size] = grid[grid_size][0] = grid[grid_size][grid_size] = 1

    grid = evolve(grid, part2_solver)
    return sum(sum(grid, []))

def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 814

    solution_part2 = part2(data)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 924


if __name__ == "__main__":
    main()
