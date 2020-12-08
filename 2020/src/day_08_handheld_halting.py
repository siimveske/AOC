import os


def loadProgram(file: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    program = []
    with open(input_file_path, 'r') as file:
        for line in file:
            command, arg = line.split()
            program.append({'command': command, 'arg': int(arg), 'cnt': 0})

    return program


def executeProgram(program: list[dict]):
    i = 0
    acc = 0
    while i < len(program):
        command, arg, cnt = program[i].values()

        if cnt > 0:
            return {'status': 'error', 'acc': acc}
        program[i]['cnt'] += 1

        if command == 'nop':
            i += 1
        elif command == 'acc':
            acc += arg
            i += 1
        elif command == 'jmp':
            i += arg

    return {'status': 'ok', 'acc': acc}


def resetProgram(program: list[dict]):
    for instruction in program:
        instruction['cnt'] = 0
    return program


def fixProgram(program: list[dict]):
    resetProgram(program)
    for i in range(len(program)):
        command, arg, _ = program[i].values()
        if command == 'nop' and arg != 0:
            program[i]['command'] = 'jmp'
            result = executeProgram(program)
            if result.get('status') == 'ok':
                return result
            else:
                program[i]['command'] = 'nop'
                resetProgram(program)
        elif command == 'jmp':
            program[i]['command'] = 'nop'
            result = executeProgram(program)
            if result.get('status') == 'ok':
                return result
            else:
                program[i]['command'] = 'jmp'
                resetProgram(program)


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
