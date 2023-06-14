from functools import reduce


# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n:int) -> set[int]:
    return set(
        reduce(list.__add__,([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    )

def score(n:int):
    f = factors(n)
    return sum([i*10 for i in f])

def part1() -> int:

    i = 1000
    limit = 29000000
    while score(i) < limit:
        i += 1
    return i


def part2() -> int:
    pass


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 665280

    # solution_part2 = part2()
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 212


if __name__ == "__main__":
    main()
