import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def check_direction(matrix: list[list[str]], row: int, col: int, direction: tuple[int, int]) -> bool:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row_offset, col_offset = direction
    letters = ['X']

    for i in range(1, 4):
        new_row = row + i * row_offset
        new_col = col + i * col_offset

        if (0 <= new_row < num_rows) and (0 <= new_col < num_cols):
            letters.append(matrix[new_row][new_col])

    return ''.join(letters) == 'XMAS'


def part1(input_file: str) -> int:
    """
    Find all occurrences of 'XMAS' in all eight directions from 'X'.
    """
    total = 0
    matrix = read_input(input_file)
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, 1),  # up_right
        (-1, -1),  # up_left
        (1, 1),  # down_right
        (1, -1)  # down_left
    ]

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 'X':
                for direction in directions:
                    if check_direction(matrix, row, col, direction):
                        total += 1
    return total


# def part2(input_file: str) -> int:
#     memory = read_input(input_file)
#     tokens = parse_tokens(memory)
#     total = multiply(tokens)
#     return total


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 4

    filename = 'test_input2.txt'
    assert part1(filename) == 18

    print('Part 1 OK')

    # filename = 'test_input2.txt'
    # assert part2(filename) == 48
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 2685
    # assert solution_part2 == 76729637


if __name__ == '__main__':
    test()
    main()
