from __future__ import annotations
from collections import defaultdict
from itertools import product
from math import inf as INFINITY
import os

'''https://github.com/mebeim/aoc/blob/master/2022/README.md#day-16---proboscidea-volcanium'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    rates = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            valve, neighbours = line.strip().split(';')
            valve_code = valve[6:8]
            valve_flow_rate = int(valve[23:])

            neighbours = neighbours.strip()
            neighbours = neighbours.split(' ')[4:]
            neighbours = [n[0:2] for n in neighbours]

            graph[valve_code] = neighbours
            rates[valve_code] = valve_flow_rate
    return (graph, rates)


def floyd_warshall(g):
    distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

    for a, bs in g.items():
        distance[a][a] = 0

        for b in bs:
            distance[a][b] = 1
            distance[b][b] = 0

    for a, b, c in product(g, g, g):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance


def get_solutions(distances, valves, time=30, current_valve='AA', chosen_valves={}):
    for nxt_valve in valves:
        new_time = time - distances[current_valve][nxt_valve] - 1
        if new_time < 2:
            continue

        new_chosen = chosen_valves | {nxt_valve: new_time}
        yield from get_solutions(distances, valves - {nxt_valve}, new_time, nxt_valve, new_chosen)

    yield chosen_valves


def score(rates, valves):
    result = 0
    for valve, duration in valves.items():
        result += rates[valve] * duration
    return result


def part1(inputFile: str) -> int:
    graph, rates = readInput(inputFile)
    distances = floyd_warshall(graph)
    valves = frozenset(filter(rates.get, graph))

    max_pressure = 0
    for solution in get_solutions(distances, valves):
        max_pressure = max(max_pressure, score(rates, solution))
    return max_pressure


def part2(inputFile: str):
    data = readInput(inputFile)
    return 0


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

    # solution_part2 = part2(filename)
    # assert solution_part2 == 11482462818989
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
