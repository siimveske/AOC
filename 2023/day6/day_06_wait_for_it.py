import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    p = re.compile(r'\d+')
    with open(input_file_path, 'r') as f:
        lines = f.readlines()
        time = [int(number) for number in p.findall(lines[0])]
        dist = [int(number) for number in p.findall(lines[1])]

    return time, dist


def part1(input_file: str) -> int:
    times, distances = read_input(input_file)
    margin_of_error = 1
    for i, time in enumerate(times):
        number_of_ways_to_win = 0
        max_dist = distances[i]
        for time_to_hold in range(1, time):
            speed = time_to_hold
            travel_time = time - time_to_hold
            distance = travel_time * speed
            if distance > max_dist:
                number_of_ways_to_win += 1
        margin_of_error *= number_of_ways_to_win
    return margin_of_error


def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 288
    print('Part 1 OK')

    # assert part2(filename) == 46
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 196167384
    # assert solution_part2 == 125742456


if __name__ == '__main__':
    test()
    main()
