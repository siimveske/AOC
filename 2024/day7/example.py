# https://old.reddit.com/r/adventofcode/comments/1h8l3z5/2024_day_7_solutions/m0tv6di/

from math import log10

def digits(n):
    return int(log10(n)) + 1

def endswith(a, b):
    return (a - b) % 10 ** digits(b) == 0

def is_tractable(test_value, numbers, check_concat=True):
    *head, n = numbers
    if not head:
        return n == test_value
    q, r = divmod(test_value, n)
    if r == 0 and is_tractable(q, head, check_concat):
        return True
    if check_concat and endswith(test_value, n) and is_tractable(test_value // (10 ** digits(n)), head, check_concat):
        return True
    return is_tractable(test_value - n, head, check_concat)

def solve(data):
    ans1 = ans2 = 0
    for line in data:
        test_value, *numbers = line
        if is_tractable(test_value, numbers, False):
            ans1 += test_value
            ans2 += test_value
        elif is_tractable(test_value, numbers):
            ans2 += test_value
    return ans1, ans2