import os
from collections import defaultdict


def loadProgram(file: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    program = []
    with open(input_file_path, 'r') as file:
        for line in file:
            command, arg = line.split()
            program.append({'command': command, 'arg': int(arg)})

    return program


def executeProgram(program: list[dict]):
    i = 0
    acc = 0
    history = defaultdict(int)
    
    while i < len(program):
        command, arg = program[i].values()

        if history[i] > 0:
            return {'status': 'error', 'acc': acc}
        history[i] += 1

        if command == 'nop':
            i += 1
        elif command == 'acc':
            acc += arg
            i += 1
        elif command == 'jmp':
            i += arg

    return {'status': 'ok', 'acc': acc}


def fixProgram(program: list[dict]):
    for i in range(len(program)):
        command, arg = program[i].values()
        if command == 'nop' and arg != 0:
            program[i]['command'] = 'jmp'
            result = executeProgram(program)
            if result.get('status') == 'ok':
                return result
            else:
                program[i]['command'] = 'nop'
        elif command == 'jmp':
            program[i]['command'] = 'nop'
            result = executeProgram(program)
            if result.get('status') == 'ok':
                return result
            else:
                program[i]['command'] = 'jmp'


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_08_input.txt')
    program = loadProgram(file)
    part1 = executeProgram(program)
    part2 = fixProgram(program)

    print("part 1: ", part1.get('acc'))
    print("part 2: ", part2.get('acc'))

    assert part1.get('acc') == 5
    assert part2.get('acc') == 8


def main():
    print('\n---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_08_input.txt')
    program = loadProgram(file)
    part1 = executeProgram(program)
    part2 = fixProgram(program)

    print("part 1: ", part1.get('acc'))
    print("part 2: ", part2.get('acc'))


if __name__ == '__main__':
    test()
    main()
