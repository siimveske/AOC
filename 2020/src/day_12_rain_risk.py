import os

COMPASS = {
       0: 'E',
      90: 'S',
     180: 'W',
     270: 'N',
     -90: 'N',
    -180: 'W',
    -270: 'S'
    }


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        instructions = [(line[0], int(line[1:])) for line in file]

    return instructions


def move(x, y, amount, direction):
    if direction == 'E':
        return (x + amount, y)
    if direction == 'W':
        return (x - amount, y)
    if direction == 'N':
        return (x, y + amount)
    if direction == 'S':
        return (x, y - amount)


def rotate(angle, direction, amount):
    if direction == 'L':
        new_orientation = angle - amount
        if new_orientation <= -360:
            new_orientation = new_orientation % -360
    elif direction == 'R':
        new_orientation = angle + amount
        if new_orientation >= 360:
            new_orientation = new_orientation % 360

    return new_orientation


def transform(position, instruction):
    x, y, angle = position
    command, value = instruction

    if command == 'F':
        direction = COMPASS[angle]
        x, y = move(x, y, value, direction)
    elif command in ['N', 'S', 'E', 'W']:
        x, y = move(x, y, value, command)
    elif command in ['L', 'R']:
        angle = rotate(angle, command, value)

    return (x, y, angle)


def manhattan_distance(position):
    x, y, _ = position
    return abs(x) + abs(y)


def part1(file):
    position = (0, 0, 0)  # x, y, angle
    instructions = load_program(file)
    for instruction in instructions:
        position = transform(position, instruction)
    print('part 1:', manhattan_distance(position))


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_12_input.txt')
    part1(file)


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_12_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    main()
