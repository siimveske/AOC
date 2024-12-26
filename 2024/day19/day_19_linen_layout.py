import os

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        a, b = file.read().split("\n\n")
        a = [i.strip() for i in a.split(",")]
        b = b.splitlines()
    return a,b

def can_construct(target: str, word_bank: list[str], memo: dict[str, bool] = None) -> bool:
    """
    Checks if a target string can be constructed from a list of words in the word bank.

    Args:
        target (str): The target string to construct.
        word_bank (list[str]): The list of words that can be used to construct the target string.
        memo (dict[str, bool], optional): A memoization dictionary to store previously computed results for efficiency. Defaults to None.

    Returns:
        bool: True if the target string can be constructed from the word bank, False otherwise.
    """
    if memo is None:
        memo = {}

    # If the target string is empty, it can be constructed from any word bank
    if target == "":
        return True

    # If the target string has already been computed, return the cached result
    if target in memo:
        return memo[target]

    # Iterate over each word in the word bank
    for word in word_bank:
        # If the target string starts with the word, check if the remaining suffix can be constructed
        if target.startswith(word):
            # Part of the target that remains after removing the word
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    # If no combination of words can construct the target string, return False
    memo[target] = False
    return False


def part1(input_file: str) -> int:
    a, b = read_input(input_file)
    results = {s: can_construct(s, a) for s in b}
    result = sum(results.values())
    return result


# def part2(input_file: str, rows: int, cols: int) -> str:
#     coordinates = read_input(input_file)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 6
    print("Part 1 OK")

    # assert part2(filename, rows=7, cols=7) == "6,1"
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename, rows=71, cols=71)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 342
    # assert solution_part2 == "60,37"


if __name__ == "__main__":
    test()
    main()
