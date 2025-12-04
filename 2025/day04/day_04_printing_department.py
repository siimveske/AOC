import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    grid = []
    with open(input_file_path, 'r') as f:
        grid = [line.strip() for line in f]

    return grid


def part1(input_file: str) -> int:
    grid = read_input(input_file)
    rows = len(grid)
    cols = len(grid[0])
    direction = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]

    number_of_accessible_paper_rolls = 0
    for r_idx in range(rows):
        for c_idx in range(cols):
            current = grid[r_idx][c_idx]

            # Only consider positions with a paper roll
            if current != '@':
                continue

            # Count paper rolls in the eight adjacent positions
            neighbours_cnt = 0
            for dr, dc in direction:
                nr, nc = r_idx + dr, c_idx + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbours_cnt += 1
            if neighbours_cnt < 4:
                number_of_accessible_paper_rolls += 1

    return number_of_accessible_paper_rolls


def part2(input_file: str) -> int:
    joltage_list = read_input(input_file)
    total_joltage = 0

    for joltages in joltage_list:
        digits = []
        current_index = 0

        # Extract 12 digits by finding max in sliding window
        for _ in range(12):
            remaining = 12 - len(digits)
            window_end = len(joltages) - (remaining - 1)
            window = joltages[current_index:window_end]

            max_digit = max(window)
            digits.append(max_digit)

            # Move index past the max digit found
            current_index += window.index(max_digit) + 1

        joltage = int(''.join(str(d) for d in digits))
        total_joltage += joltage

    return total_joltage


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    # assert part2(filename) == 3121910778619
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1356
    # assert solution_part2 == 175053592950232


if __name__ == '__main__':
    test()
    main()
