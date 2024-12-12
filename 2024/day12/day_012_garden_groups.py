import os


def read_input(filename: str) -> tuple[list[int], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        grid = f.read().splitlines()
    return grid

def explore(grid, row, col, plant_type, plots, visited):
    row_inbound = 0 <= row < len(grid)
    col_inboud = 0 <= col < len(grid[0])

    if not row_inbound or not col_inboud:
        return 0
    if grid[row][col] != plant_type:
        return 0
    if (row, col) in visited:
        return 0

    visited.add((row, col))
    plots.add((row, col))

    explore(grid, row - 1, col, plant_type, plots, visited)
    explore(grid, row + 1, col, plant_type, plots, visited)
    explore(grid, row, col - 1, plant_type, plots, visited)
    explore(grid, row, col + 1, plant_type, plots, visited)

    return plots


def get_island_perimeter(island: set) -> int:
    perimeter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row, col in island:
        for i, j in directions:
            new_row = row + i
            new_col = col + j
            if (new_row, new_col) not in island:
                perimeter += 1
    return perimeter


def part1(input_file: str) -> int:
    """Returns the total cost of fencing all of the separate gardens."""

    # Get the garden grid from the input file
    garden_grid = read_input(input_file)

    # Initialize variables
    visited = set()
    total_cost = 0
    islands = []

    # Iterate over all positions in the garden grid
    for row, line in enumerate(garden_grid):
        for col, plant_type in enumerate(line):
            # Check if the current position is a new island
            if (row, col) not in visited:
                island_plots = set()
                island_plots = explore(garden_grid, row, col, plant_type, island_plots, visited)
                if island_plots:
                    islands.append(island_plots)

    # Calculate the total cost of fencing all of the separate gardens
    for island in islands:
        area = len(island)
        perimeter = get_island_perimeter(island)
        cost = area * perimeter
        total_cost += cost

    return total_cost

# def part2(input_file: str) -> int:
#     pass

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 140

    filename = 'test_input2.txt'
    assert part1(filename) == 772

    filename = 'test_input3.txt'
    assert part1(filename) == 1930

    print('Part 1 OK')

    # assert part2(filename) == 31
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1446042
    # assert solution_part2 == 20520794


if __name__ == '__main__':
    test()
    main()
