import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as f:
        for line in f:
            data.append([int(i) for i in line.strip()])
    return data


def get_neighbours(item, rows, cols):
    row, col = item
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

    return filtered_neighbours


def evolve(energy_map):
    rows = len(energy_map)
    cols = len(energy_map[0])
    flash_cnt = 0

    flashed_octopuses = []
    for row in range(rows):
        for col in range(cols):
            new_value = energy_map[row][col] + 1
            if new_value > 9:
                flashed_octopuses.append((row, col))
                energy_map[row][col] = 0
                flash_cnt += 1
            else:
                energy_map[row][col] = new_value

    while flashed_octopuses:
        octopus = flashed_octopuses.pop()
        neighbours = get_neighbours(octopus, rows, cols)
        for row, col in neighbours:
            new_value = energy_map[row][col]
            if new_value == 0:
                continue
            else:
                new_value += 1

            if new_value > 9:
                flashed_octopuses.append((row, col))
                energy_map[row][col] = 0
                flash_cnt += 1
            else:
                energy_map[row][col] = new_value

    return flash_cnt


def part1(inputFile: str):
    energy_map = readInput(inputFile)

    total_flash_cnt = 0
    for i in range(100):
        total_flash_cnt += evolve(energy_map)

    return total_flash_cnt


def part2(inputFile: str):
    energy_map = readInput(inputFile)

    generation = 1
    while True:
        if evolve(energy_map) == 100:
            break
        else:
            generation += 1

    return generation


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 1656
    print('Part 1 OK')
    assert part2(filename) == 195
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
