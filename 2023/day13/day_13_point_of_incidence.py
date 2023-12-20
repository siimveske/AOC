import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        patterns = f.read().split('\n\n')
        patterns = [pattern.splitlines() for pattern in patterns]

    return patterns


def find(grid) -> int:
    """Solution src: https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day13.py"""
    result = 0
    for i in range(1, len(grid)):
        if all(a == b for a, b in zip(grid[:i][::-1], grid[i:])):
            result = i
            break
    return result


def find2(grid) -> int:
    """Solution src: https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day13.py"""
    result = 0
    for i in range(1, len(grid)):
        differs = []
        for a, b in zip(grid[:i][::-1], grid[i:]):
            for ax, bx in zip(a, b):
                differs.append(ax != bx)
        if sum(differs) == 1:
            result = i
            break
    return result


def part1(input_file: str) -> int:
    grids = read_input(input_file)
    result = 0
    for grid in grids:
        result += 100 * find(grid)
        result += find([*zip(*grid)])

    return result


def part2(input_file: str) -> int:
    grids = read_input(input_file)
    result = 0
    for grid in grids:
        result += 100 * find2(grid)
        result += find2([*zip(*grid)])

    return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 405

    filename = "test_input2.txt"
    assert part1(filename) == 10

    print("Part 1 OK")

    filename = "test_input3.txt"
    assert part2(filename) == 400

    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 33975
    assert solution_part2 == 29083


if __name__ == "__main__":
    test()
    main()
