from __future__ import annotations
import os
import hashlib


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().strip()


def part1(input: str) -> int:

    if input.endswith('.txt'):
        secret = readInput(input)
    else:
        secret = input

    idx = 0
    while True:
        string = (secret + str(idx)).encode(encoding='utf-8')
        hash: str = hashlib.md5(string).hexdigest()
        if hash.startswith('00000'):
            return idx
        idx += 1


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')

    assert part1('abcdef') == 609043
    assert part1('pqrstuv') == 1048970
    print('Part 1 OK')

    # assert len(travel2('^v')) == 3
    # assert len(travel2('^>v<')) == 3
    # assert len(travel2('^v^v^v^v^v')) == 11
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
