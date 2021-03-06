import os


class Version:
    part1 = 1
    part2 = 2


def test():
    print('---- TEST -----')

    entries = [1721, 979, 366, 299, 675, 1456]
    part1_solution = solve(entries, Version.part1)
    part2_solution = solve(entries, Version.part2)

    assert part1_solution == 514579
    assert part2_solution == 241861950

    print('---- END TEST -----\n')


def main():
    print('---- PROGRAM ----')

    input_file = os.path.join('..', 'data', 'day_01_input.txt')
    data = readInput(input_file)
    part1_solution = solve(data, Version.part1)
    part2_solution = solve(data, Version.part2)

    print('---- END PROGRAM ----\n')
    print(f'Solution Part 1: {part1_solution}')
    print(f'Solution Part 2: {part2_solution}')


def solve(entries: list[int], version: Version):
    '''
        Example combinations for list [172, 979, 366, 299, 675]
        --- Part 1 ---
        172 979 - 0 1
        172 366 - 0 2
        172 299 - 0 3
        172 675 - 0 4
        979 366 - 1 2
        979 299 - 1 3
        979 675 - 1 4
        366 299 - 2 3
        366 675 - 2 4
        299 675 - 3 4
        
        --- Part 2 ---
        172 979 366 - 0 1 2
        172 979 299 - 0 1 3
        172 979 675 - 0 1 4
        172 366 299 - 0 2 3
        172 366 675 - 0 2 4
        172 299 675 - 0 3 4
        979 366 299 - 1 2 3
        979 366 675 - 1 2 4
        979 299 675 - 1 3 4
        366 299 675 - 2 3 4
    '''

    solution = 0
    expectedSum = 2020
    numberOfEntries = len(entries)

    if version == Version.part1:
        print('[ PART: 1 ]')
        for i in range(numberOfEntries - 1):
            entry1 = entries[i]
            for j in range(i + 1, numberOfEntries):
                entry2 = entries[j]
                if entry1 + entry2 == expectedSum:
                    solution = entry1 * entry2
                    print(f'{entry1} + {entry2} == 2020')
                    print(f'{entry1} * {entry2} == {solution}')
                    return solution
    
    elif version == Version.part2:
        print('[ PART: 2 ]')
        for i in range(numberOfEntries - 2):
            entry1 = entries[i]
            for j in range(i + 1, numberOfEntries - 1):
                entry2 = entries[j]
                for k in range(j + 1, numberOfEntries):
                    entry3 = entries[k]
                    if entry1 + entry2 + entry3 == expectedSum:
                        solution = entry1 * entry2 * entry3
                        print(f'{entry1} + {entry2} + {entry3} == 2020')
                        print(f'{entry1} * {entry2} * {entry3} == {solution}')
                        return solution
    
    else:
        raise Exception('Invalid version!')

    return solution


def readInput(filename: str):
    data = []
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        for line in f:
            data.append(int(line))
        f.close()

    return data


if __name__ == '__main__':
    test()
    main()
