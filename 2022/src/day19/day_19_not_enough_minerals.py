import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        pass


def part1(inputFile: str):
    cubes = readInput(inputFile)


def part2(inputFile: str):
    cubes = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 64
    print('Part 1 OK')

    # assert part2(filename) == 58
    # print('Part 2 OK\n')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # assert solution_part1 == 4580

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part1 == 2610


if __name__ == '__main__':
    test()
    main()
