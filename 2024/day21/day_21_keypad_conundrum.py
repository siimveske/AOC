import os

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        grid = [list(row) for row in file.read().splitlines()]
    return grid


def part1(input_file: str) -> int:
    grid, start, end = read_input(input_file)
    path = find_path(grid, start, end)
    result = count_cheats(path, max_distance, threshold)
    return result


# def part2(input_file: str, max_distance: int, threshold: int) -> int:
#     grid, start, end = read_input(input_file)
#     path = find_path(grid, start, end)
#     result = count_cheats(path, max_distance, threshold)
#     return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 126384
    print("Part 1 OK")

    # assert part2(filename, max_distance=20, threshold=76) == 3
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename, max_distance=20, threshold=100)
    # print(f"Solution for Part 2: {solution_part2}\n")

    # assert solution_part1 == 1293
    # assert solution_part2 == 977747


if __name__ == "__main__":
    test()
    main()
