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
    while True:
        command, arg, cnt = program[i].values()
        
        if cnt > 0:
            return acc
        program[i]['cnt'] += 1
        
        if command == 'nop':
            i += 1
        elif command == 'acc':
            acc += arg
            i += 1
        elif command == 'jmp':
            i += arg
    
def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_08_input.txt')
    program = loadProgram(file)
    acc = executeProgram(program)
    print("part 1: ", acc)
    
    assert acc == 5


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_08_input.txt')
    program = loadProgram(file)
    acc = executeProgram(program)
    print("part 1: ", acc)
    
if __name__ == '__main__':
    test()
    main()