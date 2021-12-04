import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        report = [line.strip() for line in f.readlines()]

    return report


def part1(inputFile: str):

    report = readInput(inputFile)

    gamma_rate = ''
    epsilon_rate = ''
    for col in range(len(report[0])):
        cnt_0 = 0
        cnt_1 = 0
        for row in range(len(report)):
            if report[row][col] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1
        if cnt_0 > cnt_1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


def part2(inputFile: str):

    instructions = readInput(inputFile)

    x, depth, aim = 0, 0, 0
    for cmd, val in instructions:
        if cmd == 'up':
            aim -= val
        elif cmd == 'down':
            aim += val
        elif cmd == 'forward':
            x += val
            depth += (aim * val)

    return x * depth


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 198
    print('Part 1 OK')
    # assert part2(filename) == 900
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
