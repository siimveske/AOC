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
    valid_tickets = []

    for ticket in tickets['nearby_tickets']:
        is_valid_ticket = True
        for value in ticket:
            valid = False
            for lstart, lstop, ustart, ustop in tickets['notes'].values():
                if (lstart <= value <= lstop) or (ustart <= value <= ustop):
                    valid = True
                    break
            if not valid:
                is_valid_ticket = False
                errors.append(value)
        if is_valid_ticket:
            valid_tickets.append(ticket)

    valid_tickets.append(tickets['your_ticket'])
    return (errors, valid_tickets)


def part1(file):
    tickets = parse_tickets(file)
    errors, _ = validate_tickets(tickets)
    error_rate = sum(errors)
    print('part 1:', error_rate)
    return error_rate


def part2(file):
    tickets = parse_tickets(file)
    _, validated_tickets = validate_tickets(tickets)

    field_map = {}
    cols = len(validated_tickets[0])
    sets = defaultdict(set)

    for field, rules in tickets['notes'].items():
        lstart, lstop, ustart, ustop = rules
        for col in range(cols):
            valid = True
            for ticket in validated_tickets:
                value = ticket[col]
                if not(lstart <= value <= lstop) and not(ustart <= value <= ustop):
                    valid = False
                    break
            if valid:
                sets[field].add(col)

    while len(sets.keys()) > 0:
        for name, fieldset in sets.items():
            if len(fieldset) == 1:
                field_map[list(fieldset)[0]] = name
                break

        sets.pop(name)
        for i in sets.keys():
            sets[i] = sets[i] - fieldset

    result = 1
    your_ticket = tickets['your_ticket']
    for index, name in field_map.items():
        if name.startswith('departure'):
            result *= your_ticket[index]

    print('part 2:', result)
    return field_map


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_16_input.txt')
    assert part1(file) == 71

    file = os.path.join('..', 'test', 'day_16_input2.txt')
    fields = part2(file)
    assert fields[0] == 'row'
    assert fields[1] == 'class'
    assert fields[2] == 'seat'


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_16_input.txt')
    part1(file)
    part2(file)


if __name__ == '__main__':
    test()
    main()
