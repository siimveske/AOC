def part1() -> int:
    target_row = 2981
    target_col = 3075
    code = 20151125

    r, c = 1, 1
    while True:
        r -= 1
        c += 1

        if r == 0:
            r = c
            c = 1

        code = (code * 252533) % 33554393
        if r == target_row and c == target_col:
            return code


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 9132360


if __name__ == "__main__":
    main()
