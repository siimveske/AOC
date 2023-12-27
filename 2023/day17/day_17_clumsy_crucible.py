import collections
import heapq
import math
import os


def read_input(filename: str) -> tuple[dict[tuple[int, int], int], tuple[int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = {}
    with open(input_file_path, 'r') as f:
        lines = f.read().splitlines()
        for idx_r, row in enumerate(lines):
            for idx_c, value in enumerate(row):
                grid[(idx_r, idx_c)] = int(value)

    rows = len(lines)
    cols = len(lines[0])

    return grid, (rows - 1, cols - 1)


def get_neighbors(node: tuple[tuple[int, int], tuple[int, int]]):
    location, direction = node
    r, c = location
    nr, nc = direction
    if nr == 0:
        yield (r - 1, c), (-1, 0)
        yield (r + 1, c), (1, 0)
    if nc == 0:
        yield (r, c - 1), (0, -1)
        yield (r, c + 1), (0, 1)
    if nr > 0:
        yield (r + 1, c), (nr + 1, 0)
    if nr < 0:
        yield (r - 1, c), (nr - 1, 0)
    if nc > 0:
        yield (r, c + 1), (0, nc + 1)
    if nc < 0:
        yield (r, c - 1), (0, nc - 1)


def dijkstra(grid, destination, neighbors, max_run):
    """Modified Dijkstra's shortest path Algorithmg
    src: https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day17.py"""

    start_location, start_direction = (0, 0), (0, 0)
    start = (start_location, start_direction)
    dist = collections.defaultdict(lambda: math.inf, {start: 0})
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)
        loc, vec = node
        if not all(-max_run <= component <= max_run for component in vec):
            continue
        if loc == destination:
            return dist[node]
        for neighbor in neighbors(node):
            nlocation = neighbor[0]
            if nlocation not in grid:
                continue
            new_dist = dist[node] + grid[nlocation]
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # No path found
    return math.inf


def part1(input_file: str) -> int:
    graph, destination = read_input(input_file)
    result = dijkstra(graph, destination, get_neighbors, 3)
    return int(result)


def part2(input_file: str) -> int:
    grid = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 102
    print('Part 1 OK')

    # assert part2(filename) == 51
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1013
    # assert solution_part2 == 8239


if __name__ == '__main__':
    test()
    main()
