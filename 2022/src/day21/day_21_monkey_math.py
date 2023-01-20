from operator import add, mul, sub, floordiv
import os

'''https://github.com/mebeim/aoc/tree/master/2022#day-21---monkey-math'''

OPMAP = {
    '+': add,
    '*': mul,
    '-': sub,
    '/': floordiv
}

# Calculate R or L knowing that E = L op R.
# True  = need to calculate L given E and R as parameters.
# False = need to calculate R given E and L as parameters.
REV_OPMAP = {
    ('+', True): sub,
    ('+', False): sub,
    ('*', True): floordiv,
    ('*', False): floordiv,
    ('-', True): add,
    ('-', False): lambda x, l: l - x,
    ('/', True): mul,
    ('/', False): lambda x, l: l // x,
}


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    Tree = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            a, b = line.strip().split(': ')
            Tree[a] = int(b) if b.isdigit() else b.split()
    return Tree


def calc(tree, node):
    value = tree[node]
    if not isinstance(value, list):
        return value

    l, op, r = value
    lvalue = calc(tree, l)
    rvalue = calc(tree, r)

    if lvalue is None or rvalue is None:
        return None

    return OPMAP[op](lvalue, rvalue)


def find_value(tree, node, expected):
    if node == 'humn':
        # We reached the node we wanted and we now know its value.
        return expected

    l, op, r = tree[node]
    lvalue = calc(tree, l)
    rvalue = calc(tree, r)

    if lvalue is None:
        # Left side has unknown value, calculate its expected value and keep going.
        expected = REV_OPMAP[op, True](expected, rvalue)
        return find_value(tree, l, expected)

    # Right side has unknown value, calculate its expected value and keep going.
    expected = REV_OPMAP[op, False](expected, lvalue)
    return find_value(tree, r, expected)


def part1(inputFile: str):
    tree = readInput(inputFile)
    result = calc(tree, 'root')
    return result


def part2(inputFile: str):
    tree = readInput(inputFile)
    tree['humn'] = None
    tree['root'][1] = '-'
    answer = find_value(tree, 'root', 0)
    return answer


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 152
    print('Part 1 OK')

    assert part2(filename) == 301
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 331319379445180

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 3715799488132


if __name__ == '__main__':
    test()
    main()
