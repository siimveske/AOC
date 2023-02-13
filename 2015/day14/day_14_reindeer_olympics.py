from __future__ import annotations

import os
from itertools import permutations


def readInput(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    reindeers = []
    with open(input_file_path, "r") as f:
        for line in f:
            parts = line.split()
            name = parts[0]
            speed = int(parts[3])
            duration = int(parts[6])
            pause = int(parts[-2])
            reindeers.append((name, speed, duration, pause))
    return reindeers


def calculate_distances(reindeers, travel_time):
    distances = dict()
    for name, speed, duration, pause in reindeers:
        period = duration + pause
        d = travel_time // period
        m = travel_time % period
        extra = min(duration, m)
        movement_time = d * duration + extra
        distance = speed * movement_time
        distances[name] = distance
    return distances


def part1(inputFile: str) -> int:
    reindeers = readInput(inputFile)
    distances = calculate_distances(reindeers, travel_time=2503)
    return max(distances.values())


def part2(inputFile: str) -> int:
    graph = readInput(inputFile)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    # assert part1(filename) == 330

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 618

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 601


if __name__ == "__main__":
    test()
    main()
