import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        instructions = [line.split() for line in f]
    return instructions


def part1(filename: str) -> int:
    instructions = read_input(filename)
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    pointer = 0

    while pointer < len(instructions):
        inst = instructions[pointer]

        if inst[0] == "cpy":
            src = int(inst[1]) if inst[1].lstrip('-').isdigit() else registers[inst[1]]
            dest = inst[2]
            registers[dest] = src
        elif inst[0] == "inc":
            registers[inst[1]] += 1
        elif inst[0] == "dec":
            registers[inst[1]] -= 1
        elif inst[0] == "jnz":
            val = int(inst[1]) if inst[1].lstrip('-').isdigit() else registers.get(inst[1])
            jump = int(inst[2]) if inst[2].lstrip('-').isdigit() else registers.get(inst[2])
            if val != 0:
                pointer += jump - 1

        pointer += 1

    return registers["a"]


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == 42
    print("Part 1: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 318020

    # filename = "input2.txt"
    # solution_part2 = part1(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 61


if __name__ == "__main__":
    test()
    main()
