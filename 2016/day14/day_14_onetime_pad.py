import hashlib
import re


def part1(salt: str) -> int:
    idx = -1
    num_of_keys = 0

    pattern = r'(.)\1\1'
    md5_cache = {}

    def get_md5(s):
        md5_cache[s] = hashlib.md5(s.encode()).hexdigest()
        return md5_cache[s]

    while num_of_keys < 64:

        idx += 1
        md5_hash = get_md5(f"{salt}{idx}")

        matches = re.search(pattern, md5_hash)

        if matches:
            character = matches.group(1)
            sequence = character * 5
            for i in range(idx + 1, idx + 1001):
                md5_hash = get_md5(f"{salt}{i}")
                if sequence in md5_hash:
                    num_of_keys += 1
                    break
    return idx


def part2(salt: str) -> int:
    idx = -1
    num_of_keys = 0
    pattern = r'(.)\1\1'
    md5_cache = {}

    def get_md5(s, rounds=2017):
        if s not in md5_cache:
            result = s
            for _ in range(rounds):
                result = hashlib.md5(result.encode()).hexdigest()
            md5_cache[s] = result
        return md5_cache[s]

    while num_of_keys < 64:
        idx += 1
        md5_hash = get_md5(f"{salt}{idx}")

        matches = re.search(pattern, md5_hash)
        if matches:
            character = matches.group(1)
            sequence = character * 5
            for i in range(idx + 1, idx + 1001):
                md5_hash = get_md5(f"{salt}{i}")
                if sequence in md5_hash:
                    num_of_keys += 1
                    break
    return idx


def test():
    print("---- TEST ----")

    salt = "abc"

    assert part1(salt) == 22728
    print("Part 1: OK")

    assert part2(salt) == 22551
    print("Part 2: OK")


def main():
    print("---- MAIN ----")

    salt = "ngcjuoqr"
    solution_part1 = part1(salt)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 18626

    solution_part2 = part2(salt)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 20092


if __name__ == "__main__":
    test()
    main()
