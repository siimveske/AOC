import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            data.append([int(i) for i in line.strip()])
    return data


def part1(inputFile: str):
    data = readInput(inputFile)

    low_points = []
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            up = i - 1
            if up >= 0 and data[up][j] <= data[i][j]:
                continue
            down = i + 1
            if down < rows and data[down][j] <= data[i][j]:
                continue
            left = j - 1
            if left >= 0 and data[i][left] <= data[i][j]:
                continue
            right = j + 1
            if right < cols and data[i][right] <= data[i][j]:
                continue

            low_points.append(data[i][j])
            print(f'{i},{j}')

    result = sum([i + 1 for i in low_points])
    return result


def part2(inputFile: str):
    data = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 15
    print('Part 1 OK')
    #assert part2(filename) == 61229
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
