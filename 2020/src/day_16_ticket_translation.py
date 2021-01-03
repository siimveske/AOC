import os
from collections import defaultdict


class State:
    FIELDS = 0
    YOUR_TICKET = 1
    NEARBY_TICKET = 2


def parse_tickets(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    data = defaultdict(list)
    data['notes'] = defaultdict(list)
    state = State.FIELDS
    with open(input_file_path, 'r') as file:
        for line in file:

            # ignore empty lines
            if not line.strip():
                continue

            # set parsing state so we know what section is being parsed next
            if 'your ticket' in line:
                state = State.YOUR_TICKET
                continue
            elif 'nearby tickets' in line:
                state = State.NEARBY_TICKET
                continue

            if state == State.FIELDS:
                field, ranges = line.split(':')
                lower_ranges, upper_ranges = ranges.split('or')
                lower_start, lower_stop = [int(i) for i in lower_ranges.split('-')]
                upper_start, upper_stop = [int(i) for i in upper_ranges.split('-')]
                data['notes'][field] = [lower_start, lower_stop, upper_start, upper_stop]

            elif state == State.YOUR_TICKET:
                your_ticket = [int(i) for i in line.split(',')]
                data['your_ticket'] = your_ticket
            else:
                nearby_ticket = [int(i) for i in line.split(',')]
                data['nearby_tickets'].append(nearby_ticket)

    return data


def validate_tickets(tickets):
    errors = []
    for ticket in tickets['nearby_tickets']:
        for value in ticket:
            valid = False
            for lstart, lstop, ustart, ustop in tickets['notes'].values():
                if (lstart <= value <= lstop) or (ustart <= value <= ustop):
                    valid = True
                    break
            if not valid:
                errors.append(value)
    return errors


def part1(file):
    tickets = parse_tickets(file)
    error_rate = sum(validate_tickets(tickets))
    print('part 1:', error_rate)
    return error_rate


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_16_input.txt')
    assert part1(file) == 71


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_16_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    main()
