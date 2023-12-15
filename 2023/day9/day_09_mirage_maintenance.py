import os


def read_input(filename: str) -> list[list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            numbers = [int(i) for i in line.split()]
            data.append(numbers)
    return data


def part1(input_file: str) -> int:
    data = read_input(input_file)
    total = 0

    for line in data:
        sequence = [line]

        while True:
            differences = [sequence[-1][i + 1] - sequence[-1][i] for i in range(len(sequence[-1]) - 1)]

            if all(diff == 0 for diff in differences):
                cumulative_sum = [0]
                while sequence:
                    last_element = sequence.pop()[-1]
                    cumulative_sum.append(cumulative_sum[-1] + last_element)
                total += cumulative_sum[-1]
                break
            else:
                sequence.append(differences)

    return total


def part2(input_file: str) -> int:
    data = read_input(input_file)
    total = 0

    for line in data:
        sequence = [line]

        while True:
            differences = [sequence[-1][i + 1] - sequence[-1][i] for i in range(len(sequence[-1]) - 1)]

            if all(diff == 0 for diff in differences):
                cumulative_sum = [0]
                while sequence:
                    first_element = sequence.pop()[0]
                    cumulative_sum.append(first_element + (-1 * cumulative_sum[-1]))
                total += cumulative_sum[-1]
                break
            else:
                sequence.append(differences)

    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 114
    print('Part 1 OK')

    assert part2(filename) == 2
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1953784198
    assert solution_part2 == 957


if __name__ == '__main__':
    test()
    main()
