from itertools import combinations
from math import prod


def min_elements_for_sum(arr, target_sum):
    """Calculate the minimum number of elements from the given array that
    can sum up to the target_sum. Use dynamic programming to efficiently solve the problem."""

    n = len(arr)
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(target_sum, arr[i] - 1, -1):
            if dp[j - arr[i]] != float('inf'):
                dp[j] = min(dp[j], dp[j - arr[i]] + 1)

    return dp[target_sum] if dp[target_sum] != float('inf') else -1


def calculate_quantum_entanglement(num_of_groups):
    numbers = [
        1, 2, 3, 7, 11, 13, 17,
        19, 23, 31, 37, 41, 43,
        47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101,
        103, 107, 109, 113
    ]

    target_weight = sum(numbers) // num_of_groups
    min_group_size = min_elements_for_sum(numbers, target_weight)

    result = float('inf')
    for c in combinations(numbers, min_group_size):
        if sum(c) == target_weight:
            result = min(result, prod(c))

    return result


def part1() -> int:
    return calculate_quantum_entanglement(num_of_groups=3)


def part2() -> int:
    return calculate_quantum_entanglement(num_of_groups=4)


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 11846773891

    solution_part2 = part2()
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 80393059


if __name__ == "__main__":
    main()
