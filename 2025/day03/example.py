# from: https://www.reddit.com/r/adventofcode/comments/1pcvaj4/comment/ns3344n/

import os

def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        banks = [lines.strip() for lines in f]

    return banks

def find_joltage(needed_bats, banks) -> int:
    joltage = 0
    for bank in banks:
        need_to_remove = len(bank) - needed_bats
        while need_to_remove > 0:
            for i in range(len(bank) - 1):
                if bank[i] < bank[i+1]:
                    bank = bank[:i] + bank[i+1:]
                    break
            need_to_remove -= 1
        joltage += int(bank[:needed_bats])
    return joltage

def part1(input_file: str) -> int:
    banks = read_input(input_file)
    return find_joltage(2, banks)


def part2(input_file: str) -> int:
    banks = read_input(input_file)
    return find_joltage(12, banks)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 357
    print('Part 1 OK')

    assert part2(filename) == 3121910778619
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 17554
    assert solution_part2 == 175053592950232


if __name__ == '__main__':
    test()
    main()
