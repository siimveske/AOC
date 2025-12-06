import re
import os


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    math_problems = []
    with open(input_file_path, 'r') as f:
        number_pattern = r"\d+"
        operands_pattern = r"[\+\-\*\/]"
        lines = f.readlines()

        operators = lines.pop(-1)  # remove last line with operators
        operators = re.findall(operands_pattern, operators)

        for line in lines:
            numbers =re.findall(number_pattern, line)
            math_problems.append(numbers)

        math_problems.append(operators)

    return math_problems


def part1(input_file: str) -> int:
    math_problems = read_input(input_file)
    operands = math_problems.pop(-1)
    total = 0
    rows = len(math_problems)
    cols = len(math_problems[0])

    for col in range(cols):
        col_values = []
        for row in range(rows):
            col_values.append(math_problems[row][col])
        expression = operands[col].join(col_values)
        total += eval(expression)
    return total


def part2(input_file: str) -> int:
    ranges, _ = read_input(input_file)
    merged = merge_ranges(ranges)

    # Calculate the total count of fresh ingredient IDs from merged ranges
    fresh_id_cnt = 0
    for start, end in merged:
        range_size = (end - start) + 1
        fresh_id_cnt += range_size

    return fresh_id_cnt


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 4277556
    print('Part 1 OK')

    # assert part2(filename) == 14
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 4648618073226
    # assert solution_part2 == 333892124923577


if __name__ == '__main__':
    test()
    main()
