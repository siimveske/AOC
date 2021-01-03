from collections import defaultdict


def play(numbers, game_length=2020):

    last_number = 0
    history = defaultdict(list)

    for turn, number in enumerate(numbers, start=1):
        history[number].append(turn)
        last_number = number

    for turn in range(len(numbers) + 1, game_length + 1):

        '''first time the number had been spoken, new number spoken is 0'''
        if len(history[last_number]) == 1:
            last_number = 0
            history[last_number].append(turn)
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

    return last_number


def test():
    numbers = [0, 3, 6]
    assert play(numbers) == 436
    numbers = [1, 3, 2]
    assert play(numbers) == 1
    numbers = [2, 1, 3]
    assert play(numbers) == 10
    numbers = [1, 2, 3]
    assert play(numbers) == 27
    numbers = [2, 3, 1]
    assert play(numbers) == 78
    numbers = [3, 2, 1]
    assert play(numbers) == 438
    numbers = [3, 1, 2]
    assert play(numbers) == 1836

    #===========================================================================
    # numbers = [0, 3, 6]
    # assert play(numbers, game_length=30000000) == 175594
    # numbers = [1, 3, 2]
    # assert play(numbers, game_length=30000000) == 2578
    # numbers = [2, 1, 3]
    # assert play(numbers, game_length=30000000) == 3544142
    # numbers = [1, 2, 3]
    # assert play(numbers, game_length=30000000) == 261214
    # numbers = [2, 3, 1]
    # assert play(numbers, game_length=30000000) == 6895259
    # numbers = [3, 2, 1]
    # assert play(numbers, game_length=30000000) == 18
    # numbers = [3, 1, 2]
    # assert play(numbers, game_length=30000000) == 362
    #===========================================================================


def main():
    numbers = [9, 12, 1, 4, 17, 0, 18]
    print('part 1:', play(numbers))
    print('part 2:', play(numbers, game_length=30000000))


if __name__ == '__main__':
    test()
    main()
