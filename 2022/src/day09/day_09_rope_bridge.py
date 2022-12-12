import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    commands = []
    with open(input_file_path, 'r') as f:
        for line in f:
            direction, value = line.split()
            commands.append((direction, int(value)))
    return commands


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)
    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)}
    visited = set([(0, 0)])
    head = (0, 0)
    tail = (0, 0)

    for cmd, val in commands:
        for i in range(val):
            head_x, head_y = head
            tail_x, tail_y = tail
            delta_x, delta_y = directions[cmd]
            new_head_x = head_x + delta_x
            new_head_y = head_y + delta_y
            if abs(new_head_x - tail_x) > 1 or abs(new_head_y - tail_y) > 1:
                tail = (head_x, head_y)
                visited.add(tail)
            head = (new_head_x, new_head_y)

    return len(visited)


def part2(inputFile: str) -> int:
    grid = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    # assert part2(filename) == 8
    # print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 5907
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # assert solution_part2 == 287040
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
