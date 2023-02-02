import os
from collections import defaultdict


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        lines = [line.strip() for line in f]

    return lines


def parse_fs(terminal_output: list) -> dict:
    filesystem = {}
    stack = []
    for line in terminal_output:
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            if '..' in line:
                stack.pop()
            else:
                folder = line.split(' ')[2]
                stack.append(folder)
                path = ','.join(stack)
                filesystem[path] = {'files': [], 'folders': []}
        else:
            path = ','.join(stack)
            if line.startswith('dir'):
                child_folder = line.split(' ')[1]
                filesystem[path]['folders'].append(child_folder)
            else:
                size, name = line.split(' ')
                filesystem[path]['files'].append(int(size))

    return filesystem


def get_folder_size(filesystem: dict, path: str) -> int:
    size = 0
    stack = [path]
    while stack:
        current_folder = stack.pop()
        files = filesystem[current_folder]['files']
        folders = filesystem[current_folder]['folders']
        size += sum(files)
        stack += [f'{current_folder},{folder}' for folder in folders]
    return size


def part1(inputFile: str) -> int:
    terminal_output = readInput(inputFile)
    filesystem = parse_fs(terminal_output)
    solution = 0
    max_folder_size = 100000
    for path in filesystem:
        folder_size = get_folder_size(filesystem, path)
        if folder_size <= max_folder_size:
            solution += folder_size
    return solution


def part2(inputFile: str) -> int:
    terminal_output = readInput(inputFile)
    filesystem = parse_fs(terminal_output)
    used_space = get_folder_size(filesystem, '/')
    total_disk_space = 70000000
    space_available = total_disk_space - used_space
    space_needed = 30000000
    space_missing = space_needed - space_available

    min_size_to_free = float('inf')
    for path in filesystem:
        current_folder_size = get_folder_size(filesystem, path)
        if space_missing <= current_folder_size < min_size_to_free:
            min_size_to_free = current_folder_size

    return min_size_to_free


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 95437
    print('Part 1 OK')
    assert part2(filename) == 24933642
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
