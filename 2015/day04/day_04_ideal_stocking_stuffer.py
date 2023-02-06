from __future__ import annotations
import os
import hashlib


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().strip()


def solve(prefix: str, secret: str) -> int:
    idx = 0
    while True:
        string = (secret + str(idx)).encode(encoding='utf-8')
        hash: str = hashlib.md5(string).hexdigest()
        if hash.startswith(prefix):
            return idx
        idx += 1


def part1(inputFile: str) -> int:
    secret = readInput(inputFile)
    prefix = '00000'
    return solve(prefix, secret)


def part2(inputFile: str) -> int:
    secret = readInput(inputFile)
    prefix = '000000'
    return solve(prefix, secret)


def test():
    print('---- TEST ----')

    assert solve('00000', 'abcdef') == 609043
    assert solve('00000', 'pqrstuv') == 1048970
    print('OK')


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
