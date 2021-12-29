import os
import math
from collections import defaultdict
from queue import Queue


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        chunks = [line.strip() for line in f]
    return chunks


CHUNK_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

VALUE_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part1(inputFile: str):
    chunks = readInput(inputFile)

    invalid_chunks = []
    for line in chunks:
        stack = []
        for character in line:
            if character in CHUNK_MAP.keys():
                stack.append(CHUNK_MAP[character])
            else:
                expected_stop = stack.pop()
                if character != expected_stop:
                    invalid_chunks.append(character)
                    break
    points = 0
    for i in invalid_chunks:
        points += VALUE_MAP[i]

    return points


def part2(cords, graph):
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 26397
    print('Part 1 OK')
    #assert part2(cords, graph) == 1134
    #print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(cords, graph)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
