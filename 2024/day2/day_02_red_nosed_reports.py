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

def is_safe(report: list[int]) -> bool:
    min_value = 1
    max_value = 3

    is_increasing_requence = report[0] < report[1]
    is_decreasing_sequence = report[0] > report[1]

    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]
        if not min_value <= abs(diff) <= max_value:
            return False

        next_item_is_smaller = report[i+1] < report[i]
        next_item_is_bigger = report[i+1] > report[i]

        if is_increasing_requence and next_item_is_smaller:
            return False
        if is_decreasing_sequence and next_item_is_bigger:
            return False

    return True

def get_safe_reports(reports: list[list[int]]) -> list[list[int]]:
    return [report for report in reports if is_safe(report)]

def generate_options(levels: list[int]) -> list[list[int]]:
    return [levels[:i] + levels[i+1:] for i in range(len(levels))]

def get_safe_reports2(reports: list[list[int]]) -> list[list[int]]:
    safe_reports = []
    for report in reports:
        for modified_report in generate_options(report):
            if is_safe(modified_report):
                safe_reports.append(modified_report)
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
