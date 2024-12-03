import os
import re


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def find_multiplications(input_string: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_string)
    return matches

def part1(input_file: str) -> int:
    memory = read_input(input_file)
    total = 0
    for line in memory:
        for a, b in find_multiplications(line):
            total += int(a) * int(b)
    return total

# def part2(input_file: str) -> int:
#     reports = read_input(input_file)
#     safe_reports = get_safe_reports2(reports)
#     result = len(safe_reports)
#     return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 161
    print('Part 1 OK')

    # assert part2(filename) == 4
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 178794710
    # assert solution_part2 == 436


if __name__ == '__main__':
    test()
    main()
