import os


def binary(character):
    if character == '#':
        return 1
    else:
        return 0


def parse_input(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    initial_state = []
    with open(input_file_path, 'r') as file:
        for line in file:
            line = [binary(i) for i in line.strip()]
            initial_state.append(list(line))

    return initial_state


def print_layer(cubes, z=0):
    for row in cubes:
        print(row)


def part1(file):
    initial_state = parse_input(file)
    print_layer(initial_state)


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_17_input.txt')
    part1(file)


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_17_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    # main()
