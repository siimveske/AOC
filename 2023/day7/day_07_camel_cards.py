import os
from collections import Counter


class Hand:
    CARD = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    STRENGTH = {
        'high-card': 0,
        'one-pair': 1,
        'two-pair': 2,
        'three-of-a-kind': 3,
        'full-house': 4,
        'four-of-a-kind': 5,
        'five-of-a-kind': 6
    }

    def __init__(self, cards: str, bid: str):
        self.bid = int(bid)
        self.cards = cards
        self.type = Hand._parse_type(cards)
        self.strength = Hand.STRENGTH[self.type]

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        if self.strength > other.strength:
            return False
        for a, b in zip(self.cards, other.cards):
            if a == b:
                continue
            return Hand.CARD[a] < Hand.CARD[b]
        return False

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        if self.strength < other.strength:
            return False
        for a, b in zip(self.cards, other.cards):
            if a == b:
                continue
            return Hand.CARD[a] > Hand.CARD[b]
        return False

    @staticmethod
    def _parse_type(cards: str):
        c = Counter(cards)
        c_val = list(c.values())
        if 5 in c_val:
            h_type = 'five-of-a-kind'
        elif 4 in c_val:
            h_type = 'four-of-a-kind'
        elif 3 in c_val and 2 in c_val:
            h_type = 'full-house'
        elif 3 in c_val and c_val.count(1) == 2:
            h_type = 'three-of-a-kind'
        elif c_val.count(2) == 2 and c_val.count(1) == 1:
            h_type = 'two-pair'
        elif c_val.count(2) == 1 and c_val.count(1) == 3:
            h_type = 'one-pair'
        elif c_val.count(1) == 5:
            h_type = 'high-card'
        else:
            raise Exception(f'Unknown hand: {cards}')
        return h_type


def read_input(filename: str) -> list[Hand]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        for line in f:
            hands = [Hand(cards, bid) for cards, bid in line.split()]
    return hands


def part1(input_file: str) -> int:
    hands = read_input(input_file)
    hands.sort()
    result = 0
    for idx, hand in enumerate(hands):
        result += (idx + 1) * hand.bid
    return result


def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 6440
    print('Part 1 OK')

    # assert part2(filename) == 71503
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 253954294
    # assert solution_part2 == 41382569


if __name__ == '__main__':
    test()
    main()
