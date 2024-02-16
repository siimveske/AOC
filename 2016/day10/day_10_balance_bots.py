import os
from collections import defaultdict
from collections import deque


def read_input(filename: str) -> tuple[dict[tuple, list], dict[tuple, tuple]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    state = defaultdict(list)
    instructions = dict()
    with open(input_file_path, "r") as f:
        for line in f:
            tokens = line.strip().split()
            if tokens[0] == "bot":
                src = (tokens[0], int(tokens[1]))
                low = (tokens[5], int(tokens[6]))
                high = (tokens[10], int(tokens[11]))
                instructions[src] = (low, high)
            else:
                v, k = int(tokens[1]), (tokens[4], int(tokens[5]))
                state[k].append(v)

    return state, instructions


def get_first_two_value_bot(bots):
    """Helper function to retrieve the first available bot with exactly two values"""
    for key, value in bots.items():
        if len(value) == 2:
            return key
    raise RuntimeError("Couldn't find any bot with two values!")


def part1(filename: str) -> int:
    state, instructions = read_input(filename)

    # Initialize our work queue
    queue = deque()

    # Find the first bot with two values
    bot = get_first_two_value_bot(state)
    queue.append(bot)

    # Process all items on the queue until there are none left
    while queue:

        current_bot = queue.popleft()  # Get the next item from the queue
        values = sorted(state[current_bot])  # Sort the values so they'll be in ascending order
        state[current_bot] = []  # Clear out the processed values

        # Check if we found the target bot
        if values[0] == 17 and values[1] == 61:
            return current_bot[1]

        # Update the instruction targets with the new values
        low_target, high_target = instructions[current_bot]
        state[low_target].append(values[0])
        state[high_target].append(values[1])

        # If either target now holds two values, enqueue them for processing
        if len(state[low_target]) == 2:
            queue.append(low_target)

        if len(state[high_target]) == 2:
            queue.append(high_target)

    # We should never reach here unless no valid solution was found
    raise RuntimeError("Failed to find solution!")


def part2(filename: str) -> int:
    lines = read_input(filename)


def test():
    print("---- TEST ----")
    print("Part 1: OK")
    print("Part 2: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 73

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 11107527530


if __name__ == "__main__":
    # test()
    main()
