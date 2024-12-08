# https://old.reddit.com/r/adventofcode/comments/1h8l3z5/2024_day_7_solutions/m0tqv53/

"""
My Python trick for today is this: you can (but should not!) override Python's built-in operators:
This allows me "remove" the final digits of an int using the | operator:
>>> print(int(int(123) | int(3)))
12
>>> print(int(int(123) | int(23)))
1
"""

from math import log10

def cat(x, y):
    """
    Return x with the last log10(y) digits removed. Useful for "removing" the last n digits of a number.
    """
    # a || b is equal to a * round_up_to_positive_power_of_ten(b) + b
    return (x-y) / 10 ** int(log10(y)+1)

print(cat(1233, 3))
