import os
from collections import Counter
from typing import Any


class Hand:
    STRENGTH = {
        'high-card': 0,
        'one-pair': 1,
        'two-pair': 2,
        'three-of-a-kind': 3,
        'full-house': 4,
        'four-of-a-kind': 5,
        'five-of-a-kind': 6
    }

    def __init__(self, cards: str, bid: str, joker=False):
        self.card_scores = {
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
        self.bid = int(bid)
        self.cards = cards
        self.joker = joker
        if joker:
            self.card_scores['J'] = 1
        self.type = self._parse_type()
        self.strength = Hand.STRENGTH[self.type]

    def __lt__(self, other):
        if self.cards == other.cards:
            return False

        if self.strength != other.strength:
            return self.strength < other.strength

        for a, b in zip(self.cards, other.cards):
            if a == b:
                continue
            return self.card_scores[a] < self.card_scores[b]

        assert False

    def _parse_type(self):
        cards = self.cards  # we will replace value of joker
        ordered_counts = Counter(cards).most_common()  # e.g. [('3', 2), ('2', 1), ('T', 1), ('K', 1)]

        # get the most common card
        best, best_count = ordered_counts[0]  # e.g. ('3', 2)
        if best_count == 5:
            return "five-of-a-kind"

        second_best, second_best_count = ordered_counts[1]  # e.g. ('2', 1)

        if self.joker:  # Part 2
            if best == 'J':  # get the next best card
                best, best_count = second_best, second_best_count

            # convert all J into the best card
            cards = cards.replace("J", best)

            ordered_counts = Counter(cards).most_common()  # recount the hand
            best, best_count = ordered_counts[0]
            if best_count == 5:
                return "five-of-a-kind"

            second_best, second_best_count = ordered_counts[1]  # e.g. ('2', 1)

        if best_count == 4:
            return "four-of-a-kind"

        if best_count == 3:
            if second_best_count == 2:
                return "full-house"
            else:
                return "three-of-a-kind"

        if best_count == 2:
            if second_best_count == 2:
                return "two-pair"
            else:
                return "one-pair"

        return "high-card"


def read_input(filename: str) -> list[tuple[Any, Any]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            cards, bid = line.split()
            data.append((cards, bid))
    return data


def part1(input_file: str) -> int:
    data = read_input(input_file)
    hands = [Hand(cards, bid) for cards, bid in data]
    hands.sort()
    result = 0
    for idx, hand in enumerate(hands, 1):
        result += (idx * hand.bid)
    return result


def part2(input_file: str) -> int:
    data = read_input(input_file)
    hands = [Hand(cards, bid, joker=True) for cards, bid in data]
    hands.sort()
    result = 0
    for idx, hand in enumerate(hands, 1):
        result += idx * hand.bid
    return result


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
