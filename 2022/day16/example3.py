import re
'''https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py'''

with open('input.txt', mode="rt") as f:
    lines = f.read()
lines = [re.split('[\\s=;,]+', x) for x in lines.splitlines()]

GRAPH = {x[1]: set(x[10:]) for x in lines}
COST = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
BITMASK = {x: 1 << i for i, x in enumerate(COST)}
DISTANCE = {x: {y: 1 if y in GRAPH[x] else float('+inf') for y in GRAPH} for x in GRAPH}
for a in DISTANCE:
    for b in DISTANCE:
        for c in DISTANCE:
            DISTANCE[b][c] = min(DISTANCE[b][c], DISTANCE[b][a] + DISTANCE[a][c])


def visit(current_node, time, visited, released_pressure, answer):
    answer[visited] = max(answer.get(visited, 0), released_pressure)
    for next_node in COST:
        new_time = time - DISTANCE[current_node][next_node] - 1
        if BITMASK[next_node] & visited or new_time <= 0:
            continue
        visit(next_node, new_time, visited | BITMASK[next_node], released_pressure + new_time * COST[next_node], answer)
    return answer


total1 = max(visit('AA', 30, 0, 0, {}).values())
visited2 = visit('AA', 26, 0, 0, {})
total2 = max(v1 + v2 for k1, v1 in visited2.items()
             for k2, v2 in visited2.items() if not k1 & k2)
print(total1, total2)
