import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


def parse(data: str) -> tuple[int, int, int]:
    l, w, h = data.split('x')
    return (int(l), int(w), int(h))


def area(dimensions: tuple[int, int, int]) -> int:
    l, w, h = dimensions
    area1 = l * w
    area2 = w * h
    area3 = l * h

    extra = min(area1, area2, area3)
    total_area = (2 * area1) + (2 * area2) + (2 * area3)

    return total_area + extra


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    total_area = 0
    for line in data:
        dimensions = parse(line)
        total_area += area(dimensions)
    return total_area


def part2(inputFile: str):
    instructions = readInput(inputFile)


def test():
    print('---- TEST ----')

    assert area(parse('2x3x4')) == 58
    assert area(parse('1x1x10')) == 43
    print('Part 1 OK')

    # assert part2(filename) == 12
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
