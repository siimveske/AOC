import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    with open(input_file_path, 'r') as f:
        items = f.read().split()

    return items


def part1(inputFile: str):
    items = readInput(inputFile)  
    total = 0
    for line in items:
        midpoint = len(line) // 2
        a = line[0:midpoint]
        b = line[midpoint:]
        intersection = set(a).intersection(set(b)).pop()
        
        if intersection.islower():
            delta = 96
        else:
            delta = 38
        total += ord(intersection)-delta
    
    return total

def part2(inputFile: str):
    items = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 157
    print('Part 1 OK')
    # assert part2(filename) == 12
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
