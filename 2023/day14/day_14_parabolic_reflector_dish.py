import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        lines = [[*n.strip()] for n in f.readlines()]

    return lines


def part1(input_file: str) -> int:
    lines = read_input(input_file)
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

    result = 0
    for i in range(len(lines), 0, -1):
        i_row = len(lines) - i
        row = lines[i_row]
        c_row = sum([item == 'O' for item in row])
        result += i * c_row
    return result


def part2(input_file: str) -> int:
    raw_lines = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 136
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

    assert solution_part1 == 106648
    # assert solution_part2 == 54925


if __name__ == '__main__':
    test()
    main()
