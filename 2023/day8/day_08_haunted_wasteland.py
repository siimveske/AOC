import os
from collections import deque


def read_input(filename: str) -> tuple[deque[str], dict[str, tuple[str, str]]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    with open(input_file_path, 'r') as f:
        cmd, path = f.read().split('\n\n')
        cmd = deque([i for i in cmd])
        for line in path.split('\n'):
            node = line[0:3]
            left = line[7:10]
            right = line[12:15]
            graph[node] = (left, right)
    return cmd, graph


def part1(input_file: str) -> int:
    cmd, graph = read_input(input_file)
    result = 0
    location = 'AAA'
    while location != 'ZZZ':
        location = graph[location][0] if cmd[0] == 'L' else graph[location][1]
        result += 1
        cmd.rotate(-1)
    return result


def part2(input_file: str) -> int:
    bets = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 6
    print('Part 1 OK')

    # assert part2(filename) == 5905
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 18727
    # assert solution_part2 == 254837398


if __name__ == '__main__':
    test()
    main()
