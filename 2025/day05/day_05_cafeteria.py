import os
import re


def read_input(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read().strip().split('\n\n')

        # Parse ranges
        range_lines = data[0].splitlines()
        ranges = []
        for r in range_lines:
            a, b = r.split('-')
            ranges.append((int(a), int(b)))

        # Parse IDs
        ids = data[1].splitlines()
        ids = [int(i) for i in ids]

        database = (ranges, ids)

    return database


def part1(input_file: str) -> int:
    ranges, ids = read_input(input_file)
    fresh_ingredient_cnt = 0
    for _id in ids:
        for start, end in ranges:
            if start <= _id <= end:
                fresh_ingredient_cnt += 1
                break

    return fresh_ingredient_cnt


def part2(input_file: str) -> int:
    ranges, _ = read_input(input_file)

    # Merge ranges and collect all fresh ingredient IDs
    merged_ranges = []
    while ranges:
        current_start, current_end = ranges.pop(0)
        range_merged = False
        for i in range(len(ranges)):
            start, end = ranges[i]
            if current_start <= start <= current_end:
                current_end = max(current_end, end)
                ranges.pop(i)
                ranges.append((current_start, current_end))
                range_merged = True
                break
            elif current_start <= end <= current_end:
                current_start = min(current_start, start)
                ranges.pop(i)
                ranges.append((current_start, current_end))
                range_merged = True
                break
        if not range_merged:
            merged_ranges.append((current_start, current_end))

    fresh_id_cnt = 0
    for start, end in merged_ranges:
        fresh_id_cnt += (end - start) + 1
    print("Merged Ranges:", merged_ranges)

    # 340988828813600 - too hight
    return fresh_id_cnt



    # for start, end in ranges:
    #     range_size = (end - start) + 1
    #     print(f'Range {start}-{end} has size {range_size}')
    #     fresh_ingredient_ids.update(range(start, end + 1))

    return len(fresh_ingredient_ids)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 3
    print('Part 1 OK')

    assert part2(filename) == 14
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 525
    # assert solution_part2 == 8713


if __name__ == '__main__':
    test()
    main()
