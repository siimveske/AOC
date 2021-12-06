import os
'''
Refactored solution. Inspired by
https://github.com/mebeim/aoc/blob/master/2021/solutions/day04.py
'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        numbers = [int(i) for i in f.readline().split(',')]
        raw_cards = f.read().split('\n\n')

        cards = []
        for raw_card in raw_cards:
            raw_card = raw_card.strip().splitlines()
            card = list(list(map(int, row.split())) for row in raw_card)
            cards.append(card)

    return (numbers, cards)


def check_win(card, row, c):
    if sum(x == -1 for x in row) == 5:
        return True
    if sum(r[c] == -1 for r in card) == 5:
        return True
    return False


def mark(card, number):
    for r, row in enumerate(card):
        for c, cell in enumerate(row):
            if cell == number:
                card[r][c] = -1
                return check_win(card, row, c)
    return False


def winner_score(card, last_number):
    unmarked_tot = 0
    for row in card:
        unmarked_tot += sum([cell for cell in row if cell != -1])

    return unmarked_tot * last_number


def part1(inputFile: str):
    numbers, cards = readInput(inputFile)
    for number in numbers:
        for card in cards:
            win = mark(card, number)
            if win:
                score = winner_score(card, number)
                return score


def part2(inputFile: str):
    numbers, cards = readInput(inputFile)
    n_cards = len(cards)
    n_won = 0

    for number in numbers:
        for i, card in enumerate(cards):
            if card is None:
                continue

            win = mark(card, number)
            if win:
                n_won += 1
                if n_won == n_cards:
                    score = winner_score(card, number)
                    return score
                cards[i] = None


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 4512
    print('Part 1 OK')
    assert part2(filename) == 1924
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
