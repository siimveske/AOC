import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        
        acc = 0
        calories = []
        for line in f:
            line = line.strip()
            if line:
                acc += int(line)
            else:
                calories.append(acc)
                acc = 0
        if acc:
            calories.append(acc)
            
    return calories


def part1(inputFile: str):
    calories = readInput(inputFile)
    return max(calories)


def part2(inputFile: str):
    calories = readInput(inputFile)
    calories.sort(reverse=True)
    return calories[0] + calories[1] + calories[2]


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 24000
    print('Part 1 OK')
    assert part2(filename) == 45000
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
