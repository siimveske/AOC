# https://old.reddit.com/r/adventofcode/comments/1hcdnk0/2024_day_12_solutions/m1pb0m7/
from numpy import array as A, unique as uniq
from scipy.ndimage import label
from scipy.signal import convolve2d

G = A([list(l.strip()) for l in open(0)])
S = lambda A: abs(A).sum()

ans = A([0,0])
for L, n in [label(G==g) for g in uniq(G)]:
    for i in range(n):
        H = (L == i+1)

        h = convolve2d(H, [[1,-1]])
        v = convolve2d(H, [[1],[-1]])
        x = convolve2d(H, [[-1,1],[1,-1]])

        ans += S(H) * A([S(h)+S(v), S(x)])

print(*ans)