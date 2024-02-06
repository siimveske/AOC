def part1() -> int:
    row = 2981
    column = 3075
    code = 20151125

    i = 0
    while True:
        for col in range(i + 1):
            r = i - col
            if r == row - 1 and col == column - 1:
                return code
            code = (code * 252533) % 33554393
        i += 1


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 9132360


if __name__ == "__main__":
    main()
