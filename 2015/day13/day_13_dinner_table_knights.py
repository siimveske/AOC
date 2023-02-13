from __future__ import annotations

import os
from collections import defaultdict
from itertools import permutations

"""
inspired by: https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2015/d13_seating_arrangement_with_circular_set_and_perms/happy_seating.py
"""


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = defaultdict(dict)
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            a = parts[0]
            sign = 1 if parts[2] == "gain" else -1
            val = int(parts[3])
            b = parts[10][:-1]
            graph[a][b] = sign * val
    return graph


def sum_happiness(seating_arrangement: list, happiness_by_person: dict) -> int:
    happiness = 0
    for i, current_person in enumerate(seating_arrangement):
        current_next_person = seating_arrangement[(i + 1) % len(seating_arrangement)]
        happiness += happiness_by_person[current_person][current_next_person]
        happiness += happiness_by_person[current_next_person][current_person]
    return happiness


def calculate_hapiness(graph, start, perms):
    max_happiness = 0
    for perm in perms:
        # this allows us to remove reverse permutations
        if perm <= perm[::-1]:
            # convert perm from tuple to list, to make it mutable and insert the head of the table
            # such that we can insert the head of the table
            perm = [start] + list(perm)
            max_happiness = max(max_happiness, sum_happiness(perm, graph))
    return max_happiness


def part1(inputFile: str) -> int:
    graph = readInput(inputFile)
    people = set(graph.keys())
    start = people.pop()
    perms = list(permutations(people))

    max_happiness = calculate_hapiness(graph, start, perms)
    return max_happiness


def part2(inputFile: str) -> int:
    graph = readInput(inputFile)
    people = set(graph.keys())
    start = next(iter(people))
    add_me_to_graph(graph)
    people.remove(start)
    people.add("Me")
    perms = list(permutations(people))

    max_happiness = calculate_hapiness(graph, start, perms)
    return max_happiness


def add_me_to_graph(graph: dict):
    people = set(graph.keys())
    for person in people:
        graph[person]["Me"] = 0
        graph["Me"][person] = 0


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 330

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 618

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 601


if __name__ == "__main__":
    test()
    main()
