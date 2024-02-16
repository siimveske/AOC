import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def decompress(string: str) -> str:
    result = []
    idx = 0
    while idx < len(string):
        char = string[idx]
        if char == "(":
            start_idx = idx
            while char != ")":
                idx += 1
                char = string[idx]
            length, repeat = map(int, string[start_idx + 1: idx].split("x"))
            part = string[idx + 1: idx + 1 + length]
            result.append(part * repeat)
            idx += length + 1
        else:
            result.append(char)
            idx += 1
    return "".join(result)


def decompress2(string: str) -> str:
    result = []
    idx = 0
    while idx < len(string):
        char = string[idx]
        if char == "(":
            start_idx = idx
            while char != ")":
                idx += 1
                char = string[idx]
            length, repeat = map(int, string[start_idx + 1: idx].split("x"))
            part = string[idx + 1: idx + 1 + length]
            if "(" in part:
                part = decompress2(part)
            result.append(part * repeat)
            idx += length + 1
        else:
            result.append(char)
            idx += 1
    return "".join(result)


def part1(filename: str) -> int:
    lines = read_input(filename)
    length = sum(len(decompress(line)) for line in lines)
    return length


def part2(filename: str) -> int:
    lines = read_input(filename)
    length = sum(len(decompress2(line)) for line in lines)
    return length


def test():
    print("---- TEST ----")

    assert decompress("ADVENT") == "ADVENT"
    assert decompress("A(1x5)BC") == "ABBBBBC"
    assert decompress("(3x3)XYZ") == "XYZXYZXYZ"
    assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
    assert decompress("(6x1)(1x3)A") == "(1x3)A"
    assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"
    print("Part 1: OK")

    assert decompress2("(3x3)XYZ") == "XYZXYZXYZ"
    assert decompress2("X(8x2)(3x3)ABCY") == "XABCABCABCABCABCABCY"
    assert len(decompress2("(27x12)(20x12)(13x14)(7x10)(1x12)A")) == 241920
    assert len(decompress2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")) == 445
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 115118

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 11107527530


if __name__ == "__main__":
    test()
    main()
