import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        monkeys = f.read()
        monkeys = monkeys.split('\n\n')

    parsed_monkeys = []
    for idx, monkey in enumerate(monkeys):
        creature = dict()
        props = monkey.splitlines()

        creature['idx'] = idx

        starting_items = props[1].split(':')[1].split(',')
        starting_items = [int(i.strip()) for i in starting_items]
        creature['starting_items'] = starting_items

        operation = props[2].split('=')[1].strip()
        creature['operation'] = operation

        divisor = props[3].strip().split(':')[1].split(' ')[-1]
        divisor = int(divisor)
        creature['divisor'] = divisor

        yes = props[4].strip().split(' ')[-1]
        yes = int(yes)
        creature['yes'] = yes

        no = props[5].strip().split(' ')[-1]
        no = int(no)
        creature['no'] = no

        parsed_monkeys.append(creature)

    return parsed_monkeys


def part1(inputFile: str) -> int:
    monkeys = readInput(inputFile)


def part2(inputFile: str):
    commands = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13140
    print('Part 1 OK')

    # assert part2(filename) == 1
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 12640
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == EHBZLRJR
    # print(f'Solution for Part 2: \n{solution_part2}')


if __name__ == '__main__':
    test()
    main()
