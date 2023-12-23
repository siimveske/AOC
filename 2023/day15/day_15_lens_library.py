import collections
import os


def read_input(filename: str) -> list[str]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.readline().split(',')


def get_hash(txt: str) -> int:
    result = 0
    for character in txt:
        result += ord(character)
        result *= 17
        result = result % 256
    return result


def parse_tokens(tokens: list[str]):
    commands = []
    for token in tokens:
        if '=' in token:
            key, val = token.split('=')
            commands.append((key, int(val)))
        else:
            commands.append((token[:-1], 0))
    return commands


def part1(input_file: str) -> int:
    data = read_input(input_file)
    result = 0
    for text in data:
        result += get_hash(text)

    return result


def part2(input_file: str) -> int:
    data = read_input(input_file)
    commands = parse_tokens(data)
    db = {}
    for key, val in commands:
        idx = get_hash(key)
        if idx in db:
            # remove key
            if val == 0:
                if key in db[idx]:
                    db[idx].pop(key)
                    if len(db[idx]) == 0:
                        db.pop(idx)

            # add/update key
            else:
                db[idx][key] = val

        else:
            if val:
                db[idx] = collections.OrderedDict([(key, val)])

    result = 0
    for box_number, box in db.items():
        for slot_number, focal_length in enumerate(box.values(), 1):
            power = (box_number + 1) * slot_number * focal_length
            result += power

    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 1320
    print('Part 1 OK')

    assert part2(filename) == 145
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 510792
    assert solution_part2 == 269410


if __name__ == '__main__':
    test()
    main()
