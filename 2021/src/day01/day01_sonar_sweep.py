import os


def readInput(filename: str):

    data = []
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        for line in f:
            data.append(int(line))
        f.close()

    return data


def part1(inputFile: str):

    depth_measurements = readInput(inputFile)

    result = 0
    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i - 1]:
            result += 1
    return result


def part2(inputFile: str):

    depth_measurements = readInput(inputFile)

    result = 0
    for i in range(3, len(depth_measurements)):
        block_a = sum(depth_measurements[i - 3:i])
        block_b = sum(depth_measurements[i - 2:i + 1])
        if block_a < block_b:
            result += 1
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 7
    print('Part 1 OK')
    assert part2(filename) == 5
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 1: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
