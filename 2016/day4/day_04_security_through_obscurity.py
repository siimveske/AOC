import os
from collections import Counter


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, "r") as f:
        for line in f:
            tokens = line.strip().split("-")
            name = []
            for token in tokens:
                if token[0].isnumeric():
                    room_id, room_hash = token.split("[")
                    room_id = int(room_id)
                    room_hash = room_hash[:-1]
                    data.append((name, room_id, room_hash))
                else:
                    name.append(token)
    return data


def filter_rooms(rooms):
    filtered_rooms = []

    for name, room_id, room_hash in rooms:
        letters = "".join(name)
        letter_counts = Counter(letters)
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        key = "".join(letter for letter, _ in sorted_letters[:5])

        if key == room_hash:
            filtered_rooms.append((name, room_id, room_hash))

    return filtered_rooms


def part1(filename: str) -> int:
    rooms = read_input(filename)
    filtered_rooms = filter_rooms(rooms)

    return sum([room_id for name, room_id, room_hash in filtered_rooms])


def part2(filename: str) -> int:
    rooms = read_input(filename)
    filtered_rooms = filter_rooms(rooms)
    for name, room_id, _ in filtered_rooms:
        for part in name:
            decoded_letters = []
            for character in part:
                code = ord(character)
                new_code = ((code - ord("a") + room_id) % 26) + ord("a")
                decoded_letters.append(chr(new_code))
            decoded_word = "".join(decoded_letters)
            if "north" in decoded_word:
                return room_id


def test():
    print("---- TEST ----")
    filename = "test_input.txt"

    assert part1(filename) == 1514
    print("Part 1: OK")


def main():
    print("---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename)
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 158835

    solution_part2 = part2(filename)
    print(f"Solution for Part 2: {solution_part2}")
    assert solution_part2 == 993


if __name__ == "__main__":
    test()
    main()
