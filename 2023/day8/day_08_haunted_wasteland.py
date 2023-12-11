import os
from itertools import cycle


def read_input(filename: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    with open(input_file_path, 'r') as f:
        directions, path = f.read().split('\n\n')
        directions = [int(i == 'R') for i in directions]
        for line in path.split('\n'):
            node, left, right = line[0:3], line[7:10], line[12:15]
            graph[node] = (left, right)
    return directions, graph


def part1(input_file: str) -> int:
    directions, graph = read_input(input_file)
    result = 0
    location = 'AAA'
    for direction in cycle(directions):
        location = graph[location][direction]
        result += 1
        if location == 'ZZZ':
            break
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
