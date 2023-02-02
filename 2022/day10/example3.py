import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]


def part1(inputFile: str) -> int:
    lines = readInput(inputFile)
    X = 1
    cycles = 0
    signal_strengths = {}

    for line in lines:
        line = line.split()

        if line[0] == "noop":
            cycles += 1
            signal_strengths[cycles] = X * cycles

        elif line[0] == "addx":
            cycles += 1
            signal_strengths[cycles] = X * cycles

            cycles += 1
            signal_strengths[cycles] = X * cycles
            X += int(line[1])

    req_sum = sum(signal_strengths.get(i, 0) for i in range(20, 221, 40))
    return req_sum


def update_pixels(X, cycles, pixels):
    """Draws pixels if the sprite's horizontal position (X) puts its pixels
    where the CRT is currently drawing."""
    pos = (cycles - 1) % 40
    if pos in {X - 1, X, X + 1}:
        pixels[cycles - 1] = '▓'


def part2(inputFile: str):
    lines = readInput(inputFile)

    X = 1
    cycles = 0
    pixels = list("░" * 40 * 6)

    for line in lines:
        line = line.split()

        if line[0] == "noop":
            cycles += 1
            update_pixels(X, cycles, pixels)

        elif line[0] == "addx":
            cycles += 1
            update_pixels(X, cycles, pixels)

            cycles += 1
            update_pixels(X, cycles, pixels)
            X += int(line[1])

    result = ""
    for i in range(0, 201, 40):
        result += "".join(pixels[i: i + 40])
        result += "\n"
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13140
    print('Part 1 OK')

    #assert part2(filename) == 1
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 12640
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    #assert solution_part2 == EHBZLRJR
    print(f'Solution for Part 2: \n{solution_part2}')


if __name__ == '__main__':
    test()
    main()
