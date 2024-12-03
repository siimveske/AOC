import os
import re


def read_input(filename: str) -> str:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_operands(input_string: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_string)
    matches = [tuple(map(int, match)) for match in matches]
    return matches

def parse_tokens(input_string: str) -> list[str]:
    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, input_string)
    return matches

def multiply(tokens: str) -> int:
    do = True
    result = 0
    for token in tokens:
        if token == 'do()':
            do = True
        elif token == "don't()":
            do = False
        elif do:
            operand1, operand2 = parse_operands(token)[0]
            result += operand1 * operand2
    return result


def part1(input_file: str) -> int:
    total = 0
    memory = read_input(input_file)
    for operand1, operand2 in parse_operands(memory):
        total += operand1 * operand2
    return total

def part2(input_file: str) -> int:
    memory = read_input(input_file)
    tokens = parse_tokens(memory)
    total = multiply(tokens)
    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 161
    print('Part 1 OK')

    filename = 'test_input2.txt'
    assert part2(filename) == 48
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 178794710
    assert solution_part2 == 76729637


if __name__ == '__main__':
    test()
    main()
