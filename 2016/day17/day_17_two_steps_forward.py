import hashlib
from collections import deque


def find_shortest_path(code: str) -> str:
    """
    Find shortest path from top left grid to bottom right grid.
    """
    rows, cols = [4, 4]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    direction_chars = {(0, -1): 'U', (0, 1): 'D', (-1, 0): 'L', (1, 0): 'R'}
    open_doors = set("bcdef")
    queue = deque([(0, 0, '')])  # (x, y, path)

    while queue:
        x, y, path = queue.popleft()

        if x == cols - 1 and y == rows - 1:
            return path

        # generate md5 hash
        seed = code + path
        hash_value = hashlib.md5(seed.encode()).hexdigest()

        # check doors
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if (0 <= nx < cols) and (0 <= ny < rows) and hash_value[i] in open_doors:
                direction_char = direction_chars[(dx, dy)]
                queue.append((nx, ny, path + direction_char))

    return ""

def test():
    print("---- TEST ----")

    assert find_shortest_path("ihgpwlah") == "DDRRRD"
    assert find_shortest_path("kglvqrro") == "DDUDRLRRUDRD"
    assert find_shortest_path("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"

    print("OK")


def main():
    print("---- MAIN ----")

    solution_part1 = find_shortest_path("vkjiggvb")
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = solve(initial_state="10011111011011001", disk_length=35651584)
    # print(f"Solution for Part 2: {solution_part2}")

    assert solution_part1 == "RDRRULDDDR"
    # assert solution_part2 == "01101100001100100"

if __name__ == "__main__":
    test()
    main()
