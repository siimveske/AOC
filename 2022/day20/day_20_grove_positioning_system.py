import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        coordinates = [*enumerate(int(i) for i in f)]
    return coordinates


def mix(coordinates, times=1):
    numbers = list(coordinates)
    numbers_length = len(coordinates)

    for _ in range(times):
        for coordinate in coordinates:
            idx = numbers.index(coordinate)
            item = numbers.pop(idx)
            new_idx = (idx + item[1]) % len(numbers)
            numbers.insert(new_idx, item)

    for zero_idx, coordinate in enumerate(numbers):
        _, val = coordinate
        if val == 0:
            break

    result = numbers[(zero_idx + 1000) % numbers_length][1]
    result += numbers[(zero_idx + 2000) % numbers_length][1]
    result += numbers[(zero_idx + 3000) % numbers_length][1]

    return result


def part1(inputFile: str):
    coordinates = readInput(inputFile)
    return mix(coordinates)


def part2(inputFile: str):
    coordinates = readInput(inputFile)
    decryption_key = 811589153
    coordinates = [(idx, val * decryption_key) for idx, val in coordinates]
    return mix(coordinates, times=10)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 3
    print('Part 1 OK')

    assert part2(filename) == 1623178306
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 3346

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 4265712588168


if __name__ == '__main__':
    test()
    main()
