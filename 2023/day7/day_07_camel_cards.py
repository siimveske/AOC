import os
from collections import Counter

'''
Solution from: https://github.com/mebeim/aoc/blob/master/2023/solutions/day07.py
'''


def read_input(filename: str) -> dict[str, int]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    bets = {}
    tbl = str.maketrans('TJQKA', 'ABCDE')
    with open(input_file_path, 'r') as f:
        for line in f:
            hand, bet = line.split()
            bets[hand.translate(tbl)] = int(bet)
    return bets


def strength(hand):
    counter = Counter(hand)
    descending_frequencies = sorted(counter.values(), reverse=True)
    return descending_frequencies, hand


def strength_with_joker(hand):
    if hand == '00000':
        return [5], hand

    counter = Counter(hand)
    jokers = counter.pop('0', 0)
    descending_frequencies = sorted(counter.values(), reverse=True)
    descending_frequencies[0] += jokers

    return descending_frequencies, hand


def part1(input_file: str) -> int:
    bets = read_input(input_file)
    ordered_hands = sorted(bets, key=strength)
    total = 0

    for rank, hand in enumerate(ordered_hands, 1):
        total += rank * bets[hand]

    return total


def part2(input_file: str) -> int:
    bets = read_input(input_file)
    new_bets = {hand.replace('B', '0'): bet for hand, bet in bets.items()}
    ordered_hands = sorted(new_bets, key=strength_with_joker)
    total = 0

    for rank, hand in enumerate(ordered_hands, 1):
        total += rank * new_bets[hand]

    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 6440
    print('Part 1 OK')

    assert part2(filename) == 5905
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 253954294
    assert solution_part2 == 254837398


if __name__ == '__main__':
    test()
    main()
