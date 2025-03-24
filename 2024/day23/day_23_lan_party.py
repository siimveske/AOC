import os
from collections import defaultdict


def read_input(filename: str) -> dict[str, set[str]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    network = defaultdict(set)
    with open(file_path, "r") as file:
        for line in file.read().strip().split("\n"):
            a, b = line.split("-")
            network[a].add(b)
            network[b].add(a)
    return network

def find_triplets(network: dict[str, set[str]]) -> set[tuple[str, str, str]]:
    """Find all sets of three computers where each computer is connected to the other two computers.

    Args:
        network: Dictionary representing the network where keys are computers and values are sets of connected computers"
    """
    triplets = set()
    for c in network.keys():
        for n1 in network[c]:
            for n2 in network[n1]:
                if n2 != c and n2 in network[c]:
                    triplet = sorted([c, n1, n2])
                    triplets.add(tuple(triplet))
    return triplets

def filter_triplets(triplets: set[tuple[str, str, str]], prefix="t") -> set[tuple[str, str, str]]:
    """Filter triplets to only include those where at least one computer name starts with prefix.

    Args:
        triplets: Set of triplets where each triplet is a tuple of three computers
        prefix: Prefix to filter by
    """
    filtered_triplets = set()
    for triplet in triplets:
        for computer in triplet:
            if computer.startswith(prefix):
                filtered_triplets.add(triplet)
                break
    return filtered_triplets

def part1(input_file: str) -> int:
    network = read_input(input_file)
    triplets = find_triplets(network)
    result = filter_triplets(triplets)
    return len(result)


def part2(input_file: str) -> int:
    pass

def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 7
    print("Part 1 OK")

    # filename = "test_input2.txt"
    # assert part2(filename) == 23
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

# solution_part2 = part2(filename)
# print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 1308
# assert solution_part2 == 1444


if __name__ == "__main__":
    test()
    main()
