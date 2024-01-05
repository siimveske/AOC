import collections
import os


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def print_lines(p1, p2):
    diff = [a - b for a, b in zip(p1, p2)]
    str_diff = map(str, diff)

    print(','.join(str_diff))
    # if any(i > 0 for i in diff):
    #     print(','.join(str_diff))


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    lines = []
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            l, r = line.split('~')
            p1, p2 = tuple(map(int, l.split(','))), tuple(map(int, r.split(',')))
            lines.append((p1, p2))
    return lines


def line_to_segment(a, b):
    x0, y0, z0 = a
    x1, y1, z1 = b
    segment = []

    # For horizontal segments (x-axis)
    if y0 == y1 and z0 == z1:
        for x in range(x0, x1 + 1) if x0 <= x1 else range(x0, x1 - 1, -1):
            segment.append((x, y0, z0))

    # For vertical segments (y-axis)
    elif x0 == x1 and z0 == z1:
        for y in range(y0, y1 + 1) if y0 <= y1 else range(y0, y1 - 1, -1):
            segment.append((x0, y, z0))

    # For depth segments (z-axis)
    elif x0 == x1 and y0 == y1:
        for z in range(z0, z1 + 1) if z0 <= z1 else range(z0, z1 - 1, -1):
            segment.append((x0, y0, z))

    return segment


def get_supports(segments, segment):
    result = []
    for idseg, seg in segments.items():
        for point in segment:
            if point in seg:
                result.append(idseg)
                break
    return result


def part1(input_file: str) -> int:
    lines = read_input(input_file)
    sorted_lines = sorted(lines, key=lambda x: x[0][2])
    segments = [line_to_segment(a, b) for a, b in sorted_lines]
    supported = {i: [] for i in range(len(segments))}
    supporting = {i: [] for i in range(len(segments))}
    processed = dict()
    for idx, segment in enumerate(segments):
        while True:
            nxt = [(x, y, z - 1) for x, y, z in segment]
            if nxt[0][2] <= 0:
                processed[idx] = segment
                break
            supports = get_supports(processed, nxt)
            if supports:
                supported[idx] = supports
                for i in supports:
                    supporting[i].append(idx)
                processed[idx] = segment
                break
            segment = nxt
        segments[idx] = segment

    can_be_removed = set()
    cant_be_removed = set()
    for k, v in supporting.items():
        if not v:
            can_be_removed.add(k)
    for k, v in supported.items():
        if len(v) > 1:
            can_be_removed.update(v)

    result = len(can_be_removed)
    return result


def part2(input_file: str) -> int:
    grid, start = read_input(input_file)


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    part1(filename)
    assert part1(filename) == 5
    print('Part 1 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename, 327)
    # print(f'Solution for Part 2: {solution_part2}\n')

    # assert solution_part1 == 3572
    # assert solution_part2 == 594606492802848


if __name__ == '__main__':
    test()
    main()
