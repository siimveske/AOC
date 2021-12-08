import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            segments, digits = line.split(' | ')
            data.append([segments.split(), digits.strip().split()])
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
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 26
    print('Part 1 OK')
    #assert part2(filename) == 168
    #print('Part 2 OK')


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
