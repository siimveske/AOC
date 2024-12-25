import os
import re


def read_input(filename: str) -> tuple[list[int], list[int]]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        registry, program = file.read().split("\n\n")
        registry = [int(i) for i in re.findall(r"(\d+)", registry)]
        program = [int(i) for i in re.findall(r"(\d+)", program)]

    return registry, program


def compute(a: int, program: list[int]) -> int:
    reg_a, reg_b, reg_c = a, 0, 0

    def combo(idx):
        return [0, 1, 2, 3, reg_a, reg_b, reg_c][idx]

    ip = 0
    output = []
    while ip < len(program):
        opcode, arg = program[ip], program[ip + 1]
        if opcode == 0: # adv instruction
            reg_a = reg_a // 2**combo(arg)
        elif opcode == 1: # bxl instruction
            reg_b = reg_b^arg
        elif opcode == 2: # bst instruction
            reg_b = combo(arg)%8
        elif opcode == 3 and reg_a != 0: # jnz instruction
            ip = arg
            continue
        elif opcode == 4: # bxc instruction
            reg_b = reg_b^reg_c
        elif opcode == 5: # out instruction
            output.append(combo(arg) % 8)
        elif opcode == 6: # bdv instruction
            reg_b = reg_a // 2**combo(arg)
        elif opcode == 7: # cdv instruction
            reg_c = reg_a // 2**combo(arg)
        ip += 2

    return output


def find_quine_input(a: int, idx: int, program: list[int]) -> list[int]:
    """Return quine input for program."""
    result = None
    output = compute(a, program)
    # print(f"a: {a}, idx: {idx}, output: {output}")
    if output == program:
        return a
    if output == program[-idx:] or not idx:
        for n in range(8):
            result = find_quine_input(8 * a + n, idx + 1, program)
            if result:
                break
    return result


def part1(input_file: str) -> int:
    registry, program = read_input(input_file)
    result = compute(registry[0], program)
    return ",".join(str(i) for i in result)


def part2(input_file: str) -> int:
    _, program = read_input(input_file)
    result = find_quine_input(0, 0, program)
    return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == "4,6,3,5,6,3,5,2,1,0"
    print("Part 1 OK")

    filename = "test_input2.txt"
    assert part2(filename) == 117440
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == "7,1,3,7,5,1,0,3,4"
    assert solution_part2 == 190384113204239


if __name__ == "__main__":
    test()
    main()
