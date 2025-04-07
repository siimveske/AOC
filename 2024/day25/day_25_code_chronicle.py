import os


def read_input(filename: str) -> tuple:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    def count_blocks_in_column(lines: list, col_index: int) -> int:
        return sum(1 for row in lines if row[col_index] == "#")

    def get_height_pattern(item: str) -> tuple:
        lines = item.splitlines()
        column_count = len(lines[0])
        heights = [count_blocks_in_column(lines, col) for col in range(column_count)]
        return tuple(heights)

    keys = []
    locks = []

    with open(file_path, "r") as file:
        patterns = file.read().strip().split("\n\n")
        free_space = len(patterns[0].splitlines())

        for pattern in patterns:
            heights = get_height_pattern(pattern)
            if pattern.startswith("#####"):
                locks.append(heights)
            else:
                keys.append(heights)

    return locks, keys, free_space


def part1(input_file: str) -> int:
    locks, keys, free_space = read_input(input_file)
    compatible_pairs = set()

    def can_fit_together(lock, key):
        return all(l + k <= free_space for l, k in zip(lock, key))

    for lock in locks:
        for key in keys:
            if can_fit_together(lock, key):
                compatible_pairs.add((lock, key))

    return len(compatible_pairs)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 3
    print("Part 1 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    assert solution_part1 == 2900


if __name__ == "__main__":
    test()
    main()
