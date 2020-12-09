import os
from collections import deque


def load_program(file: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        program = [int(line) for line in file]

    return program


def check_number(n: int, preamble: list[int]) -> bool:
    '''Test if any two numbers from preamble sum into n'''
    for i in range(0, len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == n:
                return True
    return False


def find_bug(program: list[int], preamble_length) -> int:
    '''Return the number for what we fail to compile a sum from the preamble'''
    for i in range(preamble_length, len(program)):
        n = program[i]
        preamble = program[i - preamble_length:i]
        if check_number(n, preamble) is False:
            return n


def find_weakness(program: list[int], bug: int) -> int:
    i, _sum = 0, 0
    queue = deque()
    while True:
        if _sum == bug:
            break
        if _sum > bug:
            _sum -= queue.popleft()
        else:
            queue.append(program[i])
            _sum += program[i]
            i += 1

    result = min(queue) + max(queue)
    return result


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_09_input.txt')
    program = load_program(file)
    bug = find_bug(program, preamble_length=5)
    weakness = find_weakness(program, bug)

    print("part 1: ", bug)
    print("part 2: ", weakness)

    assert bug == 127
    assert weakness == 62


def main():
    print('\n---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_09_input.txt')
    program = load_program(file)
    bug = find_bug(program, preamble_length=25)
    weakness = find_weakness(program, bug)

    print("part 1: ", bug)
    print("part 2: ", weakness)


if __name__ == '__main__':
    test()
    main()
