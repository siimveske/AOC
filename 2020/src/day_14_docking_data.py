import os


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        program = [line.strip().split(' = ') for line in file]

    return program


def part1(file):
    program = load_program(file)

    memory = {}
    and_mask = ''
    or_mask = ''

    for line in program:
        key, value = line
        if key == 'mask':
            and_mask = int(value.replace('X', '1'), 2)
            or_mask = int(value.replace('X', '0'), 2)
        else:
            value = int(value)
            result = (value & and_mask) | or_mask
            memory[key] = result

    sum_of_all_values = sum(memory.values())
    print('part 1:', sum_of_all_values)
    return sum_of_all_values


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_14_input.txt')
    assert part1(file) == 165


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_14_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    main()
