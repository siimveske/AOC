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


def next_pwd(pwd: list):
    characters = [c for c in pwd]
    for i in range(len(pwd) - 1, -1, -1):
        new_value = ord(characters[i]) + 1
        if new_value > ord("z"):
            characters[i] = "a"
        else:
            characters[i] = chr(new_value)
            break

    return "".join(characters)


def next_valid_pwd(pwd: list):
    while validate(pwd) is False:
        pwd = next_pwd(pwd)
    return pwd


def part1(pwd: str) -> int:
    result = next_valid_pwd(pwd)
    return result


def part2(pwd: str) -> int:
    pwd = next_pwd(pwd)
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
