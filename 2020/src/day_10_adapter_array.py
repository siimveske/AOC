import os


def load_program(file: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        program = [int(line) for line in file]

    return program


def get_differences(joltage_ratings):
    joltage_ratings.sort()
    differences = [0, 0, 0, 0]
    
    # difference between charging outlet and lowerst rated adapter
    differences[joltage_ratings[0]] += 1
    # difference between device's built-in adapter and highest rated adapter is always 3
    differences[3] += 1
    
    for i in range(1, len(joltage_ratings)):
        difference = joltage_ratings[i] - joltage_ratings[i - 1]
        differences[difference] += 1

    return differences


def test():
    print('---- TEST ----')
    
    file = os.path.join('..', 'test', 'day_10_input.txt')
    joltage_ratings = load_program(file)
    differences = get_differences(joltage_ratings)
    
    assert differences[1] == 7
    assert differences[3] == 5
    print('part1: ', differences[1] * differences[3])


def main():
    print('\n---- PROGRAM ----')
    
    file = os.path.join('..', 'data', 'day_10_input.txt')
    joltage_ratings = load_program(file)
    differences = get_differences(joltage_ratings)
    
    print('part1: ', differences[1] * differences[3])


if __name__ == '__main__':
    test()
    main()
