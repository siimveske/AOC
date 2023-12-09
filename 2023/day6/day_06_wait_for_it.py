import math
import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    p = re.compile(r'\d+')
    with open(input_file_path, 'r') as f:
        lines = f.readlines()
        time = list(map(int, p.findall(lines[0])))
        dist = list(map(int, p.findall(lines[1])))

    return time, dist


def part1(input_file: str) -> int:
    times, distances = read_input(input_file)
    result = 1
    for time, max_dist in zip(times, distances):
        number_of_ways_to_win = 0
        for time_to_hold in range(1, time):
            speed = time_to_hold
            travel_time = time - time_to_hold
            distance = travel_time * speed
            if distance > max_dist:
                number_of_ways_to_win += 1
        result *= number_of_ways_to_win
    return result

    # def part2(input_file: str) -> int:
    #     times, distances = read_input(input_file)
    #     time = int(''.join(map(str, times)))
    #     record_distance = int(''.join(map(str, distances)))
    #
    #     number_of_ways_to_win = 0
    #     for time_to_hold in range(1, time):
    #         speed = time_to_hold
    #         travel_time = time - time_to_hold
    #         distance = travel_time * speed
    #         if distance > record_distance:
    #             number_of_ways_to_win += 1
    #     return number_of_ways_to_win


def part2(input_file: str) -> int:
    """
    link: https://en.wikipedia.org/wiki/Quadratic_formula
    link: https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb#scrollTo=zjf-F1pEb4_i
    d = (t - h) * h
    d = th - h**2

    Where d is the distance to beat, t is the race duration, and h is the hold time.

    Therefore:
    h**2 - th + d = 0
    """
    times, distances = read_input(input_file)
    time = int(''.join(map(str, times)))
    dist = int(''.join(map(str, distances)))

    # solve using quadratic
    discriminant = time ** 2 - (4 * dist)
    h1 = int((-time + math.sqrt(discriminant)) / 2)
    h2 = int((-time - math.sqrt(discriminant)) / 2)

    return abs(h1 - h2)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 288
    print('Part 1 OK')

    assert part2(filename) == 71503
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 840336
    assert solution_part2 == 41382569


if __name__ == '__main__':
    test()
    main()
