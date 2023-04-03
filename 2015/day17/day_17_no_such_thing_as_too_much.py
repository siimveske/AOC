from itertools import combinations
import os

def readInput(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return [int(i) for i in f]

def part1(containers: list, target=150) -> int:
    count = 0
    for i in range(1, len(containers)+1):
        for c in combinations(containers, i):
            if sum(c) == target:
                count += 1
    return count


def part2(containers: dict) -> int:
    pass


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 1638

    # solution_part2 = part2(data)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 405


if __name__ == "__main__":
    main()
