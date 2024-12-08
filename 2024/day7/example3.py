# https://www.reddit.com/r/adventofcode/comments/1h8l3z5/2024_day_7_solutions/m0uaade/

from math import log10
from re import findall

class int(int):
    __or__ = lambda x, y: (x-y) / 10 ** int(log10(y)+1)

def f(tgt, xs):
    if tgt%1 or not xs: return 0
    tgt = int(tgt)
    *xs, x = xs

    return tgt * any([tgt == x and not xs,
                    f(tgt / x, xs),
                    f(tgt - x, xs),
                    f(tgt | x, xs)])

print(sum(f(t, xs) for t, *xs in [
    map(int, findall(r'\d+', l)) for l in open('test_input.txt')]))
