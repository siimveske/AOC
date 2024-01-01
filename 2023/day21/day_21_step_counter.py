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


def neigbours(location: tuple[int, int], grid: list[list[str]]) -> set:
    r, c = location
    border = len(grid)
    result = set()
    for x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        xr, xc = x
        if (0 <= xr < border) and (0 <= xc < border) and (grid[xr][xc] == '.'):
            result.add(x)
    return result


def part1(input_file: str, steps) -> int:
    grid, start = read_input(input_file)

    locations = {start}
    for i in range(steps):
        new_locations = set()
        while locations:
            location = locations.pop()
            n = neigbours(location, grid)
            new_locations = new_locations.union(n)
        locations = new_locations

    locations.add(start)
    return len(locations)


def part2(input_file: str) -> int:
    graph = read_input(input_file)


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

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 3572
    # assert solution_part2 == 238420328103151


if __name__ == '__main__':
    test()
    main()
