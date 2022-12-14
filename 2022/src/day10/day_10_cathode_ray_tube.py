import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    commands = []
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line == 'noop':
                commands.append(('noop', 0))
            else:
                cmd, val = line.split()
                commands.append((cmd, int(val)))
    return commands


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)
    checkpoints = [20, 60, 100, 140, 180, 220]
    signals = []

    cmd_idx = 0
    pause = 0
    register = 1
    val = 0
    for i in range(1, 221):
        if i in checkpoints:
            signal = i * register
            signals.append(signal)
        if pause > 0:
            pause -= 1
            register += val
            val = 0
            continue

        cmd = commands[cmd_idx][0]
        val = commands[cmd_idx][1]
        if cmd == 'addx':
            pause = 1

        cmd_idx += 1

    return sum(signals)


def part2(inputFile: str):
    commands = readInput(inputFile)

    cmd_idx = 0
    pause = 0
    register = 1
    val = 0
    for i in range(1, 241):
        sprite = range(register, register + 3)
        if i in sprite:
            print('#', end='')
        else:
            print('.', end='')
        if i % 40 == 0:
            print('')
        if pause > 0:
            pause -= 1
            register += val
            val = 0
            continue

        cmd = commands[cmd_idx][0]
        val = commands[cmd_idx][1]
        if cmd == 'addx':
            pause = 1

        cmd_idx += 1


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13140
    print('Part 1 OK')

    assert part2(filename) == 1
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 12640
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    #assert solution_part2 == 2303
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
