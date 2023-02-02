import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    paths = defaultdict(list)
    with open(input_file_path, 'r') as f:
        for line in f:
            A, B = line.strip().split('-')
            if B != 'start':
                paths[A].append(B)
            if A != 'start':
                paths[B].append(A)
    paths.pop('end')
    return paths


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node.islower() and node in path:
            continue
        else:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def find_paths(graph):
    paths = []
    stack = [('start', [], False)]
    while stack:
        current, path, visited = stack.pop()

        if current == 'end':
            paths.append(path + [current])
            continue

        if current.islower() and current in path:
            if visited:
                continue
            visited = True

        stack.extend([(node, [*path, current], visited) for node in graph[current]])

    return paths


def part1(inputFile: str):
    graph = readInput(inputFile)
    paths = find_all_paths(graph, 'start', 'end')
    return len(paths)


def part2(inputFile: str):
    graph = readInput(inputFile)
    paths = find_paths(graph)
    return len(paths)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 10
    print('Part 1 OK')
    assert part2(filename) == 36
    print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
