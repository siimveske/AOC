import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    instructions = []
    with open(input_file_path, 'r') as f:
        for line in f:
            cmd, val = line.split(' ')
            instructions.append((cmd, int(val)))

    return instructions


def part1(inputFile: str):

    instructions = readInput(inputFile)

    x, depth = 0, 0
    for cmd, val in instructions:
        if cmd == 'forward':
            x += val
        elif cmd == 'down':
            depth += val
        else:
            depth -= val

    return x * depth


def part2(inputFile: str):

    instructions = readInput(inputFile)

    x, depth, aim = 0, 0, 0
    for cmd, val in instructions:
        if cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
        else:
            x += val
            depth += (aim * val)

    return x * depth


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 150
    print('Part 1 OK')
    assert part2(filename) == 900
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
