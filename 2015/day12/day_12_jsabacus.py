from __future__ import annotations

import os
import re
import json
from typing import Iterable


def readInput(filename: str) -> str:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read()


def part1(data: str) -> int:
    numbers = re.findall(r"-?\d+", data)
    result = sum(map(int, numbers))
    return result


def travel(data: Iterable):
    result = 0
    if type(data) == int:
        result = data
    elif type(data) == list:
        result = sum(map(travel, data))
    elif type(data) == dict:
        if "red" not in data.values():
            result = sum(map(travel, data.values()))
    return result


def part2(data: str) -> int:
    json_data = json.loads(data)
    result = travel(json_data)
    return result


def test():
    print("---- TEST ----")

    assert part1("[1,2,3]") == 6
    assert part1('{"a":2,"b":4}') == 6
    assert part1("[[[3]]]") == 3
    assert part1('{"a":{"b":4},"c":-1}') == 3
    assert part1('{"a":[-1,1]}') == 0
    assert part1('[-1,{"a":1}]') == 0
    assert part1("[]") == 0
    assert part1("{}") == 0

    assert part2("[1,2,3]") == 6
    assert part2('[1,{"c":"red","b":2},3]') == 4
    assert part2('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert part2('[1,"red",5]') == 6

    print("OK\n")


def main():
    print("---- MAIN ----")

    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 111754

    solution_part2 = part2(data)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 65402


if __name__ == "__main__":
    test()
    main()
