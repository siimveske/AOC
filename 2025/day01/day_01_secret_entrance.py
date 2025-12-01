import os


def read_input(filename: str) -> list[int]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    numbers = []

    with open(input_file_path, 'r') as f:
        for line in f:
            value = int(line.replace('L', "-").replace('R', "").strip())
            numbers.append(value)

    return numbers


def part1(input_file: str) -> int:
    numbers = read_input(input_file)
    position = 50
    code = 0
    for number in numbers:
        position = (position + number) % 100
        if position == 0:
            code += 1
    return code


# def part2(input_file: str) -> int:
#     first_list, second_list = read_input(input_file)
#     total = 0
#     count_map = {}

#     for num in first_list:
#         if num not in count_map:
#             count_map[num] = second_list.count(num)
#         total += num * count_map[num]

#     return total



def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 3
    print('Part 1 OK')

    # assert part2(filename) == 31
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1031
    # assert solution_part2 == 20520794


if __name__ == '__main__':
    test()
    main()
