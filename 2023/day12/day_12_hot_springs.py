import functools
import os

"""Solution from: https://redd.it/18hbbxe"""


def read_input(filename: str) -> list[tuple[str, tuple[int, ...]]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    condition_records = []
    with open(input_file_path, "r") as f:
        for line in f:
            records, groups = line.split()
            groups = tuple(map(int, groups.split(',')))
            condition_records.append((records, groups))
    return condition_records


@functools.cache
def calc(record, groups):
    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that aren't in the groups
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound-sign "#"
    def pound():
        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc(record[next_group + 1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as dot "."
    def dot():
        # We just skip over the dot looking for the next pound
        return calc(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    # # Help with debugging
    # print(record, groups, "->", out)
    return out


def part1(input_file: str) -> int:
    broken_records = read_input(input_file)
    total = 0
    for record, groups in broken_records:
        total += calc(record, groups)
        calc.cache_clear()
    return total


def part2(input_file: str) -> int:
    broken_records = read_input(input_file)
    total = 0
    for record, groups in broken_records:
        record = '?'.join([record] * 5)
        groups = groups * 5
        total += calc(record, groups)
        calc.cache_clear()
        # # Create a nice divider for debugging
        # print(10 * "-")
    return total


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename) == 21
    print("Part 1 OK")

    assert part2(filename) == 525152
    print("Part 2 OK")


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 7599
    assert solution_part2 == 15454556629917


if __name__ == "__main__":
    test()
    main()
