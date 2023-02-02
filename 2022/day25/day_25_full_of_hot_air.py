from __future__ import annotations
import os
import math

''' Inspired by: https://adventofcode.com/2022/day/25'''

def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read().splitlines()

    return data

SNAFU_MAP = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def decode(snafu:str) -> int:
    result = 0
    for index, char in enumerate(snafu[::-1]):
        result += SNAFU_MAP[char]*math.pow(5, index)
    return int(result)

def encode(n: int) -> str:
    res = ''

    while n:
        n, digit = divmod(n, 5)

        if digit > 2:
            # Add 1 more of the next (higher) power of 5
            n += 1

            # Borrow from it:
            if digit == 3:
                res += '=' # Take 2 x current power of 5.
            else: # digit == 4
                res += '-' # Take 1 x current power of 5.
        else:
            res += str(digit)

    return res[::-1]

def part1(inputFile: str):
    data = readInput(inputFile)
    total = 0
    for line in data:
        total += decode(line)
    snafu = encode(total)
    return snafu

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == '2=-1=0'
    print('Part 1 OK')

def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == '2-0-020-1==1021=--01'

if __name__ == '__main__':
    test()
    main()
