import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    sections = []
    with open(input_file_path, 'r') as f:
        for line in f:
            first, second = line.split(',')
            start1, stop1 = map(int, first.split('-'))
            start2, stop2 = map(int, second.split('-'))
            sections.append((start1, stop1, start2, stop2))

    return sections


def part1(inputFile: str) -> int:
    sections = readInput(inputFile)

    overlap_count = 0
    for start1, stop1, start2, stop2 in sections:
        # first section is inside the second section
        if start1 >= start2 and stop1 <= stop2:
            overlap_count += 1
        # second section is inside the first section
        elif start2 >= start1 and stop2 <= stop1:
            overlap_count += 1

    return overlap_count


def part2(inputFile: str) -> int:
    sections = readInput(inputFile)

    overlap_count = 0
    for start1, stop1, start2, stop2 in sections:
        start1_overlaps = start2 <= start1 <= stop2
        stop1_overlaps = start2 <= stop1 <= stop2
        start2_overlaps = start1 <= start2 <= stop1
        stop2_overlaps = start1 <= stop2 <= stop1
        if start1_overlaps or stop1_overlaps or start2_overlaps or stop2_overlaps:
            overlap_count += 1

    return overlap_count


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 2
    print('Part 1 OK')
    assert part2(filename) == 4
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
