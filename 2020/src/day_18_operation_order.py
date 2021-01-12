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


def evaluate2(tokens):
    multiplier = 1
    accumulator = 0

    while tokens:
        tok = tokens.popleft()

        if tok.isdigit():
            val = int(tok)
            accumulator += val * multiplier
        elif tok == '*':
            multiplier = accumulator
            accumulator = 0
        elif tok == '(':
            val = evaluate2(tokens)
            accumulator += val * multiplier
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
    total = 0
    exprs = read_file(file)
    for expr in exprs:
        total += evaluate2(deque(expr))

    print('part2: ', total)


def test():
    print('---- TEST ----')

    token = tokenize('1 + 2 * 3 + 4 * 5 + 6')
    assert evaluate(deque(token)) == 71
    assert evaluate2(deque(token)) == 231

    token = tokenize('1 + (2 * 3) + (4 * (5 + 6))')
    assert evaluate(deque(token)) == 51
    assert evaluate2(deque(token)) == 51

    token = tokenize('2 * 3 + (4 * 5)')
    assert evaluate(deque(token)) == 26
    assert evaluate2(deque(token)) == 46

    token = tokenize('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    assert evaluate(deque(token)) == 437
    assert evaluate2(deque(token)) == 1445

    token = tokenize('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    assert evaluate(deque(token)) == 12240
    assert evaluate2(deque(token)) == 669060

    token = tokenize('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    assert evaluate(deque(token)) == 13632
    assert evaluate2(deque(token)) == 23340


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_18_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    #test()
    main()
