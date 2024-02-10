def solution1(code, mul, mod, target_row, target_col) -> int:
    r, c = 1, 1
    while True:
        r -= 1
        c += 1

        if r == 0:
            r = c
            c = 1

        code = (code * mul) % mod
        if (r, c) == (target_row, target_col):
            return code


def solution2(code, mul, mod, target_row, target_col) -> int:
    # https://www.mathsisfun.com/algebra/triangular-numbers.html
    # In triangular number pattern if we know a row and column of a point in the hypothenus
    # then the formula to calulate the number of points in the hypothenus is: row+col-1
    side = target_row + target_col - 2  # side length of 1 step smaller triangle
    nth = (side) * (side + 1) // 2 + target_col

    # Use Modular exponentiation to calculate a value with large exponent (nth - 1)
    # https://en.wikipedia.org/wiki/Modular_exponentiation
    nth_code = (code * pow(mul, nth - 1, mod)) % mod
    return nth_code


def part1() -> int:
    code = 20151125
    mul = 252533
    mod = 33554393
    target_row = 2981
    target_col = 3075
    return solution2(code, mul, mod, target_row, target_col)


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 9132360


if __name__ == "__main__":
    main()
