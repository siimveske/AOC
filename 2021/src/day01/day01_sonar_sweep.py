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


def count_depth_measurement_increases(depth_measurements: list):
    result = 0
    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i - 1]:
            result += 1
    return result


def part1(inputFile: str):
    depth_measurements = readInput(inputFile)
    result = count_depth_measurement_increases(depth_measurements)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 7


def main():
    print('---- PART 1 ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}\n')


if __name__ == '__main__':
    #test()
    main()
