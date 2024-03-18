import os
import re
import itertools
import copy
from collections import deque


def read_input(filename: str) -> list[list[str]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    floors = [[], [], [], []]
    with open(input_file_path, "r") as f:
        for idx, line in enumerate(f):
            chips = [groups[1] + ' chip' for groups in re.findall(r'((\w+)-compatible microchip)', line)]
            generators = re.findall(r'(\w+ generator)', line)
            floors[idx] = chips + generators

    return floors


def get_state_hash(floors: list[list[str]], current_floor: int):

    cnt = []
    for floor in floors:
        num_of_generators = 0
        num_of_chips = 0
        for item in floor:
            if 'generator' in item:
                num_of_generators += 1
            if 'chip' in item:
                num_of_chips += 1
        cnt.append((num_of_generators, num_of_chips))
    state = (current_floor, tuple(cnt))
    return state


explored_states = set()


def state_explored(floors: list[list[str]], current_floor: int):
    global explored_states

    current_state = get_state_hash(floors, current_floor)
    if current_state in explored_states:
        return True

    explored_states.add(current_state)

    return False


def valid_floor_contents(floors: list[list[str]]):
    for floor in floors:
        # Only floors with a generator can cause problems
        if not any([item for item in floor if 'generator' in item]):
            continue

        for item in floor:
            is_chip = 'chip' in item
            if not is_chip:
                continue

            chip_type = item.split()[0]

            # floor contains at least one generator, but no generator for this chip
            if chip_type + ' generator' not in floor:
                return False

    return True


def make_move(floors: list[list[str]], current_floor: int, next_floor: int, move_items: list[str]):
    new_floor_contents = copy.deepcopy(floors)
    new_floor_contents[current_floor] = list(set(new_floor_contents[current_floor]) - set(move_items))
    new_floor_contents[next_floor] += move_items
    return new_floor_contents


def part1(filename: str) -> int:
    floors = read_input(filename)

    current_floor, num_moves = 0, 0
    queue = deque([(floors, current_floor, num_moves)])

    while queue:
        floors, current_floor, num_moves = queue.popleft()

        if state_explored(floors, current_floor):
            continue

        # If everything is on floor 4 then we've won
        if len(floors[-1]) == sum(len(floor) for floor in floors):
            return num_moves

        num_moves += 1
        floor_below = current_floor - 1
        floor_above = current_floor + 1
        possible_moves = list(itertools.combinations(floors[current_floor] + [None], 2))

        for move_items in possible_moves:
            for next_floor in [floor_below, floor_above]:
                if not 0 <= next_floor < len(floors):
                    continue
                new_floor_contents = make_move(
                    floors,
                    current_floor,
                    next_floor,
                    list(filter(None, move_items))
                )
                if valid_floor_contents(new_floor_contents):
                    queue.append((new_floor_contents, next_floor, num_moves))


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == 11
    print("Part 1: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 37

    filename = "input2.txt"
    solution_part2 = part1(filename)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 61


if __name__ == "__main__":
    test()
    main()
