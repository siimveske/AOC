import os
import math

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


def move_waypoint(waypoint, amount, direction):
    x, y = waypoint
    if direction == 'E':
        return (x + amount, y)
    if direction == 'W':
        return (x - amount, y)
    if direction == 'N':
        return (x, y + amount)
    if direction == 'S':
        return (x, y - amount)


def update_angle(angle, direction, amount):
    if direction == 'L':
        new_orientation = angle - amount
        if new_orientation <= -360:
            new_orientation = new_orientation % -360
    elif direction == 'R':
        new_orientation = angle + amount
        if new_orientation >= 360:
            new_orientation = new_orientation % 360

    return new_orientation


def rotate_waypoint(waypoint, direction, amount):
    px, py = waypoint

    if direction == 'R':
        amount *= -1
    angle = math.radians(amount)

    qx = math.cos(angle) * px - math.sin(angle) * py
    qy = math.sin(angle) * px + math.cos(angle) * py

    return (qx, qy)


def move_ship(waypoint, ship, amount):
    xWp, yWp = waypoint
    xS, yS = ship
    return (xS + xWp * amount, yS + yWp * amount)


def manhattan_distance(position):
    x, y = position[0], position[1]
    return int(abs(x) + abs(y))


def part1(file):
    instructions = load_program(file)

    angle = 0
    waypoint = (0, 0)
    for instruction in instructions:
        command, value = instruction
        if command == 'F':
            direction = COMPASS[angle]
            waypoint = move_waypoint(waypoint, value, direction)
        elif command in ['N', 'S', 'E', 'W']:
            waypoint = move_waypoint(waypoint, value, command)
        elif command in ['L', 'R']:
            angle = update_angle(angle, command, value)

    distance = manhattan_distance(waypoint)
    print('part 1:', distance)

    return distance


def part2(file):
    instructions = load_program(file)

    ship = (0, 0)
    waypoint = (10, 1)
    for instruction in instructions:
        command, value = instruction
        if command == 'F':
            ship = move_ship(waypoint, ship, value)
        elif command in ['N', 'S', 'E', 'W']:
            waypoint = move_waypoint(waypoint, value, command)
        elif command in ['L', 'R']:
            waypoint = rotate_waypoint(waypoint, command, value)

    distance = manhattan_distance(ship)
    print('part 2:', distance)
    return distance


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_12_input.txt')
    assert part1(file) == 25
    assert part2(file) == 286


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_12_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    test()
    main()
