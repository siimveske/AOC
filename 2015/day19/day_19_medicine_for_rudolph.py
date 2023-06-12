import os


def readInput(filename: str) -> tuple[list, str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    mappings = []
    molecule = ""
    with open(input_file_path, "r") as f:
        raw_mapping, molecule = f.read().split('\n\n')
        molecule = molecule.strip()
        for line in raw_mapping.splitlines():
            k, v = line.split(" => ")
            mappings.append((k, v))

    return (mappings, molecule)


def find_all_substrings(string: str, substring: str) -> list[int]:
    for i in range(len(string)):
        if string.startswith(substring, i):
            yield i


def part1(data: tuple[list, str]) -> int:
    mappings, molecule = data
    molecules = set()
    for src_to_dst in mappings:
        src, dst = src_to_dst
        for idx in find_all_substrings(molecule, src):
            molecules.add(molecule[0:idx] + dst + molecule[idx + len(src):])
    return len(molecules)


def part2(grid: list[list[int]]) -> int:
    pass


def main():
    print("---- MAIN ----")
    filename = "input.txt"
    data = readInput(filename)

    solution_part1 = part1(data)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 535

    # solution_part2 = part2(data)
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 924


if __name__ == "__main__":
    main()
