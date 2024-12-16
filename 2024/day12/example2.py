# https://old.reddit.com/r/adventofcode/comments/1hcdnk0/2024_day_12_solutions/m1nj6se/
grid = {i+j*1j: c for i,r in enumerate(open('test_input.txt'))
                  for j,c in enumerate(r.strip())}

sets = {p: {p} for p in grid}

for p in grid:
    for n in p+1, p-1, p+1j, p-1j:
        if n in grid and grid[p] == grid[n]:
            sets[p] |= sets[n]
            for x in sets[p]:
                sets[x] = sets[p]

sets = {tuple(s) for s in sets.values()}

def edge(ps):
    P = {(p,d) for d in (+1,-1,+1j,-1j) for p in ps if p+d not in ps}
    stuff = set()
    for p, d in P:
        print(f"p={p}, d={d}, d*1j={d*1j} ,(p+d*1j, d)={(p+d*1j, d)}")
        stuff.add((p+d*1j, d))
    p2 = P - stuff
    result = P, p2
    return result

for part in 0,1: print(sum(len(s) * len(edge(s)[part]) for s in sets))