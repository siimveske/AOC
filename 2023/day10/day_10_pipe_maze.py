from collections import defaultdict, deque
import os


def read_input(filename: str) -> list[list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        data = [l.strip() for l in f]

    graph = defaultdict(list)
    start = None
    rows = len(data)
    cols = len(data[0])

    for r_idx, row in enumerate(data):
        for c_idx, node in enumerate(row):
            current_node = (r_idx, c_idx)

            up = r_idx - 1
            up_node = data[up][c_idx] if up >= 0 else None
            down = r_idx + 1
            down_node = data[down][c_idx] if down < rows else None
            left = c_idx - 1
            left_node = data[r_idx][left] if left >= 0 else None
            right = c_idx + 1
            right_node = data[r_idx][right] if right < cols else None

            valid_up_nodes = ['S', '|', 'F', '7']
            valid_down_nodes = ['S', '|', 'L', 'J']
            valid_left_nodes = ['S', 'F', 'L', '-']
            valid_right_nodes = ['S', '7', 'J', '-']

            if node == 'S':
                start = current_node
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == '|':
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == '-':
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == 'F':
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == '7':
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))
                if down_node and down_node in valid_down_nodes:
                    graph[current_node].append((down, c_idx))
            elif node == 'L':
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if right_node and right_node in valid_right_nodes:
                    graph[current_node].append((r_idx, right))
            elif node == 'J':
                if up_node and up_node in valid_up_nodes:
                    graph[current_node].append((up, c_idx))
                if left_node and left_node in valid_left_nodes:
                    graph[current_node].append((r_idx, left))

    return start, graph


def part1(input_file: str) -> int:
    start, graph = read_input(input_file)

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
    pass

def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 4

    filename = "test_input2.txt"
    assert part1(filename) == 8

    print("Part 1 OK")

    # assert part2(filename) == 2
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 6875
    # assert solution_part2 == 957


if __name__ == "__main__":
    test()
    main()
