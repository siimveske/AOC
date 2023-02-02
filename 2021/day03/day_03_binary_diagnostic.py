import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        report = [line.strip() for line in f.readlines()]

    return report


def find_counts(report: list, bit_index: int):
    result = [0, 0]
    for item in report:
        result[int(item[bit_index])] += 1
    return result


def part1(inputFile: str):

    report = readInput(inputFile)

    gamma_rate = ''
    epsilon_rate = ''
    for col in range(len(report[0])):
        cnt_0, cnt_1 = find_counts(report, col)
        if cnt_0 > cnt_1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


def find_oxygen_rating(report: list):

    result = filter_oxygen_rating(report, 0)
    for i in range(1, len(result[0])):
        result = filter_oxygen_rating(result, i)
        if len(result) == 1:
            break

    if len(result) > 1:
        raise Exception('Failed to filter oxygen rating')

    return int(result[0], 2)


def find_co2_rating(report: list):

    result = filter_co2_rating(report, 0)
    for i in range(1, len(result[0])):
        result = filter_co2_rating(result, i)
        if len(result) == 1:
            break

    if len(result) > 1:
        raise Exception('Failed to filter co2 rating')

    return int(result[0], 2)


def filter_oxygen_rating(report: list, index: int):
    result = []
    cnt_0, cnt_1 = find_counts(report, index)
    for item in report:
        if (cnt_0 > cnt_1) and item[index] == '0':
            result.append(item)
        elif (cnt_1 > cnt_0) and item[index] == '1':
            result.append(item)
        elif (cnt_0 == cnt_1) and item[index] == '1':
            result.append(item)
    return result


def filter_co2_rating(report: list, index: int):
    result = []
    cnt_0, cnt_1 = find_counts(report, index)
    for item in report:
        if (cnt_0 < cnt_1) and item[index] == '0':
            result.append(item)
        elif (cnt_1 < cnt_0) and item[index] == '1':
            result.append(item)
        elif (cnt_0 == cnt_1) and item[index] == '0':
            result.append(item)
    return result


def part2(inputFile: str):

    report = readInput(inputFile)

    oxygen_rating = find_oxygen_rating(report)
    co2_rating = find_co2_rating(report)

    return oxygen_rating * co2_rating


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 198
    print('Part 1 OK')
    assert part2(filename) == 230
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
