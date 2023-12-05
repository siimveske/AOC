import os
import re
from collections import defaultdict


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    cards = []
    with open(input_file_path, 'r') as f:
        p = re.compile(r'\d+')
        for line in f:
            my_numbers, winning_numbers = line[8:].split(' | ')
            my_numbers = [int(number) for number in p.findall(my_numbers)]
            winning_numbers = [int(number) for number in p.findall(winning_numbers)]
            cards.append([my_numbers, winning_numbers])

    return cards


def part1(input_file: str) -> int:
    cards = read_input(input_file)
    total = 0
    for card in cards:
        my_numbers, winning_numbers = card
        matched_numbers = set(my_numbers).intersection(set(winning_numbers))
        number_of_matches = len(matched_numbers)
        if number_of_matches:
            points = 2 ** (number_of_matches - 1)
            total += points

    return total


def part2(input_file: str) -> int:
    cards = read_input(input_file)
    cnt_dict = defaultdict(int)
    for idx, card in enumerate(cards):
        my_numbers, winning_numbers = card
        matched_numbers = set(my_numbers).intersection(set(winning_numbers))
        number_of_matches = len(matched_numbers)
        cnt_dict[idx] += 1
        if number_of_matches:
            for i in range(1, number_of_matches + 1):
                cnt_dict[idx + i] += cnt_dict[idx]

    total = sum(cnt_dict.values())
    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    assert part2(filename) == 30
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 23441
    assert solution_part2 == 5923918


if __name__ == '__main__':
    test()
    main()
