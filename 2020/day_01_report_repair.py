import os


class Version:
    part1 = 1
    part2 = 2
    
    
def test():
    print("---- TEST -----")
    
    entries = [1721, 979, 366, 299, 675, 1456]
    part1_solution = solve(entries, Version.part1)
    part2_solution = solve(entries, Version.part2)
    
    assert part1_solution == 514579
    assert part2_solution == 241861950
    
    print("---- END TEST -----\n")

def main():
    print("---- PROGRAM ----")
    
    input_file = "day_01_input.txt"
    data = readInput(input_file)
    part1_solution = solve(data, Version.part1)
    part2_solution = solve(data, Version.part2)
    
    print("---- END PROGRAM ----\n")
    print("Solution Part 1: %s" % part1_solution)
    print("Solution Part 2: %s" % part2_solution)
        
def solve(entries: [int], version: Version):
    solution        = 0
    expectedSum     = 2020 
    numberOfEntries = len(entries)
    
    if version == Version.part1:
        print("[ PART: 1 ]")
        for i in range(numberOfEntries):
            entry1 = entries[i]
            for j in range(numberOfEntries):
                if i != j:
                    entry2 = entries[j]
                    if entry1+entry2 == expectedSum:
                        solution = entry1*entry2
                        print("%s + %s == 2020" % (entry1, entry2))
                        print("%s * %s == %s" % (entry1, entry2, solution))
                        return solution
    elif version == Version.part2:
        print("[ PART: 2 ]")
        for i in range(numberOfEntries):
            entry1 = entries[i]
            for j in range(numberOfEntries):
                if i != j:
                    entry2 = entries[j]
                    for k in range(numberOfEntries):
                        if i != k and j !=k:
                            entry3 = entries[k]
                            if entry1+entry2+entry3 == expectedSum:
                                solution = entry1*entry2*entry3
                                print("%s + %s + %s == 2020" % (entry1, entry2, entry3))
                                print("%s * %s * %s == %s" % (entry1, entry2, entry3, solution))
                                return solution
    else:
        raise Exception("Invalid version!")
    
    return solution

def readInput(filename: str):
    data = []
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    with open(input_file_path, "r") as f:
        for line in f:
            data.append(int(line))
        f.close()
    
    return data


if __name__ == "__main__":
    test()
    main()
