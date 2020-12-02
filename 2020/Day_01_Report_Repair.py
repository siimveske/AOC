from typing import List

def test():
    items = [1721, 979, 366, 299, 675, 1456]
    return solve(items)

def solve(items: List[int]):
    for i in range(len(items)):
        item1 = items[i]
        for j in range(len(items)):
            if i != j:
                item2 = items[j]
                if item1+item2 == 2020:
                    return item1*item2
    return 0


if __name__ == "__main__":
    print("solution: %s" % test())