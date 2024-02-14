import os
import re


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def has_abba(s):
    pattern = r"([a-zA-Z])([a-zA-Z])\2\1"
    match = re.search(pattern, s)
    return match is not None and match.group(1) != match.group(2)


def supports_tls(ip_address):
    segments = ip_address.replace("[", " ").replace("]", " ").split()
    outside_brackets = segments[::2]
    inside_brackets = segments[1::2]

    in_abba = any(has_abba(segment) for segment in inside_brackets)
    out_abba = any(has_abba(segment) for segment in outside_brackets)

    return (in_abba is False) and (out_abba is True)


def part1(filename: str) -> int:
    addesses = read_input(filename)
    filtered_addresses = [address for address in addesses if supports_tls(address)]
    return len(filtered_addresses)


def part2(filename: str) -> str:
    message = read_input(filename)


def test():
    print("---- TEST ----")

    assert supports_tls("abba[mnop]qrst") is True
    assert supports_tls("abcd[bddb]xyyx") is False
    assert supports_tls("aaaa[qwer]tyui") is False
    assert supports_tls("ioxxoj[asdfgh]zxcvbn") is True
    print("Part 1: OK")

    # assert part2(filename) == "advent"
    # print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 115
    print("Part 1: OK")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == "brhailro"


if __name__ == "__main__":
    test()
    main()
