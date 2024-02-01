import os


def read_input(filename: str) -> list:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, filename)

    instructions = []
    with open(file_path, "r") as f:
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
        command, *args = instructions[idx]
        if command == "hlf":
            registry[args[0]] //= 2
        elif command == "tpl":
            registry[args[0]] *= 3
        elif command == "inc":
            registry[args[0]] += 1
        elif command == "jmp":
            idx += args[0]
            continue
        elif command == "jie" and registry[args[0]] % 2 == 0:
            idx += args[1]
            continue
        elif command == "jio" and registry[args[0]] == 1:
            idx += args[1]
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
