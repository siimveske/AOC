from itertools import cycle, combinations
from collections import defaultdict
'''
https://www.reddit.com/r/adventofcode/comments/znykq2/comment/j0vj0l2/?utm_source=share&utm_medium=web2x&context=3
https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=auto&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=from%2520itertools%2520import%2520cycle%252C%2520combinations%250Afrom%2520collections%2520import%2520defaultdict%250A%250Ainp%2520%253D%2520cycle%28enumerate%28open%280%29.read%28%29%29%29%250Arocks%2520%253D%2520cycle%28%2520%2520%2523%2520rows%2520of%2520bits%250A%2520%2520%2520%2520enumerate%28%255B%255B120%255D%252C%2520%255B32%252C%2520112%252C%252032%255D%252C%2520%255B112%252C%252016%252C%252016%255D%252C%2520%255B64%252C%252064%252C%252064%252C%252064%255D%252C%2520%255B96%252C%252096%255D%255D%29%250A%29%250AM%2520%253D%2520%255B%255D%2520%2520%2523%2520map%250AS%2520%253D%2520%255B%255D%2520%2520%2523%2520sequence%2520of%2520positions%2520of%2520rocks%2520at%2520rest%250AR%2520%253D%2520defaultdict%28list%29%2520%2520%2523%2520%28rock_idx%252C%2520instruction_idx%29%2520-%253E%2520S_idx%250AH%2520%253D%2520%255B%255D%2520%2520%2523%2520sequence%2520of%2520max%2520heights%250AL%2520%253D%2520C%2520%253D%2520Z%2520%253D%25200%2520%2520%2523%2520prefix%252C%2520cycle%2520length%2520and%2520height%2520per%2520cycle%250A%250A%250Adef%2520fits%28rk%252C%2520x%252C%2520y%29%253A%250A%2520%2520%2520%2520return%2520not%2520any%28%250A%2520%2520%2520%2520%2520%2520%2520%2520M%255Bj%255D%2520%2526%2520rk%255Bj%2520-%2520y%255D%2520%253E%253E%2520x%2520for%2520j%2520in%2520range%28y%252C%2520min%28len%28M%29%252C%2520y%2520%252B%2520len%28rk%29%29%29%250A%2520%2520%2520%2520%29%2520and%2520all%28r%2520%253E%253E%2520x%2520%253C%253C%2520x%2520%253D%253D%2520r%2520for%2520r%2520in%2520rk%29%250A%250A%250Awhile%2520not%2520C%253A%250A%2520%2520%2520%2520ri%252C%2520rock%2520%253D%2520next%28rocks%29%250A%2520%2520%2520%2520x%252C%2520y%2520%253D%25202%252C%2520len%28M%29%2520%252B%25204%250A%2520%2520%2520%2520%2523%2520play%2520rock%250A%2520%2520%2520%2520while%2520y%2520and%2520fits%28rock%252C%2520x%252C%2520y%2520-%25201%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520y%2520-%253D%25201%250A%2520%2520%2520%2520%2520%2520%2520%2520ai%252C%2520arrow%2520%253D%2520next%28inp%29%250A%2520%2520%2520%2520%2520%2520%2520%2520nx%2520%253D%2520max%280%252C%2520x%2520-%25201%29%2520if%2520arrow%2520%253D%253D%2520%2522%253C%2522%2520else%2520min%287%252C%2520x%2520%252B%25201%29%250A%2520%2520%2520%2520%2520%2520%2520%2520x%2520%253D%2520nx%2520if%2520fits%28rock%252C%2520nx%252C%2520y%29%2520else%2520x%250A%250A%2520%2520%2520%2520%2523%2520update%2520map%250A%2520%2520%2520%2520for%2520j%252C%2520r%2520in%2520enumerate%28rock%252C%2520y%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520if%2520j%2520%253C%2520len%28M%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520M%255Bj%255D%2520%257C%253D%2520r%2520%253E%253E%2520x%250A%2520%2520%2520%2520%2520%2520%2520%2520else%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520M.append%28r%2520%253E%253E%2520x%29%250A%2520%2520%2520%2520H.append%28len%28M%29%29%250A%2520%2520%2520%2520S.append%28x%29%250A%250A%2520%2520%2520%2520%2523%2520find%2520cycle%250A%2520%2520%2520%2520T%2520%253D%2520R%255B%28ri%252C%2520ai%29%255D%250A%2520%2520%2520%2520T.append%28len%28S%29%29%250A%2520%2520%2520%2520for%2520b%252Cm%2520in%2520combinations%28T%255B%253A-1%255D%252C%25202%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520if%2520m%2520-%2520b%2520%253D%253D%2520len%28S%29%2520-%2520m%2520and%2520S%255Bb%253Am%255D%2520%253D%253D%2520S%255Bm%253A%255D%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520L%252C%2520C%252C%2520Z%2520%253D%2520b%252C%2520m%2520-%2520b%252C%2520len%28M%29%2520-%2520H%255Bm-1%255D%250A%250Adef%2520height%28iters%29%253A%250A%2520%2520%2520%2520U%252CV%2520%253D%2520divmod%28iters-L%252C%2520C%29%250A%2520%2520%2520%2520return%2520Z%2520*%2520U%2520%252B%2520H%255BL%252BV-1%255D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%250Aprint%2520%28%2522Part1%253A%2520%2522%252C%2520height%282022%29%29%250Aprint%2520%28%2522Part1%253A%2520%2522%252C%2520height%281000000000000%29%29%250A
'''

inp = cycle(enumerate(open('input.txt').read()))
rocks = cycle(  # rows of bits
    enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]])
)
M = []  # map
S = []  # sequence of positions of rocks at rest
R = defaultdict(list)  # (rock_idx, instruction_idx) -> S_idx
H = []  # sequence of max heights
L = C = Z = 0  # prefix, cycle length and height per cycle


def fits(rk, x, y):
    return not any(
        M[j] & rk[j - y] >> x for j in range(y, min(len(M), y + len(rk)))
    ) and all(r >> x << x == r for r in rk)


while not C:
    ri, rock = next(rocks)
    x, y = 2, len(M) + 4
    # play rock
    while y and fits(rock, x, y - 1):
        y -= 1
        ai, arrow = next(inp)
        nx = max(0, x - 1) if arrow == "<" else min(7, x + 1)
        x = nx if fits(rock, nx, y) else x

    # update map
    for j, r in enumerate(rock, y):
        if j < len(M):
            M[j] |= r >> x
        else:
            M.append(r >> x)
    H.append(len(M))
    S.append(x)

    # find cycle
    T = R[(ri, ai)]
    T.append(len(S))
    for b, m in combinations(T[:-1], 2):
        if m - b == len(S) - m and S[b:m] == S[m:]:
            L, C, Z = b, m - b, len(M) - H[m - 1]


def height(iters):
    U, V = divmod(iters - L, C)
    return Z * U + H[L + V - 1]


print("Part1: ", height(2022))
print("Part1: ", height(1000000000000))
