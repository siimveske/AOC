import os


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

    # Sort the ranges by their start value (the first number)
    # This is crucial so we only need to compare with the last merged item.
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    # Initialize merged ranges with the first sorted range
    merged = [sorted_ranges[0]]

    # Iterate through the sorted ranges and merge overlapping ones
    for current_start, current_end in sorted_ranges[1:]:
        # Get the last range added to our merged list
        last_start, last_end = merged[-1]

        # Check if the current range overlaps with the last one.
        # We use <= so that ranges touching (e.g., 3-5 and 5-7) also merge.
        if current_start <= last_end:
            # Overlap detected!
            # We merge them by updating the end of the last range.
            # We take the max() because the current range might end
            # before the previous one (e.g., 10-20 and 12-15).
            new_end = max(last_end, current_end)
            merged[-1] = (last_start, new_end)
        else:
            # No overlap, add the current range to merged ranges
            merged.append((current_start, current_end))

    # Calculate the total count of fresh ingredient IDs from merged ranges
    fresh_id_cnt = 0
    for start, end in merged:
        range_size = (end - start) + 1
        fresh_id_cnt += range_size

    return fresh_id_cnt


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
    assert solution_part2 == 333892124923577


if __name__ == '__main__':
    test()
    main()
