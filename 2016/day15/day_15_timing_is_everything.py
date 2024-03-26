import hashlib
import re
import os


def read_input(filename: str) -> list[tuple[int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    disks = []
    with open(input_file_path, "r") as f:
        for line in f:
            tokens = line.split()
            postitions, position = tokens[3], tokens[-1][:-1]
            disks.append((int(postitions), int(position)))
    return disks


def part1(filename: str) -> int:
    disks = read_input(filename)
    time = 0
    while True:
        for idx, (postitions, position) in enumerate(disks, 1):
            if (position + time + idx) % postitions != 0:
                time += 1
                break
        else:
            return time


def part2(filename: str) -> int:
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename) == 5
    print("Part 1: OK")

    # assert part2(filename) == 22551
    # print("Part 2: OK")


def main():
    print("---- MAIN ----")

    filename = "input.txt"
    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 400589

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 20092


if __name__ == "__main__":
    test()
    main()
