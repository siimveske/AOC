import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read()

    return data


def climb(data: str) -> int:
    floor = 0
    op = {
        '(': 1,
        ')':-1 }
    for char in data:
        floor += op[char]

    return floor


def part1(inputFile: str):
    data = readInput(inputFile)
    return climb(data)


def part2(inputFile: str):
    data = readInput(inputFile)


def test():
    print('---- TEST ----')

    assert climb('(())') == 0
    assert climb('()()') == 0
    assert climb('(((') == 3
    assert climb('(()(()(') == 3
    assert climb('))(((((') == 3
    assert climb('())') == -1
    assert climb('))(') == -1
    assert climb(')))') == -3
    assert climb(')())())') == -3

    print('Part 1 OK')

    # assert part2(filename) == 45000
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
