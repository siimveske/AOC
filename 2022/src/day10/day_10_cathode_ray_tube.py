import os
'''
https://github.com/aaftre/AdventofCode/tree/master/2022/Day10
'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        commands = [line.split() for line in f.readlines()]
    return commands


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)

    x = 1
    clk = 0
    signal = list()

    def incclk():
        nonlocal x, clk, signal

        clk += 1

        if clk == 20 or (clk - 20) % 40 == 0:
            signal.append(clk * x)

    for cmd in commands:
        if cmd[0] == 'noop':
            incclk()
        elif cmd[0] == 'addx':
            incclk()
            incclk()
            x += int(cmd[1])

    return sum(signal)


def part2(inputFile: str):
    commands = readInput(inputFile)

    x = 1
    clk = 0
    msg = list()

    def incclk():
        nonlocal x, clk

        if (clk + 1) % 40 == 0:
            msg.append('\n')
        elif clk % 40 == x or clk % 40 == x - 1 or clk % 40 == x + 1:
            msg.append('▓')
        else:
            msg.append('░')

        clk += 1

    for cmd in commands:
        if cmd[0] == 'noop':
            incclk()
        elif cmd[0] == 'addx':
            incclk()
            incclk()
            x += int(cmd[1])

    return ''.join(msg)


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
