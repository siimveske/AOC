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

    h_pos = 0
    v_pos = 0

    for cmd, val in instructions:
        if cmd == 'forward':
            h_pos += val
        elif cmd == 'down':
            v_pos += val
        else:
            v_pos -= val

    return h_pos * v_pos


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 150
    print('Part 1 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')


if __name__ == '__main__':
    test()
    main()
