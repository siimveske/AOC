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


def tokens_to_vertices(tokens: list[tuple[str, int, str]]) -> tuple[list[tuple[int, int]], int]:
    vertices = []
    r, c = 0, 0
    perimeter = 0
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for token in tokens:
        direction, steps, color = token
        dr, dc = directions[direction]
        r += dr * steps
        c += dc * steps
        vertices.append((r, c))
        perimeter += steps

    return vertices, perimeter


def shoelace(vertices):
    """https://en.wikipedia.org/wiki/Shoelace_formula -> Triangle form"""
    xs, ys = zip(*vertices)
    left = sum(a * b for a, b in zip(xs, ys[1:]))
    right = sum(a * b for a, b in zip(ys, xs[1:]))

    area = abs(left - right) // 2
    return area


def part1(input_file: str) -> int:
    tokens = read_input(input_file)
    vertices, perimeter = tokens_to_vertices(tokens)

    # Pick's theorem - https://en.wikipedia.org/wiki/Pick%27s_theorem
    area = shoelace(vertices) + perimeter // 2 + 1
    return int(area)


def part2(input_file: str) -> int:
    graph, destination = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 62
    print('Part 1 OK')

    # assert part2(filename) == 94
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 47527
    # assert solution_part2 == 1215


if __name__ == '__main__':
    test()
    main()
