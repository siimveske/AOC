import itertools
from operator import add, mul
import os
import re


def read_input(filename: str) -> list[list[int]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    equations = []
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            numbers = [int(i) for i in re.findall(r'\d+', line)]
            equations.append(numbers)
    return equations

def calculate_total(equations: list[list[int]], ops: list) -> int:
    cache = {}
    total = 0

    for equation in equations:
        expected_result, arguments = equation[0], equation[1:]
        num_of_operations = len(arguments) - 1
        if num_of_operations not in cache:
            cache[num_of_operations] = list(itertools.product(ops, repeat=num_of_operations))

        for operations in cache[num_of_operations]:
            test_result = operations[0](arguments[0], arguments[1])
            for i in range(1, num_of_operations):
                test_result = operations[i](test_result, arguments[i+1])

            if test_result == expected_result:
                total += expected_result
                break

    return total

def join(a, b):
    return int(f'{a}{b}')

def part1(input_file: str) -> int:
    equations = read_input(input_file)
    total = calculate_total(equations, [add, mul])
    return total

def part2(input_file: str) -> int:
    equations = read_input(input_file)
    total = calculate_total(equations, [add, mul, join])
    return total

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 3749
    print('Part 1 OK')

    assert part2(filename) == 11387
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 7710205485870
    assert solution_part2 == 20928985450275


if __name__ == '__main__':
    test()
    main()
