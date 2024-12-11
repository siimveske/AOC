from collections import defaultdict


def blink_stones(stones: list[int], blink_count: int) -> dict[int, int]:
    """
    Blink the stones the given number of times.
    """
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in range(blink_count):
        new_stone_counts = defaultdict(int)
        for number, count in stone_counts.items():
            if number == 0:
                new_stone_counts[1] += count
            elif len(str(number)) % 2 == 0:
                left, right = str(number)[: len(str(number)) // 2], str(number)[len(str(number)) // 2 :]
                new_stone_counts[int(left)] += count
                new_stone_counts[int(right)] += count
            else:
                new_stone_counts[number * 2024] += count

        stone_counts = new_stone_counts

    return stone_counts


def part1(stones: list[int], blink_count:int) -> int:
    new_stones = blink_stones(stones, blink_count)
    return sum(new_stones.values())

def part2(stones: list[int], blink_count:int) -> int:
    return part1(stones, blink_count)


def test():
    print('---- TEST ----')

    stones = [0, 1, 10, 99, 999]
    assert part1(stones, blink_count=1) == 7

    stones = [125, 17]
    assert part1(stones, blink_count=6) == 22
    assert part1(stones, blink_count=25) == 55312
    print("Part 1 OK")

    assert part2(stones, blink_count=25) == 55312
    print('Part 2 OK')

def main():
    print('\n---- MAIN ----')

    stones = [4, 4841539, 66, 5279, 49207, 134, 609568, 0]
    solution_part1 = part1(stones, blink_count=25)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(stones, blink_count=75)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 212655
    assert solution_part2 == 253582809724830


if __name__ == '__main__':
    test()
    main()
