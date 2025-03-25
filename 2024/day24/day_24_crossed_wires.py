import os


def read_input(filename: str) -> dict[str, set[str]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    state = dict()
    network = []
    with open(file_path, "r") as file:
        part_a, part_b = file.read().split("\n\n")
        for line in part_a.strip().split("\n"):
            wire, value = line.split(": ")
            state[wire] = int(value)

        for line in part_b.strip().split("\n"):
            inputs, output = line.split(" -> ")
            inputs = inputs.split(" ")
            network.append([inputs, output])

    return state, network


def part1(input_file: str) -> int:
    state, network = read_input(input_file)

    def apply_logic_gate(op: str, arg1: int, arg2: int) -> int:
        operations = {
            "AND": lambda x, y: x & y,
            "OR": lambda x, y: x | y,
            "XOR": lambda x, y: x ^ y
        }
        return operations[op](arg1, arg2)

    def process_network() -> None:
        for inputs, output in network:
            arg1, op, arg2 = inputs
            if arg1 not in state or arg2 not in state:
                continue
            state[output] = apply_logic_gate(op, state[arg1], state[arg2])

    z_outputs = sorted([o for _, o in network if o.startswith("z")], reverse=True)
    while True:
        process_network()
        if all(o in state for o in z_outputs):
            break

    result = ''.join(str(state[output]) for output in z_outputs)
    return int(result, 2)


# def part2(input_file: str) -> int:
#     network = read_input(input_file)
#     vertices = set(network.keys())
#     max_clique = bron_kerbosch(set(), vertices, set(), network)
#     result = ','.join(sorted(max_clique))
#     return result

def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 4

    filename = "test_input2.txt"
    assert part1(filename) == 2024
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

    assert solution_part1 == 52728619468518
    # assert solution_part2 == "bu,fq,fz,pn,rr,st,sv,tr,un,uy,zf,zi,zy"


if __name__ == "__main__":
    test()
    main()
