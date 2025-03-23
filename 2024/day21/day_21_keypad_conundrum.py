import os
from collections import deque
from functools import cache
from itertools import pairwise

"""
Original solution by: mgtezak
https://github.com/mgtezak/Advent_of_Code/blob/master/2024/21/p2.py
"""

def read_input(filename: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        codes = file.read().strip().split("\n")
    return codes


N_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}
D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}
PADS = [N_PAD, D_PAD]


def bfs(start: str, target: str, graph: dict) -> list[str]:
    """Find all shortest paths from start to target in graph.

    Args:
        start: Starting node
        target: Target node
        graph: Dictionary representing the graph where values are lists of (node, direction) tuples

    Returns:
        List of paths represented as strings of directions
    """
    queue = deque([(start, [], {start})])
    shortest_length = None
    paths = []

    while queue:
        current, path, visited = queue.popleft()

        # Found target - record path if it's shortest
        if current == target:
            if shortest_length is None:
                shortest_length = len(path)
            if len(path) == shortest_length:
                paths.append("".join(path + ["A"]))
            continue

        # Skip if path is longer than shortest known path
        if shortest_length is not None and len(path) >= shortest_length:
            continue

        # Explore neighbors
        for neighbor, direction in graph[current]:
            if neighbor not in visited:
                queue.append((
                    neighbor,
                    path + [direction],
                    visited | {neighbor}
                ))

    return paths


@cache
def dfs(sequence: str, recursion_depth: int, pad_index: int = 0) -> int:
    """Calculate minimum path length through a sequence of nodes with nested recursion.

    Args:
        sequence: String of nodes to traverse
        recursion_depth: Number of recursive levels to process
        pad_index: Index of pad configuration to use (0=N_PAD, 1=D_PAD)

    Returns:
        Minimum total path length through the sequence
    """
    pad = PADS[pad_index]
    total_length = 0
    full_sequence = "A" + sequence  # Ensure sequence starts from A

    # Process each consecutive pair of nodes
    for current, next_node in pairwise(full_sequence):
        # Find all possible paths between current pair of nodes
        possible_paths = bfs(current, next_node, pad)

        if recursion_depth == 0:
            # Base case: add minimum path length
            total_length += min(len(path) for path in possible_paths)
        else:
            # Recursive case: find minimum length through nested paths
            total_length += min(
                dfs(path, recursion_depth - 1, 1)
                for path in possible_paths
            )

    return total_length

def part1(input_file: str) -> int:
    total = 0
    codes = read_input(input_file)
    for code in codes:
        keycode_number = int(code[:-1])
        min_sequence_length = dfs(code, 2)
        total += min_sequence_length * keycode_number
    return total


def part2(input_file: str) -> int:
    total = 0
    codes = read_input(input_file)
    for code in codes:
        keycode_number = int(code[:-1])
        min_sequence_length = dfs(code, 25)
        total += min_sequence_length * keycode_number
    return total


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 126384
    print("Part 1 OK")

    assert part2(filename) == 154115708116294
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 176650
    assert solution_part2 == 217698355426872


if __name__ == "__main__":
    test()
    main()
