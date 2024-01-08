import os
import sys

sys.setrecursionlimit(5000)


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        grid = f.read().splitlines()
    return grid


def walk(pos, end, grid, size, visited, memo):
    row, col = pos

    if pos == end:
        return 0
    if pos in visited:
        return -float('inf')
    if pos in memo:
        return memo[pos]

    visited.add(pos)

    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    next_locations = []
    if up > 0:
        if grid[up][col] in '.^':
            next_locations.append((up, col))
    if down < size:
        if grid[down][col] in '.v':
            next_locations.append((down, col))
    if left > 0:
        if grid[row][left] in '.<':
            next_locations.append((row, left))
    if right < size:
        if grid[row][right] in '.>':
            next_locations.append((row, right))

    distances = [1 + walk(loc, end, grid, size, set(visited), memo) for loc in next_locations]

    max_distance = max(distances)
    memo[pos] = max_distance

    return max_distance


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    size = len(grid)
    start = (0, 1)
    end = (size - 1, size - 2)
    visited = set()
    memo = {}
    result = walk(start, end, grid, size, visited, memo)
    return result


def part2(input_file: str) -> int:
    # https://www.youtube.com/watch?v=NTLYL7Mg2jU

    grid = read_input(input_file)
    length = len(grid)
    start = (0, 1)
    stop = (length - 1, length - 2)

    # Find junction poits (points with more than 2 neighbors)
    points = {start, stop}
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == '#':
                continue
            # Count neighbors
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (0 <= nr < length) and (0 <= nc < length) and grid[nr][nc] != '#':
                    neighbors += 1
            if neighbors >= 3:
                points.add((r, c))

    # Build an adjacency graph
    graph = {pt: {} for pt in points}
    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}
        while stack:
            n, r, c = stack.pop()
            if n != 0 and (r, c) in points:  # We have found a distance between two adjacent junction points
                graph[(sr, sc)][(r, c)] = n
                continue

            # Calculate distances between junction points
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < length) and (0 <= nc < length) and (grid[nr][nc] != '#') and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    # Find the longest path
    seen = set()
    def dfs(pt):
        if pt == stop:
            return 0
        m = -float('inf')

        # Lock this point for this path
        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, graph[pt][nx] + dfs(nx))  # graph[pt][nx] means distance from pt to nx
        # Release the point for next path
        seen.remove(pt)

        return m

    result = dfs(start)
    return result


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'

    assert part1(filename) == 94
    print('Part 1 OK')

    assert part2(filename) == 154
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 2154
    assert solution_part2 == 6654


if __name__ == '__main__':
    test()
    main()
