import os
"""
https://github.com/mebeim/aoc/blob/master/2022/README.md#day-9---rope-bridge
"""


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    commands = []
    with open(input_file_path, 'r') as f:
        for line in f:
            direction, value = line.split()
            commands.append((direction, int(value)))
    return commands


DELTA = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def part1(inputFile: str) -> int:
    commands = readInput(inputFile)

    visited = set([(0, 0)])
    head = (0, 0)
    tail = (0, 0)

    for cmd, val in commands:
        for i in range(val):
            head_x, head_y = head
            tail_x, tail_y = tail
            delta_x, delta_y = DELTA[cmd]
            new_head_x = head_x + delta_x
            new_head_y = head_y + delta_y
            if abs(new_head_x - tail_x) > 1 or abs(new_head_y - tail_y) > 1:
                tail = (head_x, head_y)
                visited.add(tail)
            head = (new_head_x, new_head_y)

    return len(visited)


def part2(inputFile: str) -> int:
    commands = readInput(inputFile)

    rope = [(0, 0)] * 10
    visited = {(0, 0)}

    for command in commands:
        direction, steps = command
        for _ in range(steps):
            hx, hy = rope[0]
            dx, dy = DELTA[direction]

            # Move the head
            rope[0] = hx + dx, hy + dy

            for i in range(9):
                # Consider this piece as the "head"
                hx, hy = rope[i]
                # And the one after it as the "tail"
                tx, ty = rope[i + 1]

                # Do the exact same thing we did for part 1
                dx, dy = hx - tx, hy - ty
                if dx**2 + dy**2 > 2:
                    if dx != 0:
                        tx += 1 if dx > 0 else -1
                    if dy != 0:
                        ty += 1 if dy > 0 else -1
                    rope[i + 1] = (tx, ty)

            # Keep track of tail
            visited.add(tuple(rope[9]))

    return len(visited)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 13
    print('Part 1 OK')

    assert part2(filename) == 1
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 5907
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    assert solution_part2 == 2303
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
