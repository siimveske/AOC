import os

from pyparsing import deque


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


def part2(input_file: str) -> str:
    # state, network = read_input(input_file)

    # # Extract x and y values from state
    # x, y = [], []
    # for k,v in state.items():
    #     if k.startswith("x"):
    #         x.append(v)
    #     elif k.startswith("y"):
    #         y.append(v)
    # x = ''.join(str(i) for i in x)
    # y = ''.join(str(i) for i in y)

    # def apply_logic_gate(op: str, arg1: int, arg2: int) -> int:
    #     operations = {
    #         "AND": lambda x, y: x & y,
    #         "OR": lambda x, y: x | y,
    #         "XOR": lambda x, y: x ^ y
    #     }
    #     return operations[op](arg1, arg2)

    # def process_network() -> None:
    #     q = deque(network)
    #     while q:
    #         inputs, output = q.popleft()
    #         arg1, op, arg2 = inputs
    #         if arg1 not in state or arg2 not in state:
    #             q.append([inputs, output])
    #             continue
    #         state[output] = apply_logic_gate(op, state[arg1], state[arg2])

    # process_network()
    # result = sorted([o for _, o in network if o.startswith("z")], reverse=True)
    # result = ''.join(str(state[z]) for z in result)

    # print("d: 1")
    # print(f"x: 0{x}")
    # print(f"y: 0{y}")
    # print(f"r: {result}")

    # # test 0 + x
    # print("---- TEST X+0 ----")
    # for i in range(1, len(x)+1):
    #     num = 2**i
    #     num_bin = f"{num:045b}"
    #     num_rev = num_bin[::-1]
    #     new_state = {}
    #     for i in range(len(num_rev)):
    #         xkey = f"x{i:02}"
    #         ykey = f"y{i:02}"
    #         new_state[xkey] = int(num_rev[i])
    #         new_state[ykey] = 0
    #     state = new_state

    #     process_network()
    #     result = sorted([o for _, o in network if o.startswith("z")], reverse=True)
    #     result = ''.join(str(state[z]) for z in result)
    #     print(f"d: {num}")
    #     print(f"x: 0{num_bin}")
    #     print(f"y: 0{y}")
    #     print(f"r: {result}")
    #     print()

    # # test 0 + y
    # print("---- TEST 0+Y ----")
    # for i in range(len(x)+1):
    #     num = 2**i
    #     num_bin = f"{num:045b}"
    #     num_rev = num_bin[::-1]
    #     new_state = {}
    #     for i in range(len(num_rev)):
    #         xkey = f"x{i:02}"
    #         ykey = f"y{i:02}"
    #         new_state[xkey] = 0
    #         new_state[ykey] = int(num_rev[i])
    #     state = new_state

    #     process_network()
    #     result = sorted([o for _, o in network if o.startswith("z")], reverse=True)
    #     result = ''.join(str(state[z]) for z in result)
    #     print(f"d: {num}")
    #     print(f"x: 0{x}")
    #     print(f"y: 0{num_bin}")
    #     print(f"r: {result}")
    #     print()

    # test x+y
    # print("---- TEST X+Y ----")
    # for i in range(len(x)+1):
    #     num = 2**i
    #     num_bin = f"{num:045b}"
    #     num_rev = num_bin[::-1]
    #     new_state = {}
    #     for i in range(len(num_rev)):
    #         xkey = f"x{i:02}"
    #         ykey = f"y{i:02}"
    #         new_state[xkey] = int(num_rev[i])
    #         new_state[ykey] = int(num_rev[i])
    #     state = new_state

    # print(f"x: {x}")
    # print(f"y: {y}")
    # process_network()
    # result = sorted([o for _, o in network if o.startswith("z")], reverse=True)
    # result = ''.join(str(state[z]) for z in result)
    # print(f"r: {result}")
    # print()

    # # If the output of a gate is z, then the operation has to be XOR unless it is the last bit.
    # sorted_network = sorted(network, key=lambda x: x[1])
    # for item in sorted_network:
    #     i, o = item
    #     if o.startswith("z") and i[1] != "XOR":
    #         print(o, i)
    # print()


    # # If the output of a gate is not z and the inputs are not x, y then it has to be AND / OR, but not XOR.
    # for item in sorted_network:
    #     i, o = item
    #     if not o.startswith("z") and i[0][0] not in "xy" and i[2][0] not in "xy" and i[1] == "XOR":
    #         print(o, i)

    gates = ["z12", "qdg", "vvf", "z19", "dck", "fgn", "nvh", "z37"]
    gates = sorted(gates)
    result = ','.join(gates)
    return result

def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 4

    filename = "test_input2.txt"
    assert part1(filename) == 2024
    print("Part 1 OK")

    # filename = "test_input4.txt"
    # assert part2(filename) == 0
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 52728619468518
    assert solution_part2 == "dck,fgn,nvh,qdg,vvf,z12,z19,z37"


if __name__ == "__main__":
    test()
    main()
