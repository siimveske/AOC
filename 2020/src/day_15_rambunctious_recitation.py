from collections import defaultdict


def part1(numbers):

    turn = 1
    limit = 2020
    history = defaultdict(list)
    last_number = 0

    for index, number in enumerate(numbers, start=1):
        history[number] = [index]
        turn += 1
        last_number = number

    while turn <= limit:

        '''first time the number had been spoken, new number spoken is 0'''
        if len(history[last_number]) == 1:
            last_number = 0
            history[last_number].append(turn)
            turn += 1
            continue

        '''
        next number to speak is the difference between the
        turn number when it was last spoken and the turn
        number of the time it was most recently spoken before then
        '''
        last_but_one, last = history[last_number][-2:]
        next_number = last - last_but_one
        history[next_number].append(turn)
        last_number = next_number

        turn += 1

    print('part 1:', last_number)
    return last_number


def test():
    print('---- TEST ----')
    numbers = [0, 3, 6]
    assert part1(numbers) == 436
    numbers = [1, 3, 2]
    assert part1(numbers) == 1
    numbers = [2, 1, 3]
    assert part1(numbers) == 10
    numbers = [1, 2, 3]
    assert part1(numbers) == 27
    numbers = [2, 3, 1]
    assert part1(numbers) == 78
    numbers = [3, 2, 1]
    assert part1(numbers) == 438
    numbers = [3, 1, 2]
    assert part1(numbers) == 1836


def main():
    print('---- PROGRAM ----')
    numbers = [9, 12, 1, 4, 17, 0, 18]
    part1(numbers)


if __name__ == '__main__':
    test()
    main()
