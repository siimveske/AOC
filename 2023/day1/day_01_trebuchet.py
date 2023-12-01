import os


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
    numbers = {'one': '1',
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
        new_line = []
        for idx, letter in enumerate(line):
            if letter.isdigit():
                new_line.append(letter)
                continue
            for key, value in numbers.items():
                if line[idx:].startswith(key):
                    new_line.append(value)
                    break
        transformed_lines.append(''.join(new_line))

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

    assert solution_part1 == 55172
    assert solution_part2 == 54925


if __name__ == '__main__':
    test()
    main()
