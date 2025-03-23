import os


def read_input(filename: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        numbers = file.read().strip().split("\n")
        numbers = [int(num) for num in numbers]
    return numbers

def mix(secret: int, value: int) -> int:
    return secret ^ value

def prune(secret: int) -> int:
    return secret % 16777216

def calculate(secret: int) -> int:
    result = secret * 64
    secret = mix(secret, result)
    secret = prune(secret)

    result = secret // 32
    secret = mix(secret, result)
    secret = prune(secret)

    result = secret * 2048
    secret = mix(secret, result)
    secret = prune(secret)

    return secret

def part1(input_file: str) -> int:
    secrets = read_input(input_file)
    new_secrets = []
    for secret in secrets:
        for _ in range(2000):
            secret = calculate(secret)
        new_secrets.append(secret)
    return sum(new_secrets)


# def part2(input_file: str) -> int:
#     codes = read_input(input_file)
#     return 0


def test():
    print("---- TEST ----")

    expected_values = [15887950,16495136,527345,704524,1553684,12683156,11100544,12249484,7753432,5908254]
    secret = 123
    for i in range(10):
        secret = calculate(secret)
        assert secret == expected_values[i]

    filename = "test_input.txt"
    assert part1(filename) == 37327623

    print("Part 1 OK")

    # assert part2(filename) == 154115708116294
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

#     solution_part2 = part2(filename)
#     print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 12664695565
#     assert solution_part2 == 217698355426872


if __name__ == "__main__":
    test()
    main()
