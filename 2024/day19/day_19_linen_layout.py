import os

def read_input(filename: str) -> list[tuple[int, int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        a, b = file.read().split("\n\n")
        a = [i.strip() for i in a.split(",")]
        b = b.splitlines()
    return a,b

def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

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
