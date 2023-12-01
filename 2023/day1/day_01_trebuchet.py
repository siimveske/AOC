import os
import math


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        lines = [n.strip() for n in f.readlines()]

    return lines


def get_first_number(line: str) -> str:
    for character in line:
        if character.isdigit():
            return character


def get_last_number(line: str) -> str:
    for character in line[::-1]:
        if character.isdigit():
            return character


def txt_to_number(raw_lines) -> list[str]:
    NUMBERS = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}
    transformed_lines = []

    for line in raw_lines:
        left_idx = math.inf
        right_idx = -math.inf
        left_word = ''
        right_word = ''
        first_left_digit = math.inf
        first_right_digit = -math.inf

        # find leftmost digit index
        for i, letter in enumerate(line):
            if letter.isnumeric() and i < first_left_digit:
                first_left_digit = i

        # find leftmost word
        for k, v in NUMBERS.items():
            result = line.find(k)
            if result != -1 and result < first_left_digit and result < left_idx:
                left_idx = result
                left_word = k
        if left_word:
            line = line.replace(left_word, NUMBERS[left_word], 1)

        # find rightmost digit index
        for i, letter in enumerate(line):
            if letter.isnumeric() and i > first_right_digit:
                first_right_digit = i

        # find rightmost word
        for k, v in NUMBERS.items():
            result = line.rfind(k)
            if result != -1 and result > first_right_digit and result > right_idx:
                right_idx = result
                right_word = k
        if right_word:
            line = line[::-1]
            reversed_old = right_word[::-1]
            line = line.replace(reversed_old, NUMBERS[right_word], 1)
            line = line[::-1]

        transformed_lines.append(line)

    return transformed_lines


def part1(input_file: str) -> int:
    lines = read_input(input_file)

    total = 0
    for line in lines:
        a = get_first_number(line)
        b = get_last_number(line)
        total += int(a + b)
    return total


def part2(input_file: str) -> int:
    raw_lines = read_input(input_file)
    lines = txt_to_number(raw_lines)

    total = 0
    for line in lines:
        a = get_first_number(line)
        b = get_last_number(line)
        total += int(a + b)
    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 142
    print('Part 1 OK')

    filename = 'test_input2.txt'
    assert part2(filename) == 281
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
