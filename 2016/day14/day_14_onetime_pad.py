import hashlib
import re


def part1(salt: str) -> int:
    idx = -1
    num_of_keys = 0

    pattern = r'(.)\1\1'

    while num_of_keys < 64:

        idx += 1
        md5_hash = f"{salt}{idx}"
        md5_hash = md5_hash.encode()
        md5_hash = hashlib.md5(md5_hash).hexdigest()

        matches = re.search(pattern, md5_hash)

        if matches:
            character = matches.group(1)
            sequence = character * 5
            for i in range(idx + 1, idx + 1001):
                md5_hash = f"{salt}{i}"
                md5_hash = md5_hash.encode()
                md5_hash = hashlib.md5(md5_hash).hexdigest()
                if sequence in md5_hash:
                    num_of_keys += 1
                    break
    return idx


def part2() -> int:
    pass


def test():
    print("---- TEST ----")

    assert part1(salt="abc") == 22728
    print("Part 1: OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1(salt="ngcjuoqr")
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 18626

    # solution_part2 = part2()
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 141


if __name__ == "__main__":
    test()
    main()
