import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        lines = [list(n.strip()) for n in f]

    return lines


def tilt(lines):
    transforms = [0] * len(lines[0])
    for i_row in range(1, len(lines)):
        row = lines[i_row]
        prev_row = lines[i_row - 1]
        for i_col in range(len(row)):
            this_item = row[i_col]
            prev_item = prev_row[i_col]
            if prev_item == '.':
                transforms[i_col] += 1
            elif prev_item == '#':
                transforms[i_col] = 0
            if this_item == 'O' and transforms[i_col]:
                lines[i_row - transforms[i_col]][i_col] = 'O'
                lines[i_row][i_col] = '.'
                transforms[i_col] -= 1


def part1(input_file: str) -> int:
    lines = read_input(input_file)
    line_length = len(lines[0])
    tilt(lines)

    result = 0
    for idx_row, row in enumerate(lines):
        row_sum = sum([item == 'O' for item in row])
        result += row_sum * (line_length - idx_row)
    return result


def rotate_matrix(matrix):
    return [list(reversed(col)) for col in list(zip(*matrix))]


def part2(input_file: str) -> int:
    """Inspired by: https://redd.it/18kmo3i and
    https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb"""
    lines = read_input(input_file)
    line_length = len(lines[0])

    num_of_directions = 4
    required_cycles = 1_000_000_000
    states = {}
    end_cycle = -1
    start_cycle = -1
    for cycle_index in range(required_cycles):
        for direction in range(num_of_directions):
            tilt(lines)
            lines = rotate_matrix(lines)

        board_state = ''.join([item for line in lines for item in line])
        if board_state in states:
            end_cycle = cycle_index
            start_cycle = states[board_state]
            break
        else:
            states[board_state] = cycle_index

    # Do some math
    repeat_len = end_cycle - start_cycle                    # length of 1 cycle
    remaining_cycles = required_cycles - (end_cycle + 1)    # distance from current location to endpoint
    additional_cycles = remaining_cycles % repeat_len

    for cycle in range(additional_cycles):
        for direction in range(num_of_directions):
            tilt(lines)
            lines = rotate_matrix(lines)

    result = 0
    for idx_row, row in enumerate(lines):
        row_sum = sum([item == 'O' for item in row])
        result += row_sum * (line_length - idx_row)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 136
    print('Part 1 OK')

    assert part2(filename) == 64
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 106648
    assert solution_part2 == 87700


if __name__ == '__main__':
    test()
    main()
