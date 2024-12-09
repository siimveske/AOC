import os


def read_input(filename: str) -> list[list[str]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    with open(input_path, 'r') as file:
        pass

def part1(input_file: str) -> int:
    pass

def part2(input_file: str) -> int:
    pass

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1928
    print('Part 1 OK')

    # assert part2(filename) == 34
    # print('Part 2 OK')

def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 423
    # assert solution_part2 == 1287


if __name__ == '__main__':
    test()
    main()
