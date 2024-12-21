import heapq
import os

def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = None
    with open(file_path, "r") as file:
        grid = file.read().splitlines()
        for r, row in enumerate(grid):
            if start:
                break
            for c, char in enumerate(row):
                if char == "S":
                    start = (r, c)
                    break

    return grid, start


def rotate(current_dir, steps: int) -> tuple:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index = directions.index(current_dir)
    rotated_index = (index + steps) % len(directions)
    return directions[rotated_index]


def dijkstra(grid, position):
    """Dijkstra's shortest path Algorithm"""

    direction = (0, 1)
    pq = [(0, position, direction)] # (cost, location, direction)
    visited = {(position, direction)}

    while pq:
        cost, location, direction = heapq.heappop(pq)
        visited.add((location, direction))

        r, c = location
        if grid[r][c] == "E":
            return cost

        left_dir = rotate(direction, -1)
        right_dir = rotate(direction, 1)
        next_location = (r + direction[0], c + direction[1])
        neighbors = [
            (cost + 1, next_location, direction),
            (cost + 1000, location, left_dir),
            (cost + 1000, location, right_dir)]

        for new_cost, new_pos, new_dir in neighbors:
            if (new_pos, new_dir) in visited:
                continue
            nr, nc = new_pos
            if grid[nr][nc] == "#":
                continue
            heapq.heappush(pq, (new_cost, new_pos, new_dir))

    return float("inf")


def part1(input_file: str) -> int:
    grid, start = read_input(input_file)
    min_cost = dijkstra(grid, start)
    return min_cost


# def part2(input_file: str) -> int:
#     grid, commands, start_position = read_input(input_file)
#     pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 7036

    filename = "test_input2.txt"
    assert part1(filename) == 11048

    print("Part 1 OK")

    # assert part2(filename) == 618
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 72400
    # assert solution_part2 == 1538862


if __name__ == "__main__":
    test()
    main()
