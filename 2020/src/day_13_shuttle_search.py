import os


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        timestamp = int(file.readline())
        bus_ids = [int(i) for i in file.readline().split(',') if i != 'x']

    return (timestamp, bus_ids)


def next_bus(start, buses):
    return min([(bus - (start % bus), bus) for bus in buses])


def part1(file):
    start, buses = load_program(file)
    wait_time, bus_id = next_bus(start, buses)
    result = wait_time * bus_id

    print('part 1:', result)
    return result


def part2(file):
    load_program(file)


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
