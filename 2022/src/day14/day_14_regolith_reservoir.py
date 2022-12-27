import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    rocks = set()
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(' -> ')
            line = [pair.split(',')for pair in line]
            for idx in range(len(line) - 1):
                x1 = int(line[idx][0])
                y1 = int(line[idx][1])
                x2 = int(line[idx + 1][0])
                y2 = int(line[idx + 1][1])
                if x1 == x2:  # vertical segment
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        rocks.add((x1, y))
                        min_y = min(min_y, y)
                        max_y = max(max_y, y)
                else:  # horizontal segment
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        rocks.add((x, y1))
                        min_x = min(min_x, x)
                        max_x = max(max_x, x)

    return (rocks, min_x, max_x, min_y, max_y)


def simulate(cave: tuple) -> bool:
    x, y = 500, 0
    rocks, min_x, max_x, min_y, max_y = cave
    while True:
        if y >= max_y:
            return False
        if x < min_x or x > max_x:
            return False

        down = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x + 1, y + 1)
        if down not in rocks:
            x, y = down
            continue
        elif left not in rocks:
            x, y = left
            continue
        elif right not in rocks:
            x, y = right
            continue
        else:
            rocks.add((x, y))
            return True


def simulate2(cave: tuple) -> bool:
    x, y = 500, 0
    rocks, min_x, max_x, min_y, max_y = cave
    max_y += 2
    while True:
        if (499, 1) in rocks and (500, 1) in rocks and (501, 1) in rocks:
            return False

        down = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x + 1, y + 1)
        if down not in rocks and down[1] < max_y:
            x, y = down
            continue
        elif left not in rocks and down[1] < max_y:
            x, y = left
            continue
        elif right not in rocks and down[1] < max_y:
            x, y = right
            continue
        else:
            rocks.add((x, y))
            return True


def part1(inputFile: str) -> int:
    cave = readInput(inputFile)
    cnt = 0
    while simulate(cave):
        cnt += 1
    return cnt


def part2(inputFile: str):
    cave = readInput(inputFile)
    cnt = 1
    while simulate2(cave):
        cnt += 1
    return cnt


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 24
    print('Part 1 OK')

    assert part2(filename) == 93
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 610
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    assert solution_part2 == 27194
    print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
