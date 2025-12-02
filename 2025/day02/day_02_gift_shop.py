import os


def read_input(filename: str) -> list[tuple[int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    product_id_ranges = []

    with open(input_file_path, 'r') as f:
        raw_data = f.read().strip()
        splitted_data = raw_data.split(',')
        for item in splitted_data:
            start_str, end_str = item.split('-')
            product_id_ranges.append((int(start_str), int(end_str)))

    return product_id_ranges


def part1(input_file: str) -> int:
    ranges = read_input(input_file)
    total = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            str_i = str(i)
            if len(str_i) % 2 != 0:
                continue

            midpoint = len(str_i) // 2
            first_half = str_i[:midpoint]
            second_half = str_i[midpoint:]
            if first_half == second_half:
                total += i

    return total


# def part2(input_file: str) -> int:
#     numbers = read_input(input_file)
#     position = 50
#     code = 0

#     for number in numbers:
#         for _ in range(abs(number)):
#             step = 1 if number > 0 else -1
#             position = (position + step) % 100
#             if position == 0:
#                 code += 1

#     return code


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1227775554
    print('Part 1 OK')

    # assert part2(filename) == 6
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 35367539282
    # assert solution_part2 == 5831


if __name__ == '__main__':
    test()
    main()
