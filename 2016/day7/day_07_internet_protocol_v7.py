import os
import re


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def has_abba(s: str) -> bool:
    pattern = r"(.)(?!\1)(.)\2\1"
    match = re.search(pattern, s)
    return match is not None and match.group(1) != match.group(2)


def supports_tls(ip_address: str) -> bool:
    segments = ip_address.replace("[", " ").replace("]", " ").split()
    outside_brackets = segments[::2]
    inside_brackets = segments[1::2]

    in_abba = any(has_abba(segment) for segment in inside_brackets)
    out_abba = any(has_abba(segment) for segment in outside_brackets)

    return (in_abba is False) and (out_abba is True)


def supports_ssl(ip_address: str) -> bool:
    segments = ip_address.replace("[", " ").replace("]", " ").split()
    outside_brackets = segments[::2]
    inside_brackets = segments[1::2]

    for outside in outside_brackets:
        for i in range(len(outside) - 2):
            a, b, c = outside[i : i + 3]
            if a == b or a != c:
                continue
            bab = b + a + b
            for inside in inside_brackets:
                if bab in inside:
                    return True
    return False


def part1(filename: str) -> int:
    addesses = read_input(filename)
    filtered_addresses = [address for address in addesses if supports_tls(address)]
    return len(filtered_addresses)


def part2(filename: str) -> int:
    addesses = read_input(filename)
    filtered_addresses = [address for address in addesses if supports_ssl(address)]
    return len(filtered_addresses)


def test():
    print("---- TEST ----")

    assert supports_tls("abba[mnop]qrst") is True
    assert supports_tls("abcd[bddb]xyyx") is False
    assert supports_tls("aaaa[qwer]tyui") is False
    assert supports_tls("ioxxoj[asdfgh]zxcvbn") is True
    print("Part 1: OK")

    assert supports_ssl("aba[bab]xy") is True
    assert supports_ssl("xyx[xyx]xyx") is False
    assert supports_ssl("aaa[kek]eke") is True
    assert supports_ssl("zazbz[bzb]cdb") is True
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 115

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 231


if __name__ == "__main__":
    test()
    main()
