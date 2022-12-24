import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, 'r') as f:
        for line in f:
            row = [character for character in line.strip()]
            grid.append(row)
    return grid


def part1(inputFile: str) -> int:
    grid = readInput(inputFile)


def part2(inputFile: str):
    grid = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 31
    print('Part 1 OK')

    # assert part2(filename) == 29
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 528
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # # assert solution_part2 == 14106266886
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
