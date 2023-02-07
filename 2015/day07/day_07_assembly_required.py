from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    tree = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            expression, dst = line.split(' -> ')
            if expression.isdecimal():
                expression = int(expression)
                tree[dst] = expression
            else:
                args = []
                items = expression.split(' ')
                for item in items:
                    if item.isdecimal():
                        args.append(int(item))
                    else:
                        args.append(item)
                tree[dst] = args
    return tree


def walk(tree, node: str, memo: dict) -> int:

    if node in memo:
        return memo[node]

    cmd = tree.get(node)
    if type(cmd) == int:  # a -> 100
        memo[node] = cmd
        return memo[node]

    if len(cmd) == 1:
        cmd = cmd[0]
        memo[node] = walk(tree, cmd, memo)  # a -> b
        return memo[node]

    if 'NOT' in cmd:
        _, arg = cmd
        # https://github.com/morgoth1145/advent-of-code/blob/main/2015/07/solution.py
        memo[node] = 0xFFFF ^ walk(tree, arg, memo)  # NOT a
        return memo[node]

    left, op, right = cmd
    if type(left) != int:
        left = walk(tree, left, memo)
    if type(right) != int:
        right = walk(tree, right, memo)

    if op == 'AND':
        memo[node] = left & right  # a AND b
    elif op == 'OR':
        memo[node] = left | right  # a OR b
    elif op == 'LSHIFT':
        memo[node] = left << right  # a LSHIFT b
    elif op == 'RSHIFT':
        memo[node] = left >> right  # a RSHIFT b

    return memo[node]


def part1(inputFile: str) -> int:
    tree = readInput(inputFile)
    result = walk(tree, 'a', {})
    return result


def part2(inputFile: str) -> int:
    pass


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    tree = readInput(filename)
    memo = {}
    assert walk(tree, 'd', memo) == 72
    assert walk(tree, 'e', memo) == 507
    assert walk(tree, 'f', memo) == 492
    assert walk(tree, 'g', memo) == 114
    assert walk(tree, 'h', memo) == 65412
    assert walk(tree, 'i', memo) == 65079
    assert walk(tree, 'x', memo) == 123
    assert walk(tree, 'y', memo) == 456
    print('Part 1 OK')

    # assert part2('turn on 0,0 through 0,0') == 1
    # assert part2('toggle 0,0 through 999,999') == 2_000_000
    #
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 46065

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part2 == 15343601


if __name__ == '__main__':
    test()
    main()
