import os


def read_input(filename: str) -> list[list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    joltage_list = []

    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            joltage_list.append([int(i) for i in line])

    return joltage_list


def part1(input_file: str) -> int:
    joltage_list = read_input(input_file)
    total_joltage = 0

    for joltages in joltage_list:
        max_joltage = 0
        for i in range(len(joltages) - 1):
            first_digit = joltages[i]
            second_digit = max(joltages[i + 1:])
            combined = int(str(first_digit) + str(second_digit))
            max_joltage = max(max_joltage, combined)

        total_joltage += max_joltage

    return total_joltage


def part2(input_file: str) -> int:
    joltage_list = read_input(input_file)
    total_joltage = 0

    for joltages in joltage_list:
        digits = []
        current_index = 0

        # Extract 12 digits by finding max in sliding window
        for _ in range(12):
            remaining = 12 - len(digits)
            window_end = len(joltages) - (remaining - 1)
            window = joltages[current_index:window_end]

            max_digit = max(window)
            digits.append(max_digit)

            # Move index past the max digit found
            current_index += window.index(max_digit) + 1

        joltage = int(''.join(str(d) for d in digits))
        total_joltage += joltage

    return total_joltage


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 357
    print('Part 1 OK')

    assert part2(filename) == 3121910778619
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 17554
    assert solution_part2 == 175053592950232


if __name__ == '__main__':
    test()
    main()
