from collections import deque
import os


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    grid = []
    start = None
    with open(file_path, 'r') as file:
        raw_map, moves = file.read().split("\n\n")

        # parse map
        _map = raw_map.split("\n")
        for r, line in enumerate(_map):
            grid.append(list(line))
            if start:
                continue
            for c, char in enumerate(line):
                if char == "@":
                    start = (r, c)

        # parse moves
        moves_dict = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        cmds = []
        for move in moves:
            if move in moves_dict:
                cmds.append(moves_dict[move])

    return grid, cmds, start


def part1(input_file: str) -> int:
    grid, cmds, start = read_input(input_file)
    queue = deque(cmds)

    r, c = start
    while queue:
        dr, dc = queue.popleft()
        next_r, next_c = r + dr, c + dc

        if grid[next_r][next_c] == "#":
            continue

        if grid[next_r][next_c] == ".":
            grid[next_r][next_c] = "@"
            grid[r][c] = "."
            r, c = next_r, next_c
            continue

        if grid[next_r][next_c] == "O":
            stack = []
            a, b = next_r, next_c
            while grid[a][b] == "O":
                stack.append((a, b))
                a, b = a + dr, b + dc
            if grid[a][b] == "#":
                continue
            else:
                while stack:
                    a, b = stack.pop()
                    grid[a+dr][b+dc] = "O"
                grid[next_r][next_c] = "@"
                grid[r][c] = "."
                r, c = next_r, next_c

    total = 0
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "O":
                total += 100*r+c
    return total


# def part2(input_file: str) -> int:
#     configurations = read_input(input_file)

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 2028

    filename = 'test_input2.txt'
    assert part1(filename) == 10092
    print('Part 1 OK')

    # assert part2(filename) == 875318608908
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1517819
    # assert solution_part2 == 102718967795500


if __name__ == '__main__':
    test()
    main()
