import os
import re


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    robots = set()
    with open(file_path, 'r') as file:
        for line in file:
            numbers = re.findall(r'(-?\d+)', line)
            x, y, vx, vy = [int(i) for i in numbers]
            robots.add((x, y, vx, vy))
    return robots


def part1(input_file: str, width: int, height: int) -> int:
    grid = read_input(input_file)
    for _ in range(100):
        new_grid = set()
        for robot in grid:
            x, y, vx, vy = robot
            new_x = (x + vx) % width
            new_y = (y + vy) % height
            new_grid.add((new_x, new_y, vx, vy))
        grid = new_grid

    mid_x = width // 2
    mid_y = height // 2
    count = [0, 0, 0, 0]
    for robot in grid:
        x, y, vx, vy = robot

        # top left
        if 0 <= x < mid_x and 0 <= y < mid_y:
            count[0] += 1

        # top right
        if mid_x < x < width and 0 <= y < mid_y:
            count[1] += 1

        # bottom left
        if 0 <= x < mid_x and mid_y < y < height:
            count[2] += 1

        # bottom right
        if mid_x < x < width and mid_y < y < height:
            count[3] += 1

    result = 1
    for c in count:
        result *= c
    return result


def part2(input_file: str) -> int:
    data = read_input(input_file)


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename, width=11, height=7) == 12
    print('Part 1 OK')

    # assert part2(filename) == 875318608908
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename, width=101, height=103)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 230686500
    # assert solution_part2 == 102718967795500


if __name__ == '__main__':
    test()
    main()
