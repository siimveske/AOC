import os
from typing import List

def test():
    entries = [1721, 979, 366, 299, 675, 1456]
    result = solve(entries)
    assert result == 514579

def solve(entries: List[int]):
    numberOfEntries = len(entries)
    for i in range(numberOfEntries):
        entry1 = entries[i]
        for j in range(numberOfEntries):
            if i != j:
                entry2 = entries[j]
                if entry1+entry2 == 2020:
                    return entry1*entry2
    return 0

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
    input_file = "day_01_input.txt"
    data = readInput(input_file)
    solution = solve(data)
    print("Solution: %s" % solution)
