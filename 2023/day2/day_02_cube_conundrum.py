import os
from typing import Dict, List, Any


def read_input(filename: str) -> dict[int, list[dict[Any, int]]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    games = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            game, data = line.strip().split(': ')
            game_id = int(game.split(' ')[1])
            subsets = []
            for subset in data.split('; '):
                cubes = {}
                for cube in subset.split(', '):
                    amount, color = cube.split(' ')
                    cubes[color] = int(amount)
                subsets.append(cubes)
            games[game_id] = subsets

    return games


def part1(input_file: str) -> int:
    games: dict = read_input(input_file)
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for game_id, game_data in games.items():
        is_valid = True
        for subset in game_data:
            for color, amount in subset.items():
                if amount > limits[color]:
                    is_valid = False
        if is_valid:
            total += game_id

    return total



def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 8
    print('Part 1 OK')

    # filename = 'test_input2.txt'
    # assert part2(filename) == 281
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    #
    # assert solution_part1 == 55172
    # assert solution_part2 == 54925


if __name__ == '__main__':
    test()
    main()
