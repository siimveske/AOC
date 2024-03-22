from collections import deque


def is_open_space(location: tuple[int, int], puzzle_input: int) -> bool:
    x, y = location
    result = x * x + 3 * x + 2 * x * y + y + y * y
    result += puzzle_input
    binary = bin(result)
    cnt_of_ones = binary.count("1")
    return cnt_of_ones % 2 == 0


def part1(puzzle_input: int, end: tuple[int, int]) -> int:
    start = (1, 1)
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps
        if (x, y) in visited:
            continue

        steps += 1
        visited.add((x, y))

        right = (x + 1, y)
        left = (x - 1, y)
        up = (x, y + 1)
        down = (x, y - 1)

        if right not in visited and is_open_space(right, puzzle_input):
            queue.append((right, steps))
        if left not in visited and left[0] >= 0 and is_open_space(left, puzzle_input):
            queue.append((left, steps))
        if up not in visited and is_open_space(up, puzzle_input):
            queue.append((up, steps))
        if down not in visited and down[1] >= 0 and is_open_space(down, puzzle_input):
            queue.append((down, steps))

        visited.add((x, y))


def part2() -> int:
    puzzle_input: int = 1358
    start = (1, 1)
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) in visited:
            continue
        if steps > 50:
            continue

        steps += 1
        visited.add((x, y))

        right = (x + 1, y)
        left = (x - 1, y)
        up = (x, y + 1)
        down = (x, y - 1)

        if right not in visited and is_open_space(right, puzzle_input):
            queue.append((right, steps))
        if left not in visited and left[0] >= 0 and is_open_space(left, puzzle_input):
            queue.append((left, steps))
        if up not in visited and is_open_space(up, puzzle_input):
            queue.append((up, steps))
        if down not in visited and down[1] >= 0 and is_open_space(down, puzzle_input):
            queue.append((down, steps))

    return len(visited)


def test():
    print("---- TEST ----")

    assert part1(puzzle_input=10, end=(7, 4)) == 11
    print("Part 1: OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1(puzzle_input=1358, end=(31, 39))
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 96

    solution_part2 = part2()
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 141


if __name__ == "__main__":
    test()
    main()
