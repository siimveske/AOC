from operator import add, mul, sub, floordiv
import os

OPMAP = {
    '+': add,
    '*': mul,
    '-': sub,
    '/': floordiv
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
    if isinstance(value, int):
        return value

    l, op, r = value
    lvalue = calc(tree, l)
    rvalue = calc(tree, r)
    return OPMAP[op](lvalue, rvalue)


def part1(inputFile: str):
    tree = readInput(inputFile)
    result = calc(tree, 'root')
    return result


def part2(inputFile: str):
    coordinates = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 152
    print('Part 1 OK')

    # assert part2(filename) == 1623178306
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # assert solution_part1 == 3346

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 4265712588168


if __name__ == '__main__':
    test()
    main()
