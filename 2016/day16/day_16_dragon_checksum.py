def process(a: str) -> str:
    b = "".join("1" if x == "0" else "0" for x in reversed(a))
    return a + "0" + b

def checksum(data: str) -> str:
    while len(data) % 2 == 0:
        data = "".join(
            "1" if data[i] == data[i + 1] else "0" for i in range(0, len(data), 2)
        )
    return data

def solve(initial_state: str, disk_length: int) -> str:
    data = initial_state
    while len(data) < disk_length:
        data = process(data)
    data = data[:disk_length]
    return checksum(data)

def test():
    print("---- TEST ----")

    assert process("1") == "100"
    assert process("0") == "001"
    assert process("11111") == "11111000000"
    assert process("111100001010") == "1111000010100101011110000"
    assert checksum("110010110100") == "100"
    assert solve("10000", 20) == "01100"

    print("OK")


def main():
    print("---- MAIN ----")

    solution_part1 = solve(initial_state="10011111011011001", disk_length=272)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == "10111110010110110"

    solution_part2 = solve(initial_state="10011111011011001", disk_length=35651584)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == "01101100001100100"


if __name__ == "__main__":
    test()
    main()
