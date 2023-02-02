'''
https://topaz.github.io/paste/#XQAAAQB0BAAAAAAAAAAyGUj/T2Dcw7Ul5hThEzzShsdZAUJ5ch4SlnN3Xh7xvt8/ZIA3wA1dADfQd1JkgnyrHWF+V2kA1XQ18dHNjsuhPASCpYYRIgxF25nrZvfPw9YksAS4GpG9Pp/UQbsT8Hbnv8CTLTDE0bnT2h3L2E7+tbLjSRAM5lyZYx1J7R7nI4Qw5/Gs2OCB2nspYI5JYZBYyyiP96Uf09C4yR6xN04OkeOi9VcAcvH+8uTKTBmUsoYtD4dE2TQkUTqwT0ILgHPJAEJqwc4dD4Cl+4yzKDdDtYndrlbhPK4MD635bPq8+vBnHmHVZCV3EkkDkObeuHdfGqRM4zlvDJ7rRB1YvGbVE57j+AkLHnWgLRBDn5svpefvV5XcIQwvt0jbv7np6bnsZUNZrI9BPh1xadxKm3Li+63LR5fT0KPKIhoV5dGrzxTOdEy7ZlSEanlOLrXtO8bqWkeLp/KXsRuTXuXFg6/RfqabirM8tnPphXSKBxj17yH32OoY5B700255h1jmHoxVC6s/iNmzsmyEqiYoNyhA94N9QuhCTe3pyLXP5/3BG7/CIrSFIHPmxm+9VlMqFHNWWN6QJ7HwTlFz6VmSd2y+/pR2z6ZC/+6t/hoposZ38kauq55VC8F8vh0DgkfQgx+x0C46lBpe7kL+7BSC++lTCQ==
'''


def possible(x, y):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True


def p1():
    ct = 0
    y = 2_000_000
    for x in range(min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)):
        if not possible(x, y) and (x, y) not in beacons:
            ct += 1
    return ct


def p2():
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue
                if possible(x, y):
                    return x * 4_000_000 + y


data = open("input.txt").read().strip()
sensors, beacons = set(), set()
for line in data.split("\n"):
    parts = line.split()
    sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
    bx, by = int(parts[8][2:-1]), int(parts[9][2:])
    d = abs(sx - bx) + abs(sy - by)
    sensors.add((sx, sy, d))
    beacons.add((bx, by))
print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")
