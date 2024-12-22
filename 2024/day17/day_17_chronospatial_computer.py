import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        registry, program = file.read().split("\n\n")
        registry = [int(i) for i in re.findall(r"(\d+)", registry)]
        program = [int(i) for i in re.findall(r"(\d+)", program)]

    return registry, program


def part1(input_file: str) -> int:
    data = read_input(input_file)
    return 0


# def part2(input_file: str) -> int:
#     grid, start = read_input(input_file)
#     num_of_tiles = dijkstra(grid, start)[1]
#     return num_of_tiles


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == "4,6,3,5,6,3,5,2,1,0"

    print("Part 1 OK")

    # filename = "test_input.txt"
    # assert part2(filename) == 45

    # filename = "test_input2.txt"
    # assert part2(filename) == 64
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    # assert solution_part1 == 72400
    # assert solution_part2 == 435


if __name__ == "__main__":
    test()
    main()
