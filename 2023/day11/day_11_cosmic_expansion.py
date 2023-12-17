import os
from itertools import combinations


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        galaxy_map = [[*line] for line in f.read().splitlines()]

    return galaxy_map


def expand(grid) -> list[list[str]]:
    # Create a copy of the original grid
    new_grid = [row.copy() for row in grid]

    # Identify rows and columns that contain only . character
    empty_rows = [i for i, row in enumerate(new_grid) if all(cell == '.' for cell in row)]
    empty_cols = [i for i in range(len(new_grid[0])) if all(row[i] == '.' for row in new_grid)]

    # Double rows that contain only . character
    for idx, i in enumerate(empty_rows):
        new_grid.insert(i + idx, ['.'] * len(new_grid[0]))

    # Double columns that contain only . character
    for idx, i in enumerate(empty_cols):
        for row in new_grid:
            row.insert(i + idx, '.')

    return new_grid


def find_galaxies(galaxy_map) -> list[tuple[int, int]]:
    galaxies = []
    for i, row in enumerate(galaxy_map):
        for j, item in enumerate(row):
            if item == '#':
                galaxies.append((i, j))
    return galaxies


def calculate_distances(galay_combinations) -> list[int]:
    distances = []
    for a, b in galay_combinations:
        ax, ay = a
        bx, by = b
        # Calculate the Manhattan distance
        dist = abs(ax - bx) + abs(ay - by)
        distances.append(dist)
    return distances


def part1(input_file: str) -> int:
    galaxy_map = read_input(input_file)
    expanded_galaxy_map = expand(galaxy_map)
    galaxies = find_galaxies(expanded_galaxy_map)
    galay_combinations = list(combinations(galaxies, 2))
    distances = calculate_distances(galay_combinations)
    return sum(distances)


def part2(input_file: str) -> int:
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 374

    print("Part 1 OK")

    # filename = "test_input2.txt"
    # assert part2(filename) == 8
    #
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 9565386
    # assert solution_part2 == 471


if __name__ == "__main__":
    test()
    main()
