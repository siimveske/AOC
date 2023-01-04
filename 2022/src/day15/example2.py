#!/usr/bin/env python3
import re
import random
from scipy import optimize
from scipy.optimize import Bounds


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def fun(X, args):
    x, y = X
    sensors, distances = args
    res = 0
    for i, s in enumerate(sensors):
        d = dist(s, (x, y)) - 1
        if d <= distances[i]:
            res += (distances[i] - d)
    return res


def search_optimum(sensors, distances, yscan, xscan):
    random.seed()
    b = Bounds([0, 0], [xscan - 1, yscan - 1])
    for i in range(1, 1000000):
        first_guess = [random.randint(0, xscan), random.randint(0, yscan)]
        res = optimize.minimize(fun, first_guess, [sensors, distances], bounds=b)
        if res.fun < 1:
            X = [round(res.x[0]), round(res.x[1])]
            print(X[0] * 4000000 + X[1])
            return X


def parse_file(filename, yscan, xscan):
    sensors = []
    beacons = []
    distances = []
    r = re.compile("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")
    with open(filename) as f:
        for line in f:
            m = r.match(line)
            if m:
                sensors.append((int(m.group(1)), int(m.group(2))))
                beacons.append((int(m.group(3)), int(m.group(4))))

    min_x = sensors[0][0]
    max_x = sensors[0][0]
    for i in range(len(sensors)):
        distances.append(dist(sensors[i], beacons[i]))
        min_x = min(sensors[i][0], min_x)
        min_x = min(beacons[i][0], min_x)
        max_x = max(sensors[i][0], max_x)
        max_x = max(beacons[i][0], max_x)
    min_x -= max(distances)
    max_x += max(distances)
    search_optimum(sensors, distances, yscan, xscan)


parse_file("test_input.txt", 20, 20)
parse_file("input.txt", 4000000, 4000000)
