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


def add_one(letter: chr):
    old_value = ord(letter)
    new_value = old_value + 1
    carry = False
    if new_value > ord("z"):
        new_value = ord("a")
        carry = True

    return (chr(new_value), carry)


def next_pwd(string: list):
    for i in reversed(range(len(string))):
        new_value, carry = add_one(string[i])
        string[i] = new_value
        if carry is False:
            break


def next_valid_pwd(pwd: list):
    while validate(pwd) is False:
        next_pwd(pwd)
    return "".join(pwd)


def part1(pwd: str) -> int:
    pwd = [i for i in pwd]
    result = next_valid_pwd(pwd)
    return result


def part2(pwd: str) -> int:
    pwd = [i for i in pwd]
    next_pwd(pwd)
    result = next_valid_pwd(pwd)
    return result


def test():
    print("---- TEST ----")
    assert validate("hijklmmn") == False
    assert validate("abbceffg") == False
    assert validate("abbcegjk") == False
    assert part1("abcdefgh") == "abcdffaa"
    assert part1("ghijklmn") == "ghjaabcc"
    print("OK\n")


def main():
    print("---- MAIN ----")

    solution_part1 = part1("hxbxwxba")
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "hxbxxyzz"

    solution_part2 = part2(solution_part1)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == "hxcaabcc"


if __name__ == "__main__":
    test()
    main()
