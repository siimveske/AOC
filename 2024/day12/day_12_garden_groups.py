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
    """Calculate the perimeter of an island in a garden."""
    perimeter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row, col in island:
        for row_offset, col_offset in directions:
            neighbor_row = row + row_offset
            neighbor_col = col + col_offset
            if (neighbor_row, neighbor_col) not in island:
                perimeter += 1
    return perimeter


def get_discounted_island_perimeter(island: set, garden_grid: list) -> int:
    """Calculate the number of corners of an island."""
    corners = set()
    garden = {(r, c): plant_type for r, row in enumerate(garden_grid) for c, plant_type in enumerate(row)}

    for row, col in island:
        plant_type = garden.get((row, col))

        neighbors = {
            "top": (row - 1, col),
            "top_right": (row - 1, col + 1),
            "right": (row, col + 1),
            "bottom_right": (row + 1, col + 1),
            "bottom": (row + 1, col),
            "bottom_left": (row + 1, col - 1),
            "left": (row, col - 1),
            "top_left": (row - 1, col - 1)
        }

        neighbor_plants = {key: garden.get(pos, '') for key, pos in neighbors.items()}

        # Check for external (convex) corners
        if neighbor_plants["left"] != plant_type and neighbor_plants["top"] != plant_type:
            corners.add((row, col, "top_left"))
        if neighbor_plants["top"] != plant_type and neighbor_plants["right"] != plant_type:
            corners.add((row, col, "top_right"))
        if neighbor_plants["right"] != plant_type and neighbor_plants["bottom"] != plant_type:
            corners.add((row, col, "bottom_right"))
        if neighbor_plants["left"] != plant_type and neighbor_plants["bottom"] != plant_type:
            corners.add((row, col, "bottom_left"))

        # Check for internal (concave) corners
        if neighbor_plants["bottom"] == plant_type and neighbor_plants["right"] == plant_type and neighbor_plants["bottom_right"] != plant_type:
            corners.add((row, col, "bottom_right"))
        if neighbor_plants["bottom"] == plant_type and neighbor_plants["left"] == plant_type and neighbor_plants["bottom_left"] != plant_type:
            corners.add((row, col, "bottom_left"))
        if neighbor_plants["top"] == plant_type and neighbor_plants["left"] == plant_type and neighbor_plants["top_left"] != plant_type:
            corners.add((row, col, "top_left"))
        if neighbor_plants["top"] == plant_type and neighbor_plants["right"] == plant_type and neighbor_plants["top_right"] != plant_type:
            corners.add((row, col, "top_right"))

    return len(corners)


def get_islands(garden_grid):
    visited = set()
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
    return islands


def part1(input_file: str) -> int:
    """Returns the total cost of fencing all of the separate gardens."""

    # Get the garden grid from the input file
    garden_grid = read_input(input_file)
    islands = get_islands(garden_grid)

    # Calculate the total cost of fencing all gardens
    total_cost = 0
    for island in islands:
        area = len(island)
        perimeter = get_island_perimeter(island)
        cost = area * perimeter
        total_cost += cost

    return total_cost


def part2(input_file: str) -> int:

    # Get the garden grid from the input file
    garden_grid = read_input(input_file)
    islands = get_islands(garden_grid)

    # Calculate the total cost of fencing all gardens
    total_cost = 0
    for island in islands:
        area = len(island)
        perimeter = get_discounted_island_perimeter(island, garden_grid)
        cost = area * perimeter
        total_cost += cost

    return total_cost


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 140

    filename = 'test_input2.txt'
    assert part1(filename) == 772

    filename = 'test_input3.txt'
    assert part1(filename) == 1930
    print('Part 1 OK')


    filename = 'test_input.txt'
    assert part2(filename) == 80

    filename = 'test_input2.txt'
    assert part2(filename) == 436

    filename = 'test_input4.txt'
    assert part2(filename) == 236

    filename = 'test_input5.txt'
    assert part2(filename) == 368

    filename = 'test_input3.txt'
    assert part2(filename) == 1206
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1446042
    assert solution_part2 == 902742


if __name__ == '__main__':
    test()
    main()
