# https://old.reddit.com/r/adventofcode/comments/1h8l3z5/2024_day_7_solutions/m0tqv53/

from operator import add, mul

cat = lambda x, y: int(str(x) + str(y))

ans = 0
for line in open("test_input.txt", encoding="utf-8"):
    tgt, x, *Y = map(int, line.replace(":", "").split())

    X = [x]
    for y in Y:
        X = [op(x, y) for x in X for op in (add, mul, cat)]

    if tgt in X:
        ans += tgt

print(ans)
