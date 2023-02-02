from __future__ import annotations
from collections import defaultdict
from itertools import combinations, product
from math import inf as INFINITY
import os
import re


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    flow_rates = {}

    with open(input_file_path, 'r') as f:
        for line in f:
            res = re.search(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
            name = res.group(1)                     # name of this valve
            flow_rates[name] = int(res.group(2))    # pressure release rate (per minute)
            graph[name] = res.group(3).split(", ")  # valves connected to this valve

    return graph, flow_rates


def floyd_warshall(graph: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    '''Calculate the minimum distance between any possible pair of nodes of a given graph'''
    distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

    for node, neighbours in graph.items():
        distance[node][node] = 0

        for neighbour in neighbours:
            distance[node][neighbour] = 1
            distance[neighbour][neighbour] = 0

    for a, b, c in product(graph, graph, graph):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance


def get_solutions(distances: dict[str, dict[str, int]], closed_valves: set[str], time=30, current_valve='AA', open_valves={}) -> set[dict[str, int]]:
    res = [open_valves]

    # For all the valves we can currently choose
    for next_valve in closed_valves:
        # Choosing this valve will take distances[current_valve][nxt_valve] to reach it + 1m to open it
        new_time = time - (distances[current_valve][next_valve] + 1)

        # We can't reach any other valve in less than 2m, as it would take minimum
        # 1m to reach it plus 1m to open it, and therefore it'd be stay open for 0m.
        if new_time < 2:
            continue

        # Choose this valve, it will stay open exactly for new_time (i.e. the time
        # we have now minus the time it takes to reach and open it).
        new_chosen = open_valves | {next_valve: new_time}

        # The new valves to choose from will not include this one
        still_closed_valves = closed_valves - {next_valve}
        res += get_solutions(distances, still_closed_valves, new_time, next_valve, new_chosen)
    return res


def get_score(rates: dict[str, int], solution_valves: dict[str, int]) -> int:
    '''Calculate total pressure release of the solution'''
    result = 0
    for valve, duration in solution_valves.items():
        result += rates[valve] * duration
    return result


def part1(inputFile: str) -> int:
    graph, rates = readInput(inputFile)
    distances = floyd_warshall(graph)
    valuable_valves = {key for key, val in rates.items() if val > 0}

    max_pressure = 0
    for solution in get_solutions(distances, valuable_valves):
        max_pressure = max(max_pressure, get_score(rates, solution))
    return max_pressure


def part2(inputFile: str) -> int:
    graph, rates = readInput(inputFile)
    distances = floyd_warshall(graph)

    valuable_valves = {key for key, val in rates.items() if val > 0}
    maxscore = defaultdict(int)
    for solution in get_solutions(distances, valuable_valves, 26):
        key = frozenset(solution)
        score = get_score(rates, solution)

        if score > maxscore[key]:
            maxscore[key] = score

    best = 0
    for (s1, score1), (s2, score2) in combinations(maxscore.items(), 2):
        if len(s1 & s2) == 0:
            best = max(best, score1 + score2)

    return best


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1651
    print('Part 1 OK')

    assert part2(filename) == 1707
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 2320
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    assert solution_part2 == 2967
    print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
