from typing import List

def test():
    entries = [1721, 979, 366, 299, 675, 1456]
    return solve(entries)

def solve(entries: List[int]):
    for i in range(len(entries)):
        entry1 = entries[i]
        for j in range(len(entries)):
            if i != j:
                entry2 = entries[j]
                if entry1+entry2 == 2020:
                    return entry1*entry2
    return 0


if __name__ == "__main__":
    print("solution: %s" % test())