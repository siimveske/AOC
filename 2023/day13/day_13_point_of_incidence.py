import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        patterns = f.read().split('\n\n')
        patterns = [pattern.splitlines() for pattern in patterns]

    return patterns


def check_for_mirror(pattern, i):
    splitpoint = i + 1
    pattern_length = len(pattern)
    if (pattern_length - splitpoint) > splitpoint:
        return False

    for j in range(splitpoint, pattern_length):
        a = pattern[j]
        b = pattern[pattern_length - j]
        if a != b:
            return False

    return True


def get_horizontal(pattern: list[str]):
    result = 0
    for i in range(0, len(pattern) - 1):
        this_line = pattern[i]
        next_line = pattern[i + 1]
        if this_line == next_line:
            is_mirrored = check_for_mirror(pattern, i)
            if is_mirrored:
                result = i + 1
                break
    return result


def get_vertical(matrix):
    t_matrix = list(zip(*matrix))
    result = get_horizontal(t_matrix)
    return result


def part1(input_file: str) -> int:
    patterns = read_input(input_file)
    result = 0
    for pattern in patterns:
        horizontal = get_horizontal(pattern)
        if horizontal:
            result += (horizontal * 100)
        else:
            vertical = get_vertical(pattern)
            result += vertical
    return result


def part2(input_file: str) -> int:
    broken_records = read_input(input_file)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename) == 405
    print("Part 1 OK")

    # assert part2(filename) == 525152
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")
    #
    # assert solution_part1 == 7599
    # assert solution_part2 == 15454556629917


if __name__ == "__main__":
    test()
    main()
