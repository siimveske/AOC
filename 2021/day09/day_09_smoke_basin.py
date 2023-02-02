import os
import math
from collections import defaultdict
from queue import Queue


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            data.append([int(i) for i in line.strip()])
    return data


def part1(inputFile: str):
    data = readInput(inputFile)

    low_points = []
    cords = []
    graph = defaultdict(list)

    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):

            up = i - 1
            down = i + 1
            left = j - 1
            right = j + 1

            # logic to build graph for part2
            if up >= 0 and data[i][j] != 9 and data[up][j] != 9:
                graph[(i, j)].append((up, j))
            if down < rows and data[i][j] != 9 and data[down][j] != 9:
                graph[(i, j)].append((down, j))
            if left >= 0 and data[i][j] != 9 and data[i][left] != 9:
                graph[(i, j)].append((i, left))
            if right < cols and data[i][j] != 9 and data[i][right] != 9:
                graph[(i, j)].append((i, right))

            # logic to find low point for part1
            if up >= 0 and data[up][j] <= data[i][j]:
                continue
            if down < rows and data[down][j] <= data[i][j]:
                continue
            if left >= 0 and data[i][left] <= data[i][j]:
                continue
            if right < cols and data[i][right] <= data[i][j]:
                continue

            low_points.append(data[i][j])
            cords.append((i, j))

    part1_solution = sum([i + 1 for i in low_points])
    return [part1_solution, cords, graph]


def find_basin_size(cord, graph):
    visited = set()
    queue: Queue = Queue()

    visited.add(cord)
    queue.put(cord)

    while not queue.empty():
        vertex = queue.get()
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex not in visited:
                queue.put(adjacent_vertex)
                visited.add(adjacent_vertex)

    return len(visited)


def part2(cords, graph):
    results = []
    for cord in cords:
        size = find_basin_size(cord, graph)
        results.append(size)

    results = sorted(results, reverse=True)
    part2_solution = math.prod(results[0:3])

    return part2_solution


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    solution_part1, cords, graph = part1(filename)
    assert solution_part1 == 15
    print('Part 1 OK')
    assert part2(cords, graph) == 1134
    print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1, cords, graph = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(cords, graph)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
