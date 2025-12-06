import os


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def part1(input_file: str) -> int:
    data = read_input(input_file)
    data = [line.split() for line in data]
    transposed_data = list(zip(*data))

    total = 0
    for *args, op in transposed_data:
        expression = op.join(args)
        total += eval(expression)
    return total


def evaluate_expression(nums, operator) -> int:
    if nums:
        return eval(operator.join(nums))
    return 0


def part2(input_file: str) -> int:
    lines = read_input(input_file)
    transposed = list(zip(*lines))

    total = 0
    numbers = []
    active_op = ""
    # Read vertically
    for *digits, op in transposed:
        num = "".join(digits).strip()
        op = op.strip()

        if op:
            active_op = op

        if num:
            numbers.append(num)
        else:
            total += evaluate_expression(numbers, active_op)
            numbers = []

    # Process remaining numbers
    total += evaluate_expression(numbers, active_op)

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
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 4648618073226
    assert solution_part2 == 7329921182115


if __name__ == "__main__":
    test()
    main()
