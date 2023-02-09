from __future__ import annotations

"""
inspired by: https://www.reddit.com/r/adventofcode/comments/3w192e/comment/cxsyg1w/?utm_source=share&utm_medium=web2x&context=3
"""
import os
from collections import defaultdict
import itertools


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = defaultdict(dict)
    with open(input_file_path, "r") as f:
        for line in f:
            src, _, dst, _, dist = line.strip().split(" ")
            graph[src][dst] = int(dist)
            graph[dst][src] = int(dist)
    return graph


def get_min_max_distance(graph: dict[str, dict[str, int]]) -> tuple[int, int]:
    distances = []
    cities = graph.keys()
    for perm in itertools.permutations(cities):
        distances.append(sum(map(lambda x, y: graph[x][y], perm[:-1], perm[1:])))
    return (min(distances), max(distances))


def part1(inputFile: str) -> int:
    graph = readInput(inputFile)
    return get_min_max_distance(graph)[0]


def part2(inputFile: str) -> int:
    graph = readInput(inputFile)
    return get_min_max_distance(graph)[1]


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
