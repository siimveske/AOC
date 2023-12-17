import os
from collections import defaultdict, deque


def read_input(filename: str) -> tuple[tuple[int, int], defaultdict[tuple[int, int], list[tuple[int, int]]], list[list[str]]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        grid = f.read().splitlines()
        grid = [[*line] for line in grid]

    graph = defaultdict(list)
    start = None
    rows = len(grid)
    cols = len(grid[0])

    for r_idx, row in enumerate(grid):
        for c_idx, node in enumerate(row):
            current_node = (r_idx, c_idx)

            up = r_idx - 1
            up_node = grid[up][c_idx] if up >= 0 else None
            down = r_idx + 1
            down_node = grid[down][c_idx] if down < rows else None
            left = c_idx - 1
            left_node = grid[r_idx][left] if left >= 0 else None
            right = c_idx + 1
            right_node = grid[r_idx][right] if right < cols else None

            valid_up_nodes = ["S", "|", "F", "7"]
            valid_down_nodes = ["S", "|", "L", "J"]
            valid_left_nodes = ["S", "F", "L", "-"]
            valid_right_nodes = ["S", "7", "J", "-"]

            if node == "S":
                start = current_node
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == "|":
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == "-":
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == "F":
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == "7":
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == "L":
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == "J":
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))

    return start, graph, grid


def part1(input_file: str) -> int:
    start, graph, _ = read_input(input_file)

    visited = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return max(visited.values())


def part2(input_file: str) -> int:
    """
    reddit algorithm thread:
    https://www.reddit.com/r/adventofcode/comments/18fgddy/2023_day_10_part_2_using_a_rendering_algorithm_to/
    """
    start, graph, grid = read_input(input_file)

    # find the connected path from given graph
    path = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                path.add(neighbor)
                queue.append(neighbor)

    # Convert starting position S to a valid corner connector F,7,L or J
    start_row, start_col = start
    is_left_connected = grid[start_row][start_col - 1] in ["F", "L", "-"]
    is_right_connected = grid[start_row][start_col + 1] in ["7", "J", "-"]
    is_up_connected = grid[start_row - 1][start_col] in ["|", "F", "7"]
    is_down_connected = grid[start_row + 1][start_col] in ["|", "L", "J"]

    if is_down_connected and is_right_connected:
        grid[start_row][start_col] = 'F'
    elif is_left_connected and is_down_connected:
        grid[start_row][start_col] = '7'
    elif is_up_connected and is_right_connected:
        grid[start_row][start_col] = 'L'
    elif is_up_connected and is_left_connected:
        grid[start_row][start_col] = 'J'
    else:
        raise Exception("Failed to convert start location into a connector")

    # scan map line by line from left to right to find points that are inside the borders
    inside_points = []
    for row, line in enumerate(grid):
        left_border_count = 0
        for col, node in enumerate(line):
            node_location = (row, col)
            # smart reddit people found out that if we scan from top to bottom only
            # connectors that connect from top should be counted as border
            if node_location in path and node in ['|', 'L', 'J']:
                left_border_count += 1
                continue
            # apparently odd border count means that current point is inside the path
            if (node_location not in path) and (left_border_count % 2 != 0):
                inside_points.append((row, col))

    return len(inside_points)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 4
    filename = "test_input2.txt"
    assert part1(filename) == 8

    print("Part 1 OK")

    filename = "test_input3.txt"
    assert part2(filename) == 4
    filename = "test_input4.txt"
    assert part2(filename) == 4
    filename = "test_input5.txt"
    assert part2(filename) == 8

    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 6875
    assert solution_part2 == 471


if __name__ == "__main__":
    test()
    main()
