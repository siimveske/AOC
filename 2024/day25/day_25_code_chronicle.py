import os


def read_input(filename: str) -> tuple:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    keys = []
    locks = []
    with open(file_path, "r") as file:
        for item in file.read().strip().split("\n\n"):
            lines = item.splitlines()
            heights = []
            for c in range(len(lines[0])):
                cnt = 0
                for r in range(len(lines)):
                    if lines[r][c] == "#":
                        cnt += 1
                heights.append(cnt)

            heights = tuple(heights)
            if item.startswith("#####"):
                locks.append(heights)
            else:
                keys.append(heights)
        free_space=len(lines)

    return locks, keys, free_space


def part1(input_file: str) -> int:
    locks, keys, free_space = read_input(input_file)
    pairs = set()
    for lock in locks:
        for key in keys:
            overlap = False
            for l, k in zip(lock, key):
                if l+k > free_space:
                    overlap = True
                    break
            if not overlap:
                pairs.add((lock, key))
    return len(pairs)


# def part2(input_file: str) -> int:
#     network = read_input(input_file)
#     vertices = set(network.keys())
#     max_clique = bron_kerbosch(set(), vertices, set(), network)
#     result = ','.join(sorted(max_clique))
#     return result

def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 3
    print("Part 1 OK")

    # assert part2(filename) == "co,de,ka,ta"
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 2900
    # assert solution_part2 == "bu,fq,fz,pn,rr,st,sv,tr,un,uy,zf,zi,zy"


if __name__ == "__main__":
    test()
    main()
