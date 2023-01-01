from __future__ import annotations
from dataclasses import dataclass
import os
import re


'''https://aoc.just2good.co.uk/2022/15'''


@dataclass(frozen=True)
class Point():
    """ Point with x, y coords. Knows how to add a vector, remove a vector,
    and calculate Manhattan distance to to another point. """
    x: int
    y: int

    def __sub__(self, other):
        """ Subtract other point from this point, returning new point vector """
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """ Subtract other point from this point, returning new point vector """
        return Point(self.x + other.x, self.y + other.y)

    def manhattan_distance_to(self, other: Point) -> int:
        """ Manhattan distance between this Vector and another Vector """
        diff = self - other
        return sum((abs(diff.x), abs(diff.y)))


def process_sensors(data) -> dict[Point, Point]:
    # Find four digits, preceeded by "not digit"
    pattern = re.compile(r"[\D]+x=(-?\d+)[\D]+y=(-?\d+)[\D]+x=(-?\d+)[\D]+y=(-?\d+)")
    sensor_to_beacon: dict[Point, Point] = {}
    for line in data:
        sx, sy, bx, by = map(int, pattern.findall(line)[0])
        sensor_to_beacon[Point(sx, sy)] = Point(bx, by)

    return sensor_to_beacon


class SensorGrid():
    """ Stores a grid of Sensors, and each sensor's nearest beacon. """

    def __init__(self, sensor_to_beacon: dict[Point, Point]) -> None:
        """ Takes a dictionary of Sensors and their beacons """
        self.sensor_to_beacon = sensor_to_beacon
        self.beacons = set(sensor_to_beacon.values())
        self.sensor_range = {s: b.manhattan_distance_to(s)
                             for s, b in self.sensor_to_beacon.items()}

        self._init_bounds()

    def _init_bounds(self):
        """ Get the bounds by finding min and max values of any scanner or beacon,
        then adding to each edge the maximum distance we've found for any Scanner->Beacon """
        max_distance = max(self.sensor_range.items(), key=lambda x: x[1])[1]
        self.min_x = self.min_y = self.max_x = self.max_y = 0
        for s, b in self.sensor_to_beacon.items():
            self.min_x = min([self.min_x, s.x, b.x])
            self.max_x = max([self.max_x, s.x, b.x])
            self.min_y = min([self.min_y, s.y, b.y])
            self.max_y = max([self.max_y, s.y, b.y])

        self.min_x -= max_distance
        self.min_y -= max_distance
        self.max_y += max_distance
        self.max_x += max_distance

    def _get_row_coverage_intervals(self, row: int) -> list[list]:
        """ For each nearby sensor, get all x interval for this row.
        Each sensor will return a range of coverage, like [a, b].
        So all sensors will return a list of ranges, like [[a, b][c, d][d, e]...] """

        # Get only the sensors that are within range of this row
        close_sensors = {s: r for s, r in self.sensor_range.items() if abs(s.y - row) <= r}

        intervals: list[list] = []  # store start and end y for each sensor
        for sensor, max_rng in close_sensors.items():
            vert_dist_to_row = abs(sensor.y - row)
            max_x_vector = (max_rng - vert_dist_to_row)
            start_x = sensor.x - max_x_vector
            end_x = sensor.x + max_x_vector
            intervals.append([start_x, end_x])

        return intervals

    def compress_intervals_for_row(self, row: int) -> list:
        """ Determines all intervals for a given row, in the form [[a, b][c, d][d, e]...]
        Intervals can overlap.  Compresses to minimum number of non-overlapping intervals. """
        intervals = self._get_row_coverage_intervals(row)  # In the form [[a, b][c, d][d, e]...]
        intervals.sort()
        stack = []
        stack.append(intervals[0])

        for interval in intervals[1:]:
            # Check for overlapping interval
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], interval[-1])
            else:
                stack.append(interval)

        return stack

    def __str__(self) -> str:
        rows = []
        for y in range(self.min_y, self.max_y + 1):
            row = ""
            for x in range(self.min_x, self.max_x + 1):
                point = Point(x, y)
                if point in self.sensor_to_beacon.keys():
                    row += "S"
                elif point in self.beacons:
                    row += "B"
                else:
                    row += "."

            rows.append(row)

        return "\n".join(rows)


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = process_sensors(f)
    return data


def part1(inputFile: str, TARGET_ROW: int) -> int:
    data = readInput(inputFile)
    grid = SensorGrid(data)

    row_intervals = grid.compress_intervals_for_row(TARGET_ROW)
    coverage_count = sum(interval[1] - interval[0] + 1 for interval in row_intervals)
    beacons_to_exclude = sum(1 for beacon in grid.beacons if beacon.y == TARGET_ROW)
    solution = coverage_count - beacons_to_exclude

    return solution


def part2(inputFile: str):
    cave = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename, TARGET_ROW=10) == 26
    print('Part 1 OK')

    # assert part2(filename) == 93
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename, TARGET_ROW=2000000)
    # assert solution_part1 == 26
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 27194
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
