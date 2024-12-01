import os


def read_input(filename: str) -> tuple[list[int], list[int]]:
    """
    Reads a file and returns two sorted lists of integers.

    The file is expected to contain two integers per line, with the first integer
    on each line corresponding to the first list and the second integer on each
    line corresponding to the second list.
    """
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    list_a = []
    list_b = []

    with open(input_file_path, 'r') as f:
        for line in f:
            a, b = map(int, line.split())
            list_a.append(a)
            list_b.append(b)

    list_a.sort()
    list_b.sort()

    return list_a, list_b


def part1(input_file: str) -> int:
    first_list, second_list = read_input(input_file)
    total_difference = sum(abs(a - b) for a, b in zip(first_list, second_list))
    return total_difference


def part2(input_file: str) -> int:
    first_list, second_list = read_input(input_file)
    total = 0
    count_map = {}

    for num in first_list:
        if num not in count_map:
            count_map[num] = second_list.count(num)
        total += num * count_map[num]

    return total



def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 11
    print('Part 1 OK')

    assert part2(filename) == 31
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 1765812
    assert solution_part2 == 20520794


if __name__ == '__main__':
    test()
    main()
