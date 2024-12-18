import os


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, 'r') as file:
        return file.read().splitlines()


def part1(input_file: str) -> int:
    data = read_input(input_file)
    result = 0
    return result


# def part2(input_file: str) -> int:
#     configurations = read_input(input_file)

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 480
    print('Part 1 OK')

    # assert part2(filename) == 875318608908
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 28753
    # assert solution_part2 == 102718967795500


if __name__ == '__main__':
    test()
    main()
