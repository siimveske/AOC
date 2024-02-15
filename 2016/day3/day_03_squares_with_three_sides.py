import os


def read_input(filename: str) -> list[tuple[int, int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    triangles = []
    with open(input_file_path, "r") as f:
        for line in f:
            sides = line.strip().split()
            a, b, c = map(int, sides)
            triangles.append((a, b, c))
    return triangles


def part1(filename: str) -> int:
    triangles = read_input(filename)
    filtered_triangles = []
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            filtered_triangles.append((a, b, c))
    return len(filtered_triangles)


def part2(filename: str) -> int:
    triangles = read_input(filename)
    filtered_triangles = []
    rows = len(triangles)
    cols = len(triangles[0])
    for idx_c in range(cols):
        for idx_r in range(0, rows, 3):
            a = triangles[idx_r][idx_c]
            b = triangles[idx_r + 1][idx_c]
            c = triangles[idx_r + 2][idx_c]
            if a + b > c and a + c > b and b + c > a:
                filtered_triangles.append((a, b, c))
    return len(filtered_triangles)


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 993

    solution_part1 = part2(filename)
    print(f"Solution for Part 2: {solution_part1}")
    assert solution_part1 == 1849


if __name__ == "__main__":
    main()
