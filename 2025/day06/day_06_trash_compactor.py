import re
import os


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def parse1(lines: list[str]) -> list:
    number_pattern = r"\d+"
    operands_pattern = r"[\+\-\*\/]"

    operators = lines.pop(-1)  # remove last line with operators
    operators = re.findall(operands_pattern, operators)
    math_problems = []

    for line in lines:
        numbers = re.findall(number_pattern, line)
        math_problems.append(numbers)

    math_problems.append(operators)

    return math_problems


def part1(input_file: str) -> int:
    data = read_input(input_file)
    math_problems = parse1(data)
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
    math_problems = read_input(input_file)
    operators = math_problems.pop(-1)
    operands = re.findall(r"[\+\*]", operators)
    idx_operator = 0

    # transpose math_problems matrix
    transposed = list(map(list, zip(*math_problems)))

    total = 0
    numbers = []
    for line in transposed:
        number = "".join(line).strip()
        if number.isdigit():
            numbers.append(number)
            continue

        operator = operands[idx_operator]
        idx_operator += 1
        expression = operator.join(numbers)
        total += eval(expression)
        numbers = []

    operator = operands[idx_operator]
    idx_operator += 1
    expression = operator.join(numbers)
    total += eval(expression)
    numbers = []

    return total


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == 4277556
    print("Part 1 OK")

    assert part2(filename) == 3263827
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 4648618073226
    assert solution_part2 == 7329921182115


if __name__ == "__main__":
    test()
    main()
