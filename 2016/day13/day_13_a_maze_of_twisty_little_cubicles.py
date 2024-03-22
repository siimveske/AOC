from collections import deque


def is_open_space(location: tuple[int, int], puzzle_input: int) -> bool:
    x, y = location
    binary = bin(x * x + 3 * x + 2 * x * y + y + y * y + puzzle_input)
    return binary.count("1") % 2 == 0


def get_adjacent_points(x: int, y: int) -> list[tuple[int, int]]:
    return [(nx, ny) for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if nx >= 0 and ny >= 0]


def bfs(puzzle_input: int, end: tuple[int, int] | None, max_steps: int | None = None) -> int:
    queue = deque([((1, 1), 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end or (max_steps is not None and steps > max_steps):
            return steps if (x, y) == end else len(visited)
        if (x, y) in visited:
            continue

        visited.add((x, y))
        for point in get_adjacent_points(x, y):
            if point not in visited and is_open_space(point, puzzle_input):
                queue.append((point, steps + 1))


def part1() -> int:
    return bfs(1358, (31, 39))


def part2() -> int:
    return bfs(1358, None, 50)


def test():
    print("---- TEST ----")

    assert bfs(10, (7, 4)) == 11
    print("Part 1: OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 96

    solution_part2 = part2()
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 141


if __name__ == "__main__":
    test()
    main()
