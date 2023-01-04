from __future__ import annotations
import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            valve, neighbours = line.strip().split(';')
            valve_code = valve[6:8]
            if valve_code == 'HH':
                print()
            valve_flow_rate = int(valve[23:])

            neighbours = neighbours.strip()
            neighbours = neighbours.split(' ')[4:]
            neighbours = [n[0:2] for n in neighbours]

            data[valve_code] = (valve_flow_rate, neighbours)
    return data


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    return 0


def part2(inputFile: str):
    data = readInput(inputFile)
    return 0


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 26
    print('Part 1 OK')

    assert part2(filename) == 56000011
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    #assert solution_part1 == 4737443
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 11482462818989
    # print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
