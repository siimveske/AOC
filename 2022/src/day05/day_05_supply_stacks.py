import os
from collections import defaultdict
from collections import deque


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    result = []
    with open(input_file_path, 'r') as f:
        crates, instructions = f.read().split('\n\n')
        crates = crates.split('\n')

        # parse crate map
        rows = len(crates) - 1
        stacks = defaultdict(deque)
        for row in range(rows):
            line = crates[row]
            for col in range(len(line) // 4 + 1):
                start = col * 4
                stop = start + 4
                crate = line[start:stop].strip()
                if crate:
                    stacks[col + 1].appendleft(crate[1])

        # parse instructions
        cmd = []
        for line in instructions.split('\n'):
            instruction = line.split()
            cmd.append((int(instruction[1]), int(instruction[3]), int(instruction[5])))

    return (stacks, cmd)


def part1(inputFile: str) -> int:
    stacks, commands = readInput(inputFile)
    for cmd in commands:
        cnt, src, dst = cmd
        for i in range(cnt):
            crate = stacks[src].pop()
            stacks[dst].append(crate)

    top_crates = []
    for i in range(1, len(stacks) + 1):
        top_crate = stacks[i][-1]
        top_crates.append(top_crate)

    return ''.join(top_crates)


def part2(inputFile: str) -> int:
    stacks, commands = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 'CMZ'
    print('Part 1 OK')
    #assert part2(filename) == 4
    #print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
