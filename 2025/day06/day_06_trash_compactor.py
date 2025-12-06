import os


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def part1(input_file: str) -> int:
    # Read the input file into a list of strings, one for each line.
    data = read_input(input_file)
    # Split each line by whitespace to create a 2D list (list of lists).
    data = [line.split() for line in data]
    # Transpose the data. This swaps rows and columns, so we can iterate
    # through the original columns of the input file.
    # For example:
    # [['1', '4'],      => [('1', '2', '3', '+'),
    #  ['2', '5'],           ('4', '5', '6', '*')]
    #  ['3', '6'],
    #  ['+', '*']]
    transposed_data = list(zip(*data))

    total = 0
    # Iterate through each column from the original data.
    # The last item in each transposed tuple is the operator, and the rest are numbers.
    for *args, op in transposed_data:
        # Join the numbers with the operator to form a mathematical expression string.
        # e.g., ('1', '2', '3', '+') becomes "1+2+3"
        expression = op.join(args)
        # Evaluate the expression string and add the result to the total.
        total += eval(expression)
    return total


def evaluate_expression(nums, operator) -> int:
    if nums:
        return eval(operator.join(nums))
    return 0


def part2(input_file: str) -> int:
    # Read all lines from the file.
    lines = read_input(input_file)
    # Transpose the input character by character, without splitting by whitespace first.
    # This allows reading the file "vertically".
    transposed = list(zip(*lines))

    total = 0
    numbers = []  # Stores numbers for the current expression group.
    active_op = ""  # Stores the operator for the current group.

    # Iterate through each vertical column of characters.
    for *digits, op in transposed:
        # Join the characters in the upper part of the column to form a number string.
        num = "".join(digits).strip()
        # The last character of the column is the potential operator.
        op = op.strip()

        # If there's a non-whitespace operator, it becomes the active one.
        if op:
            active_op = op

        # If a number was formed from the column, add it to the current group.
        if num:
            numbers.append(num)
        else:
            # An empty 'num' means a blank column, which acts as a separator.
            # Evaluate the expression for the completed group and add to total.
            total += evaluate_expression(numbers, active_op)
            # Reset for the next group of numbers.
            numbers = []

    # After the loop, evaluate any remaining numbers in the last group.
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
