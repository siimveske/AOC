import os
from collections import Counter
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    risk_levels = []
    graph = defaultdict(list)

    with open(input_file_path, 'r') as f:
        for line in f:
            risk_levels.append([int(i) for i in line.strip()])

    width = len(risk_levels[0])
    height = len(risk_levels)

    for i in range(height):
        for j in range(width):
            neighbours = []
            # top
            if (i - 1) >= 0:
                neighbours.append((i - 1, j))
            # right
            if (j + 1) <= (width - 1):
                neighbours.append((i, j + 1))
            # bottom
            if (i + 1) <= (height - 1):
                neighbours.append((i + 1, j))
            # left
            if (j - 1) >= 0:
                neighbours.append((i, j - 1))

            for n in neighbours:
                row, col = n
                graph[i, j].append((n, risk_levels[row][col]))
                graph[row, col].append(((i, j), risk_levels[i][j]))
                print()

    return (graph, (height - 1, width - 1))


def find_paths(graph, endnode):

    start = ((0, 0), 0)
    min_cost = float('inf')
    stack = [(start, [], 0)]

    while stack:
        (current, risk), path, cost = stack.pop()

        if current in path:
            continue

        new_cost = cost + risk
        if current == endnode:
            if new_cost < min_cost:
                min_cost = new_cost
            continue

        stack.extend([(neighbour, [*path, current], new_cost) for neighbour in graph[current]])

    return min_cost


def part1(inputFile: str):
    risk_graph, endnode = readInput(inputFile)
    paths = find_paths(risk_graph, endnode)
    return result


def part2(inputFile: str):
    template, instructions = readInput(inputFile)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 1588
    print('Part 1 OK')

    #solution_part2 = part2(filename)
    #assert solution_part2 == 2188189693529
    #print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    # main()
