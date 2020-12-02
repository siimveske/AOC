import os
from typing import List

def test():
    print("---- START TEST -----")
    
    entries = [1721, 979, 366, 299, 675, 1456]
    result = solve(entries)
    assert result == 241861950
    
    print("---- END TEST -----\n")

def main():
    print("---- PROGRAM ----")
    
    input_file = "day_01_input.txt"
    data = readInput(input_file)
    solution = solve(data)
    
    print("---- END PROGRAM ----\n")
    print("Solution: %s" % solution)
        
def solve(entries: List[int]):
    solution = 0
    numberOfEntries = len(entries)
    for i in range(numberOfEntries):
        entry1 = entries[i]
        for j in range(numberOfEntries):
            if i != j:
                entry2 = entries[j]
                for k in range(numberOfEntries):
                    if i != k and j !=k:
                        entry3 = entries[k]
                        if entry1+entry2+entry3 == 2020:
                            solution = entry1*entry2*entry3
                            print("%s + %s + %s == 2020" % (entry1, entry2, entry3))
                            print("%s * %s * %s == %s" % (entry1, entry2, entry3, solution))
                            return solution
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
