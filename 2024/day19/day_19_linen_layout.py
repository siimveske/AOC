import os

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        a, b = file.read().split("\n\n")
        a = [i.strip() for i in a.split(",")]
        b = b.splitlines()
    return a,b


def part1(input_file: str) -> int:
    data = read_input(input_file)
    return 0


# def part2(input_file: str, rows: int, cols: int) -> str:
#     coordinates = read_input(input_file)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 22
    print("Part 1 OK")

    # assert part2(filename, rows=7, cols=7) == "6,1"
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename, rows=71, cols=71)
    # print(f"Solution for Part 2: {solution_part2}\n")

    # assert solution_part1 == 276
    # assert solution_part2 == "60,37"


if __name__ == "__main__":
    test()
    main()
