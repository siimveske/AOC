from functools import cache
import os
import itertools as it

def read_input(filename: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        codes = file.read().strip().split("\n")
    return codes

N_PAD = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
                 "0": (3, 1), "A": (3, 2)
}
D_PAD = {
                 "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
}
PADS = [N_PAD, D_PAD]
OFFSETS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

@cache
def get_button_paths(start: str, end: str, idx_pad: int) -> list[str]:
    (r1, c1) = PADS[idx_pad][start]
    (r2, c2) = PADS[idx_pad][end]

    button_dr, button_dc = r2 - r1, c2 - c1
    movements = (
        "<" * -button_dc + ">" * button_dc
      + "^" * -button_dr + "v" * button_dr
    )

    paths = []
    for sequence in set(it.permutations(movements)):
        robot_r, robot_c = r1, c1
        for movement in sequence:
            robot_dr, robot_dc = OFFSETS[movement]
            robot_r += robot_dr
            robot_c += robot_dc
            if idx_pad == 0 and (robot_r, robot_c) == (3,0):
                break
            if idx_pad == 1 and (robot_r, robot_c) == (0,0):
                break
        else:
            paths.append("".join(sequence) + "A")

    return paths

@cache
def get_min_sequence_length(code: str, depth: int, idx_pad=0) -> int:
    result = 0
    for button1, button2 in zip("A" + code, code):
        paths = get_button_paths(button1, button2, idx_pad)
        if depth == 0:
            result += min(map(len, paths))
        else:
            result += min(
                get_min_sequence_length(path, depth - 1 , idx_pad=1)
                for path in paths
            )
    return result

def part1(input_file: str) -> int:
    total = 0
    codes = read_input(input_file)
    for code in codes:
        keycode_number = int(code[:-1])
        min_sequence_length = get_min_sequence_length(code, depth=2)
        total += min_sequence_length * keycode_number
    return total


def part2(input_file: str) -> int:
    total = 0
    codes = read_input(input_file)
    for code in codes:
        keycode_number = int(code[:-1])
        min_sequence_length = get_min_sequence_length(code, depth=25)
        total += min_sequence_length * keycode_number
    return total


def test():
    print("---- TEST ----")

    filename = "test_input.txt"
    assert part1(filename) == 126384
    print("Part 1 OK")

    assert part2(filename) == 154115708116294
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 176650
    assert solution_part2 == 217698355426872


if __name__ == "__main__":
    test()
    main()
