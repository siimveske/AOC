import os


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        grid = [[*line.strip()] for line in f]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                    break

    return grid, start


def neighbours(location: tuple[int, int], grid: list[list[str]]) -> set:
    r, c = location
    border = len(grid)
    result = set()
    for x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        xr, xc = x
        if (0 <= xr < border) and (0 <= xc < border) and (grid[xr][xc] != '#'):
            result.add(x)
    return result


def neighbour2(location: tuple[int, int], grid: list[list[str]]) -> list:
    r, c = location
    border = len(grid)
    result = []
    for x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        xr, xc = x
        if grid[xr % border][xc % border] != '#':
            result.append(x)
    return result


def part1(input_file: str, steps) -> int:
    grid, start = read_input(input_file)

    locations = {start}
    for i in range(steps):
        new_locations = set()
        while locations:
            location = locations.pop()
            n = neighbours(location, grid)
            new_locations = new_locations.union(n)
        locations = new_locations

    locations.add(start)
    return len(locations)


def part2(input_file: str, steps) -> int:
    grid, start = read_input(input_file)

    use_precalculated = True
    datapoints = dict([(65, 3648), (196, 32781), (327, 90972)])
    if use_precalculated is False:
        datapoints = [(0, 1)]
        locations = {start}
        for i in range(steps):
            new_locations = []
            while locations:
                location = locations.pop()
                n = neighbour2(location, grid)
                new_locations.extend(n)
            locations = set(new_locations)
            datapoints.append((i + 1, len(locations)))
        datapoints = dict(datapoints)

    # Solution from: https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb#scrollTo=KWExJmusNQOK
    one, two, three = [datapoints[65], datapoints[196], datapoints[327]]

    #  coefficients
    c = one
    b = (4 * two - 3 * one - three) // 2
    a = two - one - b

    steps = 26501365
    grid_size = len(grid)
    x = (steps - (grid_size // 2)) // grid_size  # number of whole tile lengths
    result = a * x ** 2 + b * x + c

    return result


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename, steps=6) == 16
    print('Part 1 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename, 64)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename, 327)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 3572
    assert solution_part2 == 594606492802848


if __name__ == '__main__':
    test()
    main()
