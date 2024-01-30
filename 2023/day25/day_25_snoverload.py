import os
import networkx as nx


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = nx.Graph()
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip().replace(":", "")
            components = line.split(" ")
            for component in components[1:]:
                graph.add_edge(components[0], component)

    return graph


def part1(input_file: str) -> int:
    graph = read_input(input_file)
    cut_value, partition = nx.stoer_wagner(graph)
    result = len(partition[0]) * len(partition[1])
    return result


def part2(input_file: str) -> int:
    stones = read_input(input_file)


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename) == 54
    print("Part 1 OK")

    # assert part2(filename) == 47
    # print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 552682
    # assert solution_part2 == 684195328708898


if __name__ == "__main__":
    test()
    main()
