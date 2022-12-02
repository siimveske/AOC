import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    calories = []
    with open(input_file_path, 'r') as f:
        elves = f.read().split('\n\n')
        for inventory in elves:
            parsed_calories = [int(item) for item in inventory.split()]
            calories.append(parsed_calories)

    return calories


def part1(inputFile: str):

    calories = readInput(inputFile)
    totals = [sum(c)for c in calories]
    max_calorie = max(totals)
    return max_calorie


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
    assert part1(filename) == 24000
    print('Part 1 OK')
    #assert part2(filename) == 5
    #print('Part 2 OK\n')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(filename)
    #print(f'Solution for Part 1: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
