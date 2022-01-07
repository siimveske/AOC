import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            data.append([int(i) for i in line.strip()])
    return data


def evolve(energy_map):
    rows = len(energy_map)
    cols = len(energy_map[0])
    flash_cnt = 0
    new_map = [[0] * cols for i in range(rows)]

    for row in range(rows):
        for col in range(cols):
            top = (row - 1, col)
            top_right = (row - 1, col + 1)
            right = (row, col + 1)
            bottom_right = (row + 1, col + 1)
            bottom = (row + 1, col)
            bottom_left = (row + 1, col - 1)
            left = (row, col - 1)
            top_left = (row - 1, col - 1)

            neighbours = [top, top_right, right, bottom_right, bottom, bottom_left, left, top_left]
            filtered_neighbours = [(i, j) for i, j in neighbours if (i >= 0 and i < rows) and (j >= 0 and j < cols)]

            energy_level = energy_map[row][col] + 1
            for i, j in filtered_neighbours:
                if (energy_map[i][j] + 1) > 9:
                    energy_level += 1
            if energy_level > 9:
                energy_level = 0
                flash_cnt += 1
            new_map[row][col] = energy_level

    return (new_map, flash_cnt)


def part1(inputFile: str):
    data = readInput(inputFile)

    new_map = data
    total_flash_cnt = 0
    for i in range(10):
        n_map, f_cnt = evolve(new_map)
        new_map = n_map
        total_flash_cnt += f_cnt


def part2(inputFile):
    chunks = readInput(inputFile)
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 26397
    print('Part 1 OK')
    #assert part2(filename) == 288957
    #print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    # main()
