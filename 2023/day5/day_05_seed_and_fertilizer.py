import math
import os
import re
from collections import deque


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    almanac = []
    p = re.compile(r'\d+')
    with open(input_file_path, 'r') as f:
        sections = f.read().split('\n\n')
        seeds = [int(number) for number in p.findall(sections[0])]
        almanac.append(seeds)

        for i in range(1, len(sections)):
            section = []
            for line in sections[i].split('\n')[1:]:
                dst, src, length = [int(number) for number in p.findall(line)]
                data = [src, src + length, dst - src]
                section.append(data)
            section.sort(key=lambda x: x[0])
            almanac.append(section)

    return almanac


def part1(input_file: str) -> int:
    almanac = read_input(input_file)
    seeds = almanac[0]
    mappings = almanac[1:]

    lowest_location_number = math.inf
    for seed in seeds:
        for m in mappings:
            for row in m:
                left, right, delta = row
                if left <= seed < right:
                    seed += delta
                    break
        lowest_location_number = min(lowest_location_number, seed)

    return lowest_location_number


def part2(input_file: str) -> int:
    """Solution from: https://github.com/mebeim/aoc/tree/master/2023#day-5---if-you-give-a-seed-a-fertilizer"""

    almanac = read_input(input_file)
    seeds = almanac[0]
    mappings = almanac[1:]
    segments = deque([(i, i + j) for i, j in zip(seeds[::2], seeds[1::2])])

    for mapping in mappings:
        processed = deque()
        while segments:
            a, b = segments.popleft()
            for c, d, delta in mapping:
                partial_left = c <= a < d
                partial_right = c < b <= d

                if partial_left and partial_right:
                    # Complete overlap:
                    #     a---b
                    # c-----------d
                    # Entire [a, b) segment is converted
                    processed.append((a + delta, b + delta))
                    break

                if partial_left:
                    # Partial left overlap:
                    #     a------b
                    # c------d
                    # [a, d) is converted
                    processed.append((a + delta, d + delta))
                    # [d, b) may overlap with other segments, keep it
                    segments.append((d, b))
                    break

                if partial_right:
                    # Partial right overlap:
                    # a------b
                    #     c------d
                    # [a, d) is converted
                    processed.append((c + delta, b + delta))
                    # [a, c) may overlap with other segments, keep it
                    segments.append((a, c))
                    break

                if a < c and b > d:
                    # Partial inner overlap:
                    # a-----------b
                    #     c---d
                    # [c, d) is converted
                    processed.append((c + delta, d + delta))
                    # [a, c) may overlap with other segments, keep it
                    segments.append((a, c))
                    # [d, b) may overlap with other segments, keep it
                    segments.append((d, b))
                    break
            else:
                # No overlap with any segment in this mapping, keep as is
                processed.append((a, b))
        segments = processed
    return min(s[0] for s in segments)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 35
    print('Part 1 OK')

    assert part2(filename) == 46
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 196167384
    assert solution_part2 == 125742456


if __name__ == '__main__':
    test()
    main()
