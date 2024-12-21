from collections import defaultdict
import heapq
import os


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = {}
    start = None
    with open(file_path, "r") as file:
        data = file.read().splitlines()
        for r, row in enumerate(data):
            for c, char in enumerate(row):
                if char == "S":
                    start = (r, c)
                if char != "#":
                    grid[r, c] = char
    return grid, start


def dijkstra(grid, position):
    """Modified Dijkstra's shortest path algorithm"""

    seen = []
    best = float("inf")
    orientation = (0, 1)
    dist = defaultdict(lambda: float("inf"))
    todo = [(0, position, orientation, [position])]

    while todo:
        val, pos, _dir, path = heapq.heappop(todo)
        if val > dist[pos, _dir]:
            continue

        dist[pos, _dir] = val

        if grid[pos] == 'E' and val <= best:
            seen += path
            best = val

        r, c = pos
        dr, dc = _dir
        neighbors = [
            (val + 1, r + dr, c + dc, dr, dc),
            (val + 1000, r, c, dc, -dr),
            (val + 1000, r, c, -dc, dr)
        ]
        for new_cost, nr, nc, ndr, ndc in neighbors:
            new_pos = (nr, nc)
            new_dir = (ndr, ndc)
            if new_pos not in grid:
                continue
            heapq.heappush(todo, (new_cost, new_pos, new_dir, path + [new_pos]))

    return best, len(set(seen))


def part1(input_file: str) -> int:
    grid, start = read_input(input_file)
    min_cost = dijkstra(grid, start)[0]
    return min_cost


def part2(input_file: str) -> int:
    grid, start = read_input(input_file)
    num_of_tiles = dijkstra(grid, start)[1]
    return num_of_tiles


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 7036

    filename = "test_input2.txt"
    assert part1(filename) == 11048
    print("Part 1 OK")

    filename = "test_input.txt"
    assert part2(filename) == 45

    filename = "test_input2.txt"
    assert part2(filename) == 64
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 72400
    assert solution_part2 == 435


if __name__ == "__main__":
    test()
    main()
