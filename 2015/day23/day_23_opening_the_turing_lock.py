import os


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    instructions = []
    with open(input_file_path, "r") as f:
        for line in f:
            parts = line.replace(",", "").split()
            if parts[0] in ["jio", "jie"]:
                parts[2] = int(parts[2])
            if parts[0] == "jmp":
                parts[1] = int(parts[1])
            instructions.append(parts)

    return instructions


def run(instructions: list, reg_a: int, reg_b: int) -> tuple:
    registry = {"a": reg_a, "b": reg_b}
    program_length = len(instructions)
    idx = 0
    while idx < program_length:
        instruction = instructions[idx]
        if instruction[0] == "hlf":
            registry[instruction[1]] //= 2
        elif instruction[0] == "tpl":
            registry[instruction[1]] *= 3
        elif instruction[0] == "inc":
            registry[instruction[1]] += 1
        elif instruction[0] == "jmp":
            idx += instruction[1]
            continue
        elif instruction[0] == "jie":
            if registry[instruction[1]] % 2 == 0:
                idx += instruction[2]
                continue
        elif instruction[0] == "jio":
            if registry[instruction[1]] == 1:
                idx += instruction[2]
                continue
        idx += 1
    return registry["a"], registry["b"]


def part1(filename: str) -> int:
    instructions = read_input(filename)
    _, b = run(instructions, 0, 0)
    return b


def part2(filename: str) -> int:
    instructions = read_input(filename)
    _, b = run(instructions, 1, 0)
    return b


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 170

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")
    assert solution_part2 == 247


if __name__ == "__main__":
    main()
