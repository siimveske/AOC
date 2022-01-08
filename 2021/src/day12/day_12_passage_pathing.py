import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    paths = defaultdict(list)
    with open(input_file_path, 'r') as f:
        for line in f:
            A, B = line.strip().split('-')
            paths[A].append(B)
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


def find_all_paths2(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []

    count_map = defaultdict(int)
    doubble_visit_counter = 0
    for node in path:
        count_map[node] += 1
    for key in count_map.keys():
        if key.islower() and key not in ['start', 'end'] and count_map[key] >= 2:
            doubble_visit_counter += 1

    for node in graph[start]:
        if node in path and node in ['start', 'end']:
            continue
        if node.islower() and node in path and doubble_visit_counter:
            continue
        else:
            newpaths = find_all_paths2(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def part1(inputFile: str):
    graph = readInput(inputFile)
    paths = find_all_paths(graph, 'start', 'end')
    return len(paths)


def part2(inputFile: str):
    graph = readInput(inputFile)
    paths = find_all_paths2(graph, 'start', 'end')
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
