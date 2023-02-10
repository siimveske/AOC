from __future__ import annotations


def validate(string: str) -> bool:
    forbidden_letters = ["i", "o", "l"]
    i = 0
    length = len(string)
    pairs = set()
    has_abc = False
    while i < length:
        current = string[i]
        if current in forbidden_letters:
            return False
        if i + 1 < length:
            nxt = string[i + 1]
            if current == nxt:
                pairs.add(current + nxt)
        if i + 2 < length:
            a, b, c = ord(current), ord(nxt), ord(string[i + 2])
            if (a + 1 == b) and (b + 1 == c):
                has_abc = True
        i += 1

    is_valid = len(pairs) > 1 and has_abc
    return is_valid


def part1(string: str) -> int:
    result = validate(string)


def part2(inputFile: str) -> int:
    pass


def test():
    print("---- TEST ----")
    assert validate("hijklmmn") == False
    assert validate("abbceffg") == False
    assert validate("abbcegjk") == False
    print("OK\n")


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 329356

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 4666278


if __name__ == "__main__":
    test()
    # main()
