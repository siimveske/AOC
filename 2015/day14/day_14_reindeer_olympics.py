from __future__ import annotations

import os
import re
from collections import defaultdict


def readInput(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    reindeers = []
    reindeer_pattern = re.compile(
        r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    )
    with open(input_file_path, "r") as f:
        for line in f:
            name, speed, duration, rest = reindeer_pattern.findall(line)[0]
            reindeers.append((name, int(speed), int(duration), int(rest)))
    return reindeers


def calculate_distances(reindeers, travel_time) -> dict:
    distances = dict()
    for name, speed, duration, rest in reindeers:
        cycle = duration + rest
        total_cycles = travel_time // cycle
        remainder = travel_time % cycle
        extra = min(duration, remainder)
        movement_time = total_cycles * duration + extra
        distance = speed * movement_time
        distances[name] = distance
    return distances


def part1(reindeers: list, duration=2503) -> int:
    distances = calculate_distances(reindeers, travel_time=duration)
    return max(distances.values())


def part2(reindeers: list, duration=2503) -> int:
    points = defaultdict(int)
    for i in range(duration):
        distances = calculate_distances(reindeers, travel_time=i + 1)
        max_dist = max(distances.values())
        for reindeer in distances:
            if distances[reindeer] == max_dist:
                points[reindeer] += 1
    winner = max(points.values())
    return winner


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    data = readInput(filename)

    assert part1(data, duration=1000) == 1120
    assert part2(data, duration=1000) == 689

    print("OK\n")


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 2660

    solution_part2 = part2(data)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 1256


if __name__ == "__main__":
    test()
    main()
