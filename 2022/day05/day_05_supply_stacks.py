import os
from collections import defaultdict
from collections import deque


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        crate_map, instructions = f.read().split('\n\n')
        crate_map = crate_map.split('\n')

        # parse crate map
        rows = len(crate_map) - 1
        stacks = defaultdict(deque)
        for row in range(rows):
            line = crate_map[row]
            for col in range(len(line) // 4 + 1):
                start = col * 4
                stop = start + 4
                crate = line[start:stop].strip()
                if crate:
                    stacks[col + 1].appendleft(crate[1])

        # parse instructions
        commands = []
        for instruction in instructions.split('\n'):
            parts = instruction.split()
            commands.append((int(parts[1]), int(parts[3]), int(parts[5])))

    return (stacks, commands)


def get_top_crates(stacks: deque) -> str:
    top_crates = []
    for i in range(1, len(stacks) + 1):
        top_crate = stacks[i][-1]
        top_crates.append(top_crate)
    return ''.join(top_crates)


def part1(inputFile: str) -> int:
    stacks, commands = readInput(inputFile)
    for cmd in commands:
        cnt, src, dst = cmd
        for _ in range(cnt):
            crate = stacks[src].pop()
            stacks[dst].append(crate)

    return get_top_crates(stacks)


def part2(inputFile: str) -> int:
    stacks, commands = readInput(inputFile)
    for cmd in commands:
        cnt, src, dst = cmd
        tmp_stack = []
        for _ in range(cnt):
            crate = stacks[src].pop()
            tmp_stack.append(crate)
        for _ in range(len(tmp_stack)):
            crate = tmp_stack.pop()
            stacks[dst].append(crate)

    return get_top_crates(stacks)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 'CMZ'
    print('Part 1 OK')
    assert part2(filename) == 'MCD'
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
