import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        lines = [line.strip() for line in f]

    return lines


def parse_tree(terminal_output: list):
    tree = {}
    stack = []
    for line in terminal_output:
        if line.startswith('$'):
            if 'cd' in line:
                if '..' in line:
                    stack.pop()
                else:
                    folder = line.split(' ')[2]
                    stack.append(folder)
                    path = ','.join(stack)
                    tree[path] = {'files': [], 'folders': []}
        else:
            path = ','.join(stack)
            if line.startswith('dir'):
                child_folder = line.split(' ')[1]
                tree[path]['folders'].append(child_folder)
            else:
                size, name = line.split(' ')
                tree[path]['files'].append((int(size), name))

    return tree


def get_folder_size(tree: dict, folder: str) -> int:
    size = 0
    stack = [folder]
    while stack:
        current_folder = stack.pop()
        files = tree[current_folder]['files']
        folders = tree[current_folder]['folders']
        size += sum([f[0] for f in files])
        stack += [current_folder + ',' + f for f in folders]
    return size


def part1(inputFile: str) -> int:
    terminal_output = readInput(inputFile)
    tree = parse_tree(terminal_output)
    solution = 0
    max_folder_size = 100000
    for folder in tree.keys():
        folder_size = get_folder_size(tree, folder)
        if folder_size <= max_folder_size:
            solution += folder_size
    return solution


def part2(inputFile: str) -> int:
    terminal_output = readInput(inputFile)
    tree = parse_tree(terminal_output)
    used_space = get_folder_size(tree, '/')
    total_disk_space = 70000000
    space_available = total_disk_space - used_space
    space_needed = 30000000
    space_missing = space_needed - space_available

    closest_size = float('inf')
    for folder in tree.keys():
        current_folder_size = get_folder_size(tree, folder)
        if current_folder_size < space_missing:
            continue
        delta = current_folder_size - space_missing
        if delta < closest_size:
            closest_size = current_folder_size

    return closest_size


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
