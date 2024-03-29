import os
import re

def readInput(filename: str) -> dict[int: dict[int: str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    people = {}
    with open(input_file_path, "r") as f:
        for idx, line in enumerate(f, 1):
            items = {k: int(v) for k, v in re.findall(r'(\w+): (\d+)', line)}
            people[idx] = items
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
    for idx, stuff in people.items():
        if all(ticker_tape[k] == v for k, v in stuff.items()):
            return idx
    return None


def part2(people: dict) -> int:
    for idx, stuff in people.items():
        found = True
        for k, v in stuff.items():
            if k in ['cats', 'trees']:
                if v <= ticker_tape[k]:
                    found = False
                    break
            elif k in ['pomeranians', 'goldfish']:
                if v >= ticker_tape[k]:
                    found = False
                    break
            elif k not in ['pomeranians', 'goldfish', 'cats', 'trees']:
                if ticker_tape[k] != v:
                    found = False
                    break
        if found:
            return idx
    return None


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 103

    solution_part2 = part2(data)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 405


if __name__ == "__main__":
    main()
