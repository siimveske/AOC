import itertools
import os
import re
from matplotlib import pyplot as plt


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    robots = {}
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file.read().splitlines()):
            numbers = re.findall(r'(-?\d+)', line)
            x, y, vx, vy = [int(i) for i in numbers]
            robots[idx] = (x, y, vx, vy)
    return robots

def explore(location, locations, visited):

    visited.add(location)
    directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    row, col = location
    size = 1

    for dx, dy in directions:
        new_location = (row + dx, col + dy)
        if new_location in locations and new_location not in visited:
            size += explore(new_location, locations, visited)

    return size


def maximum_island(grid):
    """Return the size of the biggest island"""

    locations = set()
    for robot in grid.values():
        x, y, vx, vy = robot
        locations.add((x, y))

    result = 0
    visited = set()

    for location in locations:
        if location in visited:
            continue
        island_size = explore(location, locations, visited)
        result = max(result, island_size)

    return result


def part1(input_file: str, width: int, height: int) -> int:
    grid = read_input(input_file)
    for _ in range(100):
        for idx, robot in grid.items():
            x, y, vx, vy = robot
            new_x = (x + vx) % width
            new_y = (y + vy) % height
            grid[idx] = (new_x, new_y, vx, vy)

    mid_x = width // 2
    mid_y = height // 2
    count = [0, 0, 0, 0]
    for robot in grid.values():
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


def part2(input_file: str, width: int, height: int):
    grid = read_input(input_file)
    num_of_robots = len(grid)
    max_num_of_connected_robots = num_of_robots // 8

    plt.xlim(0, width)
    plt.ylim(0, height)

    for i in itertools.count(1):
        for idx, robot in grid.items():
            x, y, vx, vy = robot
            new_x = (x + vx) % width
            new_y = (y + vy) % height
            grid[idx] = (new_x, new_y, vx, vy)

        connected = maximum_island(grid)

        if connected >= max_num_of_connected_robots:
            max_num_of_connected_robots = connected
            print(f'Step {i}: Max connected:{max_num_of_connected_robots}')

            plt.clf()
            plt.title(f'Step {i}')
            img = [[0] * width for _ in range(height)]
            for robot in grid.values():
                x, y, vx, vy = robot
                img[y][x] = 255
            plt.imshow(img)
            plt.show()



def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename, width=11, height=7) == 12
    print('Part 1 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename, width=101, height=103)
    print(f'Solution for Part 1: {solution_part1}')

    part2(filename, width=101, height=103)

    assert solution_part1 == 230686500


if __name__ == '__main__':
    test()
    main()
