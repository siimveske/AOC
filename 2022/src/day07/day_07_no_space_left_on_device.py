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
                    tree[folder] = {'files': [], 'folders': []}
        else:
            current_folder = stack[-1]
            if line.startswith('dir'):
                child_folder = line.split(' ')[1]
                tree[current_folder]['folders'].append(child_folder)
            else:
                size, name = line.split(' ')
                tree[current_folder]['files'].append((int(size), name))

    return tree


def get_folder_size(tree: dict, folder: str) -> int:
    size = 0
    stack = [folder]
    while stack:
        current_folder = stack.pop()
        files = tree[current_folder]['files']
        folders = tree[current_folder]['folders']
        size += sum([f[0] for f in files])
        stack += folders
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
    data = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 95437
    print('Part 1 OK')
    #assert part2(filename) == 19
    #print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
