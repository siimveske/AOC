import os
import re
from operator import add, mul
from collections import deque
'''
    https://github.com/mebeim/aoc/tree/master/2020
'''


def read_file(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        return [tokenize(line) for line in file]


def tokenize(expr):
    return re.findall(r'\d+|[+*()]', expr)


def evaluate(tokens):
    accumulator = 0
    op = add

    while tokens:
        tok = tokens.popleft()

        if tok.isdigit():
            val = int(tok)
            accumulator = op(accumulator, val)
        elif tok == '+':
            op = add
        elif tok == '*':
            op = mul
        elif tok == '(':
            val = evaluate(tokens)
            accumulator = op(accumulator, val)
        elif tok == ')':
            break

    return accumulator


def part1(file):
    total = 0
    exprs = read_file(file)
    for expr in exprs:
        total += evaluate(deque(expr))

    print('part1: ', total)


def part2(file):
    result = solve(file)


def test():
    print('---- TEST ----')

    token = tokenize('1 + 2 * 3 + 4 * 5 + 6')
    value = evaluate(deque(token))
    assert value == 71

    token = tokenize('1 + (2 * 3) + (4 * (5 + 6))')
    value = evaluate(deque(token))
    assert value == 51

    token = tokenize('2 * 3 + (4 * 5)')
    value = evaluate(deque(token))
    assert value == 26

    token = tokenize('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    value = evaluate(deque(token))
    assert value == 437

    token = tokenize('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    value = evaluate(deque(token))
    assert value == 12240

    token = tokenize('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    value = evaluate(deque(token))
    assert value == 13632


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_18_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    #main()
