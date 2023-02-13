import collections

"""from: https://github.com/morgoth1145/advent-of-code/blob/main/2015/13/solution.py"""


def parse_input(s):
    pairs = collections.Counter()

    for line in s.splitlines():
        a, _, change, n, _, _, _, _, _, _, b = line.split()
        assert b[-1] == "."
        b = b[:-1]
        n = int(n)
        if change == "lose":
            n = -n
        else:
            assert change == "gain"
        pairs[min(a, b), max(a, b)] += n

    graph = collections.defaultdict(list)

    for (a, b), n in pairs.items():
        graph[a].append((b, n))
        graph[b].append((a, n))

    return graph


def best_path(graph):
    def impl(start, path, cost):
        if len(path) == len(graph) and path[-1] == start:
            yield cost

        current = start if len(path) == 0 else path[-1]

        for neighbor, diff in graph[current]:
            if neighbor in path:
                continue

            yield from impl(start, path + [neighbor], cost + diff)

    return max(max(impl(start, [], 0)) for start in graph.keys())


def part1(s):
    graph = parse_input(s)
    return best_path(graph)


def part2(s):
    graph = parse_input(s)

    for person in list(graph.keys()):
        graph["me"].append((person, 0))
        graph[person].append(("me", 0))

    return best_path(graph)


with open("input.txt", mode="rt") as f:
    INPUT = f.read()

solution_part1 = part1(INPUT)
print(f"Solution for Part 1: {solution_part1}")
assert solution_part1 == 618

solution_part2 = part2(INPUT)
print(f"Solution for Part 2: {solution_part2}\n")
assert solution_part2 == 601
