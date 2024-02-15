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


def part2(prefix: str) -> str:
    result = ["0"] * 8
    counter = 0
    hash_length = 0
    while hash_length < 8:
        hash_input = f"{prefix}{counter}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith("00000"):
            idx = hash_output[5]
            if idx.isdigit():
                idx = int(idx)
                if idx < 8 and result[idx] == "0":
                    result[idx] = hash_output[6]
                    hash_length += 1
        counter += 1
    return "".join(result)


def test():
    print("---- TEST ----")

    assert part1("abc") == "18f47a30"
    print("Part 1: OK")

    assert part2("abc") == "05ace8e3"
    print("Part 2: OK")


def main():
    print("---- MAIN ----")

    prefix = "cxdnnyjw"
    solution_part1 = part1(prefix)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "f77a0e6e"

    solution_part2 = part2(prefix)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == "999828ec"


if __name__ == "__main__":
    test()
    main()
