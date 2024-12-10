import os


def read_input(filename: str) -> list[int]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    with open(input_path, "r") as file:
        data = file.read().strip()
        return list(map(int, data))

def part1(input_file: str) -> int:
    data = read_input(input_file)

    # build disk
    disk = []
    for i, number in enumerate(data):
        if i % 2 == 0:
            disk += [i // 2] * number
        else:
            disk += ["."] * number

    # defragment disk
    idx_free_space = disk.index(".")
    idx = len(disk) - 1
    while idx > idx_free_space:
        disk[idx_free_space], disk[idx] = disk[idx], disk[idx_free_space]
        # update free space index
        while disk[idx_free_space] != "." and idx_free_space < len(disk) - 1:
            idx_free_space += 1
        # update index
        idx -= 1

    checksum = 0
    for i, number in enumerate(disk):
        if number != ".":
            checksum += (i * number)
    return checksum

def part2(input_file: str) -> int:
    """Calculate the checksum of the disk after defragmentation."""
    disk_data = read_input(input_file)

    # Build disk
    disk = []
    free_space_info = []  # store info about free space (length, start_idx, end_idx)
    file_info = []  # store info about files (length, start_idx, end_idx)
    idx = 0
    for i, block_size in enumerate(disk_data):
        if i % 2 == 0:
            disk += [i // 2] * block_size
            file_info.append((block_size, idx))
        else:
            if not block_size:
                continue
            disk += ["."] * block_size
            free_space_info.append((block_size, idx))
        idx += block_size

    # Defragment disk
    idx = len(disk) - 1
    for file_block in reversed(file_info):
        file_size, file_start_idx = file_block
        for idx_free_slot, free_slot in enumerate(free_space_info):
            free_size, free_start_idx = free_slot
            if free_start_idx >= file_start_idx:
                break
            if free_size >= file_size:
                file_id = disk[file_start_idx]
                for i in range(free_start_idx, free_start_idx + file_size):
                    disk[i] = file_id
                for i in range(file_start_idx, file_start_idx + file_size):
                    disk[i] = "."
                new_free_size = free_size - file_size
                new_free_start_idx = free_start_idx + file_size
                free_space_info[idx_free_slot] = (new_free_size, new_free_start_idx)
                break

    # Calculate checksum
    checksum = 0
    for i, number in enumerate(disk):
        if number != ".":
            checksum += (i * number)
    return checksum

def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1928
    print('Part 1 OK')

    assert part2(filename) == 2858
    print('Part 2 OK')

def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 6299243228569
    assert solution_part2 == 6326952672104


if __name__ == '__main__':
    test()
    main()
