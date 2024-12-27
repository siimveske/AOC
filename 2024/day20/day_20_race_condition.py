import os
from collections import deque

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = end = None

    with open(file_path, "r") as file:
        # Convert input into 2D grid using list comprehension
        grid = [list(row) for row in file.read().splitlines()]

        # Find start and end positions
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char == "S":
                    start = (r, c)
                elif char == "E":
                    end = (r, c)
                # Break inner loop if both found
                if start and end:
                    break
            # Break outer loop if both found
            if start and end:
                break

    return grid, start, end


def find_path(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Finds the shortest path from start to end using breadth-first search (BFS).

    Args:
        grid: 2D grid where '#' represents walls
        start: Starting position as (row, col)
        end: Target position as (row, col)

    Returns:
        List of (row, col) coordinates representing the path, or None if no path exists
    """
    # Initialize queue with starting position and its path
    queue = deque([(start, [start])])
    # Keep track of visited positions to avoid cycles
    visited = {start}

    while queue:
        # Get next position and the path taken to reach it
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path

        # Check all four adjacent cells (up, down, left, right)
        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            # Only consider unvisited cells that aren't walls
            if ((nr, nc) not in visited and grid[nr][nc] != '#'):
                # Add new position to queue with updated path
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))

    # No path found
    return None


def count_cheats(path: list[tuple[int, int]], max_distance: int, threshold: int) -> int:
    """
    Counts the number of potential "cheating" opportunities in a path.

    Args:
        path: List of (row, col) coordinates representing the full path
        max_distance: Maximum Manhattan distance allowed between two points
        threshold: Minimum path length savings required to count as a cheat
    """
    result = 0
    # Compare each point with all subsequent points in the path
    for a in range(len(path)- 1):
        r1, c1 = path[a]
        for b in range(a + 1, len(path)):  # start from a+1 to avoid redundant checks
            r2, c2 = path[b]
            # Calculate Manhattan distance between points
            distance = abs(r1 - r2) + abs(c1 - c2)
            # Skip if points are too far apart
            if distance > max_distance:
                continue

            # Calculate how many steps would be saved by "cheating"
            # b-a is the number of steps in the original path
            # distance is the direct path length
            # The difference represents potential steps saved
            savings = b - a - distance

            # Count this as a cheat if savings meets the threshold
            if savings >= threshold:
                result += 1
    return result


def part1(input_file: str, max_distance: int, threshold: int) -> int:
    grid, start, end = read_input(input_file)
    path = find_path(grid, start, end)
    result = count_cheats(path, max_distance, threshold)
    return result


def part2(input_file: str, max_distance: int, threshold: int) -> int:
    grid, start, end = read_input(input_file)
    path = find_path(grid, start, end)
    result = count_cheats(path, max_distance, threshold)
    return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename, max_distance=2, threshold=20) == 5
    print("Part 1 OK")

    assert part2(filename, max_distance=20, threshold=76) == 3
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename, max_distance=2, threshold=100)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename, max_distance=20, threshold=100)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 1293
    assert solution_part2 == 977747


if __name__ == "__main__":
    test()
    main()
