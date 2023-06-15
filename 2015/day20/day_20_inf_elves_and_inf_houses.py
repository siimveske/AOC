from functools import reduce


# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(house:int) -> set[int]:
    return set(
        reduce(list.__add__,([i, house // i] for i in range(1, int(house**0.5) + 1) if house % i == 0))
    )

def score(n:int):
    f = factors(n)
    return sum([i*10 for i in f])


def factors2(house:int) -> set[int]:
    elves = set(reduce(list.__add__,([i, house // i] for i in range(1, int(house**0.5) + 1) if house % i == 0)))
    result = []
    for elf in elves:
        if house > elf*50:
            continue
        result.append(elf)
    return result

def score2(house:int):
    f = factors2(house)
    return sum([i*11 for i in f])


def part1() -> int:

    house_number = 1000
    limit = 29000000
    while score(house_number) < limit:
        house_number += 1
    return house_number


def part2() -> int:
    house_number = 1
    limit = 29000000
    while score2(house_number) < limit:
        house_number += 1
    return house_number


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 665280

    solution_part2 = part2()
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 705600


if __name__ == "__main__":
    main()
