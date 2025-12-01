import hashlib
from collections import deque


def find_all_paths(code: str) -> list[str]:
    """
    Find all paths from top left grid to bottom right grid.
    """
    rows, cols = [4, 4]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    direction_chars = {(0, -1): 'U', (0, 1): 'D', (-1, 0): 'L', (1, 0): 'R'}
    open_doors = set("bcdef")
    queue = deque([(0, 0, '')])  # (x, y, path)

    paths = []
    while queue:
        x, y, path = queue.popleft()

        if x == cols - 1 and y == rows - 1:
            paths.append(path)
            continue

        # generate md5 hash
        seed = code + path
        hash_value = hashlib.md5(seed.encode()).hexdigest()

        # check doors
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if (0 <= nx < cols) and (0 <= ny < rows) and hash_value[i] in open_doors:
                direction_char = direction_chars[(dx, dy)]
                queue.append((nx, ny, path + direction_char))

    return paths


def find_shortest_path(paths: list[str]) -> str:
    """
    Find shortest path from list of paths.
    """
    # return min(paths, key=len)
    return paths[0]


def find_longest_path(paths: list[str]) -> str:
    """
    Find longest path from list of paths.
    """
    # return max(paths, key=len)
    return paths[-1]


def part1(input_code: str) -> str:
    paths = find_all_paths(input_code)
    shortest_path = find_shortest_path(paths)
    return shortest_path


def part2(input_code: str) -> int:
    paths = find_all_paths(input_code)
    longest_path = find_longest_path(paths)
    return len(longest_path)


def test():
    print("---- TEST ----")

    assert part1("ihgpwlah") == "DDRRRD"
    assert part1("kglvqrro") == "DDUDRLRRUDRD"
    assert part1("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"

    assert part2("ihgpwlah") == 370
    assert part2("kglvqrro") == 492
    assert part2("ulqzkmiv") == 830

    print("OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1("vkjiggvb")
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2("vkjiggvb")
    print(f"Solution for Part 2: {solution_part2}")

    assert solution_part1 == "RDRRULDDDR"
    assert solution_part2 == 392

if __name__ == "__main__":
    test()
    main()
