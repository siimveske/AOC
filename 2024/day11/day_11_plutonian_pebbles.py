def blink(stones: list[int], blink_count: int) -> list[int]:
    for _ in range(blink_count):
        new_stones = []
        for number in stones:
            if number == 0:
                new_stones.append(1)
            elif len(str(number)) % 2 == 0:
                str_number = str(number)
                left = str_number[: len(str_number) // 2]
                right = str_number[len(str_number) // 2 :]
                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(number * 2024)
        stones = new_stones
    return stones


def part1(stones: list[int], blink_count:int) -> int:
    new_stones = blink(stones, blink_count)
    return len(new_stones)

# def part2(input_file: str) -> int:
#     pass


def test():
    print('---- TEST ----')

    stones = [0, 1, 10, 99, 999]
    assert part1(stones, blink_count=1) == 7

    stones = [125, 17]
    assert part1(stones, blink_count=6) == 22
    assert part1(stones, blink_count=25) == 55312

    print("Part 1 OK")

    # assert part2(filename) == 3
    # print('Part 2 OK')

def main():
    print('\n---- MAIN ----')

    stones = [4, 4841539, 66, 5279, 49207, 134, 609568, 0]
    solution_part1 = part1(stones, blink_count=25)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 212655
    # assert solution_part2 == 1694


if __name__ == '__main__':
    test()
    main()
