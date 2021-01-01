import os
import math


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        timestamp = int(file.readline())
        bus_ids = [int(i) if i != 'x' else i for i in file.readline().split(',')]

    return (timestamp, bus_ids)


def next_bus(start, buses):
    best_bus = (math.inf, math.inf)
    for bus in buses:
        if bus == 'x':
            continue
        time_to_wait = bus - (start % bus)
        if time_to_wait < best_bus[0]:
            best_bus = (time_to_wait, bus)

    return best_bus


def part1(file):
    start, buses = load_program(file)
    wait_time, bus = next_bus(start, buses)
    result = wait_time * bus

    print('part 1:', result)
    return result


def part2(file):
    '''
        1. https://github.com/mebeim/aoc/tree/master/2020#part-2---purely-mathematical-approach
        2. https://github.com/codertee/adventofcode/blob/main/adventofcode/solutions/y2020/d13_modular.py
    '''
    _, buses = load_program(file)
    time = step = buses[0]
    for index, bus in enumerate(buses[1:], 1):
        if bus == 'x':
            continue
        while (time + index) % bus != 0:
            time += step
        step *= bus

    print('part 2:', time)
    return time


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_13_input.txt')
    assert part1(file) == 295
    part2(file)


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_13_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    test()
    main()
