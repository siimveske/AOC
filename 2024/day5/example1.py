# https://github.com/oliver-ni/advent-of-code/blob/master/py/2024/day05.py

from functools import cmp_to_key


def p1(file):
    order_sections, list_sections = [section.splitlines() for section in file.read().split("\n\n")]
    order_pairs = [[int(num) for num in pair.split("|")] for pair in order_sections]
    lists = [[int(num) for num in lst.split(",")] for lst in list_sections]
    total = 0
    for numbers in lists:
        for first, second in order_pairs:
            try:
                if numbers.index(first) >= numbers.index(second):
                    break
            except ValueError:
                continue
        else:
            total += numbers[len(numbers) // 2]
    return total


def p2(file):
    order_sections, list_sections = [section.splitlines() for section in file.read().split("\n\n")]
    order_pairs = [[int(num) for num in pair.split("|")] for pair in order_sections]
    lists = [[int(num) for num in lst.split(",")] for lst in list_sections]
    total = 0
    for numbers in lists:
        for first, second in order_pairs:
            try:
                if numbers.index(first) >= numbers.index(second):
                    break
            except ValueError:
                pass
        else:
            numbers.sort(key=cmp_to_key(lambda a, b: -([a, b] in order_pairs) + ([b, a] in order_pairs)))
            total += numbers[len(numbers) // 2]
    return total

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(p1(f))
        print(p2(f))
