import os
from collections import Counter
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    instructions = {}
    with open(input_file_path, 'r') as f:
        template = f.readline().strip()
        f.readline()
        for line in f:
            key, value = line.split('->')
            instructions[key.strip()] = value.strip()
    return (template, instructions)


def insert(template, instructions):
    result = ''
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        result += (pair[0] + instructions[pair])
    result += pair[1]
    return result


def get_min_max(counter: dict):

    # Find max and min occurences
    max_item = float('-inf')
    min_item = float('inf')
    for i in counter.values():
        if i > max_item:
            max_item = i
        if i < min_item:
            min_item = i

    return (min_item, max_item)


def part1(inputFile: str):
    template, instructions = readInput(inputFile)

    # Build the polymer
    for i in range(10):
        template = insert(template, instructions)

    # Count letter occurences
    counter = Counter(template)

    # Find max and min occurences
    min_item, max_item = get_min_max(counter)

    # Calulate difference
    result = max_item - min_item

    return result


def part2(inputFile: str):
    template, instructions = readInput(inputFile)

    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        pairs[pair] += 1

    # build pair count table
    for _ in range(40):
        newpairs = defaultdict(int)
        for pair, count in pairs.items():
            letter = instructions[pair]
            newpairs[pair[0] + letter] += count
            newpairs[letter + pair[1]] += count
        pairs = newpairs

    # count first letters of all pairs
    counter = defaultdict(int)
    for pair, count in pairs.items():
        counter[pair[0]] += count
    counter[template[-1:]] += 1  # include last letter from initial polymer

    # Find max and min occurences
    min_item, max_item = get_min_max(counter)

    # Calulate difference
    result = max_item - min_item

    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 1588
    print('Part 1 OK')

    solution_part2 = part2(filename)
    assert solution_part2 == 2188189693529
    print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
