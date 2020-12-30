import os


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        instructions = [(line[0], int(line[1:])) for line in file]

    return instructions


def move_waypoint(waypoint, amount, direction):
    x, y = waypoint
    return {
        'E': (x + amount, y),
        'W': (x - amount, y),
        'N': (x, y + amount),
        'S': (x, y - amount)
    }[direction]


def update_direction(direction, side, degrees):
    return {
        'N': 'NESW',
        'E': 'ESWN',
        'S': 'SWNE',
        'W': 'WNES'
    }[direction][(degrees if side == 'R' else 360 - degrees) // 90]


def rotate_waypoint(waypoint, direction, amount):
    x, y = waypoint
    return {
         90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }[amount if direction == 'R' else 360 - amount]


def move_ship(waypoint, ship, amount):
    xWp, yWp = waypoint
    xS, yS = ship
    return (xS + xWp * amount, yS + yWp * amount)


def manhattan_distance(position):
    x, y = position[0], position[1]
    return abs(x) + abs(y)


def part1(file):
    instructions = load_program(file)

    direction = 'E'
    waypoint = (0, 0)
    for command, value in instructions:
        if command == 'F':
            waypoint = move_waypoint(waypoint, value, direction)
        elif command in 'NSEW':
            waypoint = move_waypoint(waypoint, value, command)
        elif command in 'LR':
            direction = update_direction(direction, command, value)

    distance = manhattan_distance(waypoint)
    print('part 1:', distance)

    return distance


def part2(file):
    instructions = load_program(file)

    ship = (0, 0)
    waypoint = (10, 1)
    for command, value in instructions:
        if command == 'F':
            ship = move_ship(waypoint, ship, value)
        elif command in 'NSEW':
            waypoint = move_waypoint(waypoint, value, command)
        elif command in 'LR':
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
