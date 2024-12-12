import os


def read_input(filename: str) -> tuple[list[int], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        pass


def part1(input_file: str) -> int:
    return 0


# def part2(input_file: str) -> int:
#     pass

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 11
    print('Part 1 OK')

    # assert part2(filename) == 31
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 1765812
    # assert solution_part2 == 20520794


if __name__ == '__main__':
    test()
    main()
