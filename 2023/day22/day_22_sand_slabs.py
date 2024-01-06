import collections
import os


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


def interpolate(a, b):
    x0, y0, z0 = a
    x1, y1, z1 = b
    segment = []

    # For horizontal segments (x-axis)
    if y0 == y1 and z0 == z1:
        segment = [(x, y0, z0) for x in range(x0, x1 + 1)]

    # For vertical segments (y-axis)
    elif x0 == x1 and z0 == z1:
        segment = [(x0, y, z0) for y in range(y0, y1 + 1)]

    # For depth segments (z-axis)
    elif x0 == x1 and y0 == y1:
        segment = [(x0, y0, z) for z in range(z0, z1 + 1)]

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
    segments = [interpolate(a, b) for a, b in sorted_lines]
    supported = {i: [] for i in range(len(segments))}
    processed = dict()
    max_z = segments[0][-1][2]
    for idx, segment in enumerate(segments):
        while True:
            nxt = [(x, y, z - 1) for x, y, z in segment]
            if nxt[0][2] <= 0:
                processed[idx] = segment
                break
            if nxt[0][2] <= max_z:
                supports = get_supports(processed, nxt)
                if supports:
                    supported[idx] = supports
                    processed[idx] = segment
                    break
            segment = nxt
        max_z = max(max_z, segment[-1][2])  # compare known highest z val with current segment highest z val
        segments[idx] = segment

    can_be_removed = set()
    cant_be_removed = set()
    for k, v in supported.items():
        if len(v) == 1:
            cant_be_removed.add(v[0])
    for i in range(len(lines)):
        if i in cant_be_removed:
            continue
        can_be_removed.add(i)

    result = len(can_be_removed)
    return result


def count_falling(root_brick, supports, supported_by) -> int:
    """original solution: https://github.com/mebeim/aoc/blob/master/2023/solutions/day22.py"""
    q = collections.deque([root_brick])
    falling = set()

    while q:
        brick = q.popleft()
        falling.add(brick)

        for supporter in supported_by[brick]:
            if all(s in falling for s in supports[supporter]):
                q.append(supporter)

    return len(falling) - 1


def part2(input_file: str) -> int:
    lines = read_input(input_file)
    sorted_lines = sorted(lines, key=lambda x: x[0][2])
    segments = [interpolate(a, b) for a, b in sorted_lines]
    supported = {i: [] for i in range(len(segments))}
    supporting = {i: set() for i in range(len(segments))}
    processed = dict()
    max_z = segments[0][-1][2]
    for idx, segment in enumerate(segments):
        while True:
            nxt = [(x, y, z - 1) for x, y, z in segment]
            if nxt[0][2] <= 0:
                processed[idx] = segment
                break
            if nxt[0][2] <= max_z:
                supports = get_supports(processed, nxt)
                if supports:
                    supported[idx] = supports
                    for supporter in supports:
                        supporting[supporter].add(idx)
                    processed[idx] = segment
                    break
            segment = nxt
        max_z = max(max_z, segment[-1][2])  # compare known highest z val with current segment highest z val
        segments[idx] = segment

    cant_be_removed = set()
    for k, v in supported.items():
        if len(v) == 1:
            cant_be_removed.add(v[0])

    result = 0
    for node in cant_be_removed:
        result += count_falling(node, supported, supporting)

    return result


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'

    assert part1(filename) == 5
    print('Part 1 OK')

    assert part2(filename) == 7
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 497
    assert solution_part2 == 67468


if __name__ == '__main__':
    test()
    main()
