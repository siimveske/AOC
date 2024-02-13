import hashlib


def part1(prefix: str) -> str:
    result = []
    idx = 0
    while len(result) < 8:
        hash_input = f"{prefix}{idx}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith("00000"):
            result.append(hash_output[5])
        idx += 1
    return "".join(result)


def part2() -> int:
    pass


def test():
    print("---- TEST ----")

    assert part1("abc") == "18f47a30"
    print("Part 1: OK")


def main():
    print("---- MAIN ----")

    solution_part1 = part1("cxdnnyjw")
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "f77a0e6e"

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 993


if __name__ == "__main__":
    test()
    main()
