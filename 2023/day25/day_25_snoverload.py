import os
import networkx as nx


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = nx.Graph()
    with open(input_file_path, "r") as f:
        for line in f:
            l, r = line.split(":")
            for node in r.strip().split():
                graph.add_edge(l, node)

    return graph


def part1(input_file: str) -> int:
    graph = read_input(input_file)
    cut_value, partition = nx.stoer_wagner(graph)
    result = len(partition[0]) * len(partition[1])
    return result


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename) == 54
    print("Part 1 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    assert solution_part1 == 552682


if __name__ == "__main__":
    test()
    main()
