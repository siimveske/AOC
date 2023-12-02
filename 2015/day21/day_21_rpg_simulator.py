LIMIT = 29000000


# https://www.reddit.com/r/adventofcode/comments/3xjpp2/comment/cy5buyt/?utm_source=share&utm_medium=web2x&context=3
def sum_of_presents(house: int) -> int:
    result = 0
    limit = int(house ** 0.5) + 1
    for elf in range(1, limit):
        if house % elf == 0:
            result += elf
            result += house / elf

    return result * 10


def sum_of_presents2(house: int) -> int:
    result = 0
    limit = int(house ** 0.5) + 1
    for elf in range(1, limit):
        if house % elf != 0:
            continue
        if elf <= 50:
            result += house / elf
        if house / elf <= 50:
            result += elf

    return result * 11


def part1() -> int:
    house_number = 1
    while sum_of_presents(house_number) < LIMIT:
        house_number += 1
    return house_number


def part2() -> int:
    house_number = 1
    while sum_of_presents2(house_number) < LIMIT:
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
