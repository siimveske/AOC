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
    data = read_input(input_file)

    # build disk
    disk = []
    fspace_info = []  # store info about free space (length_of_free_space, start_idx, end_idx)
    file_info = []  # store info about files (length_of_file, start_idx, end_idx)
    idx = 0
    for i, number in enumerate(data):
        if i % 2 == 0:
            disk += [i // 2] * number
            file_info.append((number, idx))
        else:
            if not number:
                continue
            disk += ["."] * number
            fspace_info.append((number, idx))
        idx += number

    # defragment disk
    idx = len(disk) - 1
    for file_block in reversed(file_info):
        file_size, file_start_idx = file_block
        for idx_free_slot, free_slot in enumerate(fspace_info):
            slot_size, slot_start_idx = free_slot
            if slot_start_idx >= file_start_idx:
                break
            if slot_size >= file_size:
                file_id = disk[file_start_idx]
                for i in range(slot_start_idx, slot_start_idx + file_size):
                    disk[i] = file_id
                for i in range(file_start_idx, file_start_idx + file_size):
                    disk[i] = '.'
                new_slot_size = slot_size - file_size
                new_slot_start_idx = slot_start_idx + file_size
                fspace_info[idx_free_slot] = (new_slot_size, new_slot_start_idx)
                break

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
