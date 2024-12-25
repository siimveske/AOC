import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            a, b = [int(i) for i in re.findall(r"(\d+)", line)]
            coordinates.append((a, b))

    return coordinates

def part1(input_file: str) -> int:
    coordinates = read_input(input_file)
    return 0


# def part2(input_file: str) -> int:
#     _, program = read_input(input_file)
#     result = find_quine_input(0, 0, program)
#     return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 22
    print("Part 1 OK")

    # filename = "test_input2.txt"
    # assert part2(filename) == 117440
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    # assert solution_part1 == "7,1,3,7,5,1,0,3,4"
    # assert solution_part2 == 190384113204239


if __name__ == "__main__":
    test()
    main()
