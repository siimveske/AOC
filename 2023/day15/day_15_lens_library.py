import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.readline().split(',')


def part1(input_file: str) -> int:
    data = read_input(input_file)
    result = 0
    for step in data:
        current_value = 0
        for character in step:
            current_value += ord(character)
            current_value *= 17
            current_value = current_value % 256
        result += current_value

    return result


def part2(input_file: str) -> int:
    lines = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1320
    print('Part 1 OK')

    # assert part2(filename) == 64
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 510792
    # assert solution_part2 == 87700


if __name__ == '__main__':
    test()
    main()
