import os


def read_input(filename: str) -> list[list[int, int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    list_a = []
    list_b = []

    with open(input_file_path, 'r') as f:
        for line in f:
            a, b = line.split()
            list_a.append(int(a))
            list_b.append(int(b))

    list_a.sort()
    list_b.sort()
    pairs = [list_a, list_b]

    return pairs


def part1(input_file: str) -> int:
    list_a, list_b = read_input(input_file)
    pairs = list(zip(list_a, list_b))

    total = 0
    for a, b in pairs:
        total += abs(a-b)
    return total


def part2(input_file: str) -> int:
    list_a, list_b = read_input(input_file)
    total = 0
    counts = {}

    for number in list_a:
        if number not in counts:
            counts[number] = list_b.count(number)
        total += number * counts[number]
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
