import os


def read_input(filename: str) -> list[list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    reports = []
    with open(input_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            levels = map(int, line.split())
            reports.append(list(levels))

    return reports

def get_safe_reports(reports: list[list[int]]) -> list[list[int]]:
    safe_reports = []

    min_diff = 1
    max_diff = 3
    for line in reports:
        is_increasing_requence = line[0] < line[1]
        is_safe = True
        for i in range(len(line) - 1):
            diff = line[i] - line[i+1]
            if not min_diff <= abs(diff) <= max_diff:
                is_safe = False
                break
            if is_increasing_requence and (line[i] - line[i+1]) >= 0:
                is_safe = False
                break
            if not is_increasing_requence and (line[i] - line[i+1]) <= 0:
                is_safe = False
                break
        if is_safe:
            safe_reports.append(line)

    return safe_reports

def is_safe_report(report: list[int]) -> int:
    min_diff = 1
    max_diff = 3
    is_increasing_requence = report[0] < report[1]

    is_safe = -1
    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]
        if not min_diff <= abs(diff) <= max_diff:
            is_safe = i
            break
        if is_increasing_requence and (report[i] - report[i+1]) >= 0:
            is_safe = i
            break
        if not is_increasing_requence and (report[i] - report[i+1]) <= 0:
            is_safe = i
            break
    return is_safe

def generate_sublists(input_list):
    result = []
    for i in range(len(input_list)):
        sublist = input_list[:i] + input_list[i+1:]
        result.append(sublist)
    return result

def get_safe_reports2(reports: list[list[int]]) -> list[list[int]]:
    safe_reports = []

    for line in reports:
        is_safe = is_safe_report(line)

        if is_safe == -1:
            safe_reports.append(line)
            continue

        for option in generate_sublists(line):
            if is_safe_report(option) == -1:
                safe_reports.append(option)
                break

    return safe_reports

def part1(input_file: str) -> int:
    reports = read_input(input_file)
    safe_reports = get_safe_reports(reports)
    result = len(safe_reports)
    return result

def part2(input_file: str) -> int:
    reports = read_input(input_file)
    safe_reports = get_safe_reports2(reports)
    result = len(safe_reports)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 2
    print('Part 1 OK')

    assert part2(filename) == 4
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 383
    assert solution_part2 == 436


if __name__ == '__main__':
    test()
    main()
