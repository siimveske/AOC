from __future__ import annotations
import heapq

import os
from collections import defaultdict, deque
import itertools
from math import inf as INFINITY


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = defaultdict(list)
    with open(input_file_path, "r") as f:
        for line in f:
            parts = line.strip().split(" ")
            city_a = parts[0]
            city_b = parts[2]
            distance = int(parts[4])
            graph[city_a].append((city_b, distance))
            graph[city_b].append((city_a, distance))
    return graph


# def floyd_warshall(
#     graph: dict[str, list[tuple(str, int)]]
# ) -> dict[str, dict[str, int]]:
#     """Calculate the minimum distance between any possible pair of nodes of a given graph"""
#     distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

#     for node, neighbours in graph.items():
#         distance[node][node] = 0

#         for neighbour, dist in neighbours:
#             distance[node][neighbour] = dist
#             distance[neighbour][neighbour] = 0

#     for a, b, c in itertools.product(graph, graph, graph):
#         bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

#         if ba + ac < bc:
#             distance[b][c] = ba + ac

#     return distance


def shortest_path(graph, path, distance):
    if len(path) == len(graph):
        return distance

    min_path = float("inf")
    for neighbour, ndistance in graph[path[-1]]:
        if neighbour not in path:
            result = shortest_path(graph, path + [neighbour], distance + ndistance)
            min_path = min(min_path, result)
    return min_path


def longest_path(graph, path, distance):
    if len(path) == len(graph):
        return distance

    max_path = float("-inf")
    for neighbour, ndistance in graph[path[-1]]:
        if neighbour not in path:
            result = longest_path(graph, path + [neighbour], distance + ndistance)
            max_path = max(max_path, result)
    return max_path


def part1(inputFile: str) -> int:
    graph = readInput(inputFile)

    min_dist = float("inf")
    for node in graph:
        dist = shortest_path(graph, [node], 0)
        min_dist = min(min_dist, dist)
    return min_dist


def part2(inputFile: str) -> int:
    graph = readInput(inputFile)

    max_dist = float("-inf")
    for node in graph:
        dist = longest_path(graph, [node], 0)
        max_dist = max(max_dist, dist)
    return max_dist
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 605
    assert part2(filename) == 982

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 141

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 736


if __name__ == "__main__":
    test()
    main()
