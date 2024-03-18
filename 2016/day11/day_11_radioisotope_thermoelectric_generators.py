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


def get_state_hash(floors, current_floor):
    state = (current_floor, tuple(frozenset(floor) for floor in floors))
    return state


explored_states = set()


def state_explored(floors, current_floor):
    global explored_states

    current_state = get_state_hash(floors, current_floor)
    if current_state in explored_states:
        return True

    explored_states.add(current_state)

    return False


def valid_floor_contents(floors):
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


def make_move(floors, current_floor, next_floor, move_items):
    new_floor_contents = copy.deepcopy(floors)
    new_floor_contents[current_floor] = list(set(new_floor_contents[current_floor]) - set(move_items))
    new_floor_contents[next_floor] += move_items
    return new_floor_contents


def part1(filename: str) -> int:
    floors = read_input(filename)

    # Initialize our work queue
    current_floor, num_moves = 0, 0
    queue = deque([(floors, current_floor, num_moves)])

    # Process all items on the queue until there are none left
    while queue:
        floors, current_floor, num_moves = queue.popleft()

        if not valid_floor_contents(floors):
            continue

        if state_explored(floors, current_floor):
            continue

        # If first, second and third floor are empty, everything is on floor 4 and we've won
        if floors[0] == floors[1] == floors[2] == []:
            return num_moves

        num_moves += 1
        floor_below = current_floor - 1
        floor_above = current_floor + 1
        possible_moves = list(itertools.combinations(floors[current_floor] + [None], 2))

        if floor_above < len(floors):
            for move_items in possible_moves:
                new_floor_contents = make_move(
                    floors,
                    current_floor,
                    floor_above,
                    filter(None, move_items)
                )

                queue.append((new_floor_contents, floor_above, num_moves))

        if floor_below >= 0:
            for move_items in possible_moves:
                new_floor_contents = make_move(
                    floors,
                    current_floor,
                    floor_below,
                    filter(None, move_items)
                )

                queue.append((new_floor_contents, floor_below, num_moves))


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 73

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}")
    # assert solution_part2 == 3965


if __name__ == "__main__":
    main()
