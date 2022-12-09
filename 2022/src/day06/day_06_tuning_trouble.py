import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read()

    return data


def part1(inputFile: str) -> int:
    data = readInput(inputFile)
    for i in range(len(data) - 3):
        segment_start = i
        segment_stop = i + 4
        segment = data[segment_start:segment_stop]
        if len(set(segment)) == 4:
            return segment_stop


def part2(inputFile: str) -> int:
    data = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 7
    print('Part 1 OK')
    #@assert part2(filename) == 'MCD'
    #rint('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
