import math
import os
import re


def readInput(filename: str) -> dict[int: dict[int: str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    people = {}
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            person, items = line.split(': ', 1)
            person_id = int(person.split(' ')[1])
            parsed_items = {}
            for item in items.split(', '):
                k, v = item.split(': ')
                parsed_items[k] = int(v)
            people[person_id] = parsed_items
            print()
    return people


ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def part1(people: dict) -> int:
    solution = None
    for idx, stuff in people.items():
        found = True
        for k, v in stuff.items():
            if ticker_tape[k] != v:
                found = False
                break
        if found:
            solution = idx
            break
    return solution



def part2(people: list) -> int:
    pass


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    people = readInput(filename)

    solution_part1 = part1(people)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 103

    # solution_part2 = part2(data)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 117936


if __name__ == "__main__":
    #test()
    main()
