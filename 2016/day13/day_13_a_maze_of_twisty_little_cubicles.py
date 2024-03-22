from collections import deque


def is_open_space(location: tuple[int, int], puzzle_input: int) -> bool:
    x, y = location
    result = x * x + 3 * x + 2 * x * y + y + y * y
    result += puzzle_input
    binary = bin(result)
    cnt_of_ones = sum([1 for c in binary if c == "1"])
    return cnt_of_ones % 2 == 0


def print_maze(puzzle_input: int):
    rows = 7
    cols = 10
    for r in range(rows):
        for c in range(cols):
            if is_open_space(c, r, puzzle_input):
                print(".", end="")
            else:
                print("#", end="")
        print()


def part1(puzzle_input: int, end: tuple[int, int]) -> int:
    start = (1, 1)
    queue = deque([(start, 0)])
    visited = set()

    # print_maze(puzzle_input)

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps
        if (x, y) in visited:
            continue

        right = (x + 1, y)
        left = (x - 1, y)
        up = (x, y + 1)
        down = (x, y - 1)
        if right not in visited and is_open_space(right, puzzle_input):
            queue.append((right, steps + 1))
        if left not in visited and left[0] >= 0 and is_open_space(left, puzzle_input):
            queue.append((left, steps + 1))
        if up not in visited and is_open_space(up, puzzle_input):
            queue.append((up, steps + 1))
        if down not in visited and down[1] >= 0 and is_open_space(down, puzzle_input):
            queue.append((down, steps + 1))

        visited.add((x, y))


def part2() -> int:
    pass


def test():
    print("---- TEST ----")

    assert part1(puzzle_input=10, end=(7, 4)) == 11
    print("Part 1: OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1(puzzle_input=1358, end=(31, 39))
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 96

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 9227674


if __name__ == "__main__":
    test()
    main()
