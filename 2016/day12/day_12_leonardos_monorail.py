import os


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, "r") as f:
        instructions = [line.split() for line in f]
    return instructions


def work(registers: dict, instructions: list[list[str]]) -> int:
    pointer = 0

    while pointer < len(instructions):
        inst = instructions[pointer]
        jump = 1
        if inst[0] == "cpy":
            val = registers[inst[1]] if inst[1] in registers else int(inst[1])
            name = inst[2]
            registers[name] = val
        elif inst[0] == "inc":
            registers[inst[1]] += 1
        elif inst[0] == "dec":
            registers[inst[1]] -= 1
        elif inst[0] == "jnz":
            val = registers[inst[1]] if inst[1] in registers else int(inst[1])
            if val != 0:
                jump = registers[inst[2]] if inst[2] in registers else int(inst[2])

        pointer += jump

    return registers["a"]


def part1(filename: str) -> int:
    instructions = read_input(filename)
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    return work(registers, instructions)


def part2(filename: str) -> int:
    instructions = read_input(filename)
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    return work(registers, instructions)


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

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 9227674


if __name__ == "__main__":
    test()
    main()
