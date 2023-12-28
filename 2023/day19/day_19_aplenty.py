import os


def read_input(filename: str) -> list[tuple[str, int, str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    tokens = []
    with open(input_file_path, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            direction, value, color = line.split()
            tokens.append((direction, int(value), color))
    return tokens


def part1(input_file: str) -> int:
    tokens = read_input(input_file)


def part2(input_file: str) -> int:
    tokens = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 19114
    print('Part 1 OK')

    # assert part2(filename) == 952408144115
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    #
    # assert solution_part1 == 47527
    # assert solution_part2 == 52240187443190


if __name__ == '__main__':
    test()
    main()
