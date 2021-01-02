import os


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    program = []
    with open(input_file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(' = ')
            if key == 'mask':
                program.append((key, value))
            else:
                program.append((int(key[4:-1]), int(value)))

    return program


def apply_mask(address, mask):
    result = []
    mask_length = len(mask)
    bin_address = format(address, f'0{mask_length}b')
    for i in range(mask_length):
        mask_bit = mask[i]
        if mask_bit == '0':
            # If the bitmask bit is 0, the corresponding memory address bit is unchanged
            result.append(bin_address[i])
        elif mask_bit == '1':
            # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1
            result.append('1')
        elif mask_bit == 'X':
            # If the bitmask bit is X, the corresponding memory address bit is floating
            result.append('{}')

    return ''.join(result)


def part1(file):
    program = load_program(file)

    memory = {}
    and_mask = ''
    or_mask = ''

    for key, value in program:
        if key == 'mask':
            and_mask = int(value.replace('X', '1'), 2)
            or_mask = int(value.replace('X', '0'), 2)
        else:
            result = (value & and_mask) | or_mask
            memory[key] = result

    sum_of_all_values = sum(memory.values())
    print('part 1:', sum_of_all_values)
    return sum_of_all_values


def part2(file):
    program = load_program(file)

    memory = {}
    mask = ''
    floating_bit_count = 0

    for key, value in program:
        if key == 'mask':
            mask = value
            floating_bit_count = mask.count('X')
        else:
            template = apply_mask(key, mask)
            for i in range(pow(2, floating_bit_count)):
                bitstring = format(i, f'0{floating_bit_count}b')
                masked_address = template.format(*bitstring)
                address = int(masked_address, 2)
                memory[address] = value

    sum_of_all_values = sum(memory.values())
    print('part 2:', sum_of_all_values)
    return sum_of_all_values


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_14_input.txt')
    assert part1(file) == 165

    file = os.path.join('..', 'test', 'day_14_input2.txt')
    assert part2(file) == 208


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_14_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    test()
    main()
