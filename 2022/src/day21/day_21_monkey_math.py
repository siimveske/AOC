import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        coordinates = [*enumerate(int(i) for i in f)]
    return coordinates


def part1(inputFile: str):
    coordinates = readInput(inputFile)


def part2(inputFile: str):
    coordinates = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 152
    print('Part 1 OK')

    # assert part2(filename) == 1623178306
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # assert solution_part1 == 3346

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 4265712588168


if __name__ == '__main__':
    test()
    main()
