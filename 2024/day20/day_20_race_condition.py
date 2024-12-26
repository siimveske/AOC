import os
from collections import defaultdict, deque

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = None
    end = None
    with open(file_path, "r") as file:
        data = file.read().splitlines()
        for row in data:
            grid.append(list(row))

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "S":
                    start = (r, c)
                elif col == "E":
                    end = (r, c)

    return grid, start, end


def find_path(grid, start, end):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path

        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if ((nr, nc) not in visited and grid[nr][nc] != '#'):
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))

    return None


def part1(input_file: str, cheat_value: int) -> int:
    """
    Calculate the number of valid cheat paths that save at least cheat_value steps.
    A cheat path involves jumping through a wall to skip ahead in the path.
    """
    grid, start, end = read_input(input_file)

    # Convert grid to coordinate map for easier lookup
    grid_map = {(r, c): col for r, row in enumerate(grid)
                for c, col in enumerate(row)}

    # Find shortest path and create index lookup
    path = find_path(grid, start, end)
    indexed_path = {pos: idx for idx, pos in enumerate(path)}

    # Directions to check for potential wall jumps
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Count shortcuts of different lengths
    shortcuts = defaultdict(int)
    for current_pos in path[:-1]:
        r, c = current_pos
        current_idx = indexed_path[current_pos]

        for dr, dc in directions:
            # Check if there's a wall we can jump through
            wall_pos = (r + dr, c + dc)
            if grid_map.get(wall_pos) != '#':
                continue

            # Check landing position after wall jump
            landing_pos = (r + 2*dr, c + 2*dc)
            landing_idx = indexed_path.get(landing_pos, 0)
            if landing_idx <= current_idx:
                continue

            # Calculate how many steps we save
            steps_saved = landing_idx - current_idx - 2
            if steps_saved > 0:
                shortcuts[steps_saved] += 1

    return sum(count for steps, count in shortcuts.items() if steps >= cheat_value)


# def part2(input_file: str) -> int:
#     patterns, strings = read_input(input_file)
#     results = {s: count_construct(s, patterns) for s in strings}
#     result = sum(results.values())
#     return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename, cheat_value=20) == 5
    print("Part 1 OK")

    # assert part2(filename) == 16
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename, cheat_value=100)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 1293
    # assert solution_part2 == 891192814474630


if __name__ == "__main__":
    test()
    main()
