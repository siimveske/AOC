import os

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

SCORE_MAP = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        chunks = [line.strip() for line in f]
    return chunks


def part1(inputFile: str):
    chunks = readInput(inputFile)

    points = 0
    for line in chunks:
        stack = []
        for character in line:
            if character in CHUNK_MAP.keys():
                stack.append(CHUNK_MAP[character])
            else:
                expected_stop = stack.pop()
                if character != expected_stop:
                    points += VALUE_MAP[character]
                    break
    return points


def part2(inputFile):
    chunks = readInput(inputFile)

    score_list = []
    for line in chunks:
        score = 0
        stack = []
        for character in line:
            if character in CHUNK_MAP.keys():
                stack.append(CHUNK_MAP[character])
            else:
                expected_stop = stack.pop()
                if character != expected_stop:
                    stack = []
                    break

        if stack:
            for character in stack[::-1]:
                score *= 5
                score += SCORE_MAP[character]
            score_list.append(score)

    sorted_score_list = sorted(score_list)
    mid_item_index = len(sorted_score_list) // 2
    mid_value = sorted_score_list[mid_item_index]
    return mid_value


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 26397
    print('Part 1 OK')
    assert part2(filename) == 288957
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
