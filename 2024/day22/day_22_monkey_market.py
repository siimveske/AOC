import os
from collections import Counter, deque


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
    # result = secret * 64
    # secret = mix(secret, result)
    # secret = prune(secret)
    secret = mix(secret, (secret << 6)) & 0xFFFFFF

    # result = secret // 32
    # secret = mix(secret, result)
    # secret = prune(secret)
    secret = mix(secret, (secret >> 5)) & 0xFFFFFF

    # result = secret * 2048
    # secret = mix(secret, result)
    # secret = prune(secret)
    secret = mix(secret, (secret << 11)) & 0xFFFFFF

    return secret

def get_price_patterns_for_secret(secret: int) -> dict[tuple[int, ...], int]:
    """Analyze price patterns for a single secret number.

    Args:
        secret: Initial secret number

    Returns:
        Dictionary mapping price difference patterns to profits
    """
    PATTERN_LENGTH = 4
    ITERATIONS = 2000

    last_price = secret % 10  # Last digit is the price
    price_diffs = deque(maxlen=PATTERN_LENGTH) # Keep track of last 4 price differences
    pattern_to_profit = {}

    for _ in range(ITERATIONS):
        secret = calculate(secret)
        current_price = secret % 10
        price_diff = current_price - last_price

        price_diffs.append(price_diff)
        if len(price_diffs) == PATTERN_LENGTH:
            pattern = tuple(price_diffs)
            pattern_to_profit.setdefault(pattern, current_price) # Store ONLY first occurrence of pattern

        last_price = current_price

    return pattern_to_profit


def part1(input_file: str) -> int:
    secrets = read_input(input_file)
    new_secrets = []
    for secret in secrets:
        for _ in range(2000):
            secret = calculate(secret)
        new_secrets.append(secret)
    return sum(new_secrets)


def part2(input_file: str) -> int:
    """Calculate maximum profit from price patterns.

    Args:
        input_file: Path to input file containing secret numbers

    Returns:
        Maximum profit found across all price patterns
    """
    secrets = read_input(input_file)
    price_pattern_profits = Counter()

    for secret in secrets:
        price_pattern_profits.update(get_price_patterns_for_secret(secret))

    return max(price_pattern_profits.values())


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


    filename = "test_input2.txt"
    assert part2(filename) == 23
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 12664695565
    assert solution_part2 == 1444


if __name__ == "__main__":
    test()
    main()
