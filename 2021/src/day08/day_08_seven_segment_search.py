from io import RawIOBase
import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            segments, digits = line.split(' | ')
            segments = [frozenset(segment) for segment in segments.strip().split()]
            digits = [frozenset(digit) for digit in digits.strip().split()]
            data.append((segments, digits))
    return data


def part1(inputFile: str):
    data = readInput(inputFile)
    result = 0
    for _, digits in data:
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                result += 1
    return result


def part2(inputFile: str):
    data = readInput(inputFile)
    return decodeSegments(data)


def _decodeUniqueSegments(segments: list, segment_map: dict, digit_map: defaultdict):
    for segment in segments:
        segment_length = len(segment)

        if segment in segment_map or segment_length not in [2, 3, 4, 7]:
            continue

        # 1,4,7 and 8 have unique segment length
        if segment_length == 2:
            segment_map[segment] = 1
            digit_map[1] = segment
        elif segment_length == 3:
            segment_map[segment] = 7
            digit_map[7] = segment
        elif segment_length == 4:
            segment_map[segment] = 4
            digit_map[4] = segment
        elif segment_length == 7:
            segment_map[segment] = 8
            digit_map[8] = segment


def decodeSegments(data: list):
    result = 0
    for segments, digits in data:
        segment_map = {}
        digit_map = defaultdict(set)
        _decodeUniqueSegments(digits, segment_map, digit_map)
        _decodeUniqueSegments(segments, segment_map, digit_map)

        for segment in segments:
            if segment in segment_map:
                continue

            segment_length = len(segment)

            # 2, 3 and 5 have 5 segments
            if segment_length == 5:
                # Only 2 has 2 common segments with 4
                if len(segment & digit_map[4]) == 2:
                    segment_map[segment] = 2
                    digit_map[2] = segment
                # 3 has 3 common segments with 7
                # and 2 common segments with 1
                elif len(segment & digit_map[7]) == 3 or len(segment & digit_map[1]) == 2:
                    segment_map[segment] = 3
                    digit_map[3] = segment
                # If it's not 2 or 3 then it has to be 5
                else:
                    segment_map[segment] = 5
                    digit_map[5] = segment

            # 0, 6 and 9 have 6 segments
            else:
                # Only 4 and 9 have 4 common segments
                if len(segment & digit_map[4]) == 4:
                    segment_map[segment] = 9
                    digit_map[9] = segment

                # 6 has 1 common segment with 1
                # and 2 common segments with 7
                elif len(segment & digit_map[1]) == 1 or len(segment & digit_map[7]) == 2:
                    segment_map[segment] = 6
                    digit_map[6] = segment

                # If it's not 6 or 9 then it has to be 0
                else:
                    segment_map[segment] = 0
                    digit_map[0] = segment

        if len(segment_map) != 10:
            raise Exception("Failed to decode all input segments")

        # decode output numbers
        output = ''
        for digit in digits:
            output += str(segment_map[digit])
        result += int(output)

    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 26
    print('Part 1 OK')
    assert part2(filename) == 61229
    print('Part 2 OK')


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
