import os


def readInput(filename: str) -> list[list[bool]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, "r") as f:
        for  line in f:
            grid.append([1 if i=='#' else 0 for i in line.strip()])
    return grid


def part1_solver(grid: list[list[int]], row: int, col: int) -> int:
    neighbours = [
        [row-1, col],
        [row-1, col+1],
        [row, col+1],
        [row+1, col+1],
        [row+1, col],
        [row+1, col-1],
        [row, col-1],
        [row-1, col-1]
    ]

    lights_on = 0
    rows=cols=len(grid)
    for r,c in neighbours:
        if 0 <= r < rows and 0 <= c < cols:
            lights_on += grid[r][c]

    if grid[row][col]:
        return 1 if lights_on in [2,3] else 0
    else:
        return 1 if lights_on == 3 else 0


def part2_solver(grid: list[list[int]], row: int, col: int) -> int:
    rows = cols = len(grid) - 1
    if (row, col) in [(0, 0), (0, cols), (rows, 0), (rows, cols)]:
        return 1
    return part1_solver(grid, row, col)


def evolve(grid: list, solver: callable):
    steps = 100
    rows=cols=len(grid)
    for _ in range(steps):
        new_grid = []
        for row in range(rows):
            new_row = []
            for col in range(cols):
                item = solver(grid, row, col)
                new_row.append(item)
            new_grid.append(new_row)
        grid = new_grid
    return grid


def part1(grid: list[list[int]]) -> int:
    grid = evolve(grid, part1_solver)
    result = 0
    for row in grid:
        for col in row:
            result += col
    return result


def part2(grid: list[list[int]]) -> int:
    grid[0][0] = grid[0][99] = grid[99][0] = grid[99][99] = 1 # initialize four corners
    grid = evolve(grid, part2_solver)
    result = 0
    for row in grid:
        for col in row:
            result += col
    return result

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
