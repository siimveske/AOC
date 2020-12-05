import os
import math


def readFile(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    data = []
    with open(input_file_path, 'r') as file:
        for line in file:
            data.append(line.strip())

    return data


def decode(raw_tickets):
    decoded_tickets = []
    for ticket in raw_tickets:
        rows = ticket[:7]
        cols = ticket[7:]
        row = search(rows, 0, 127)
        col = search(cols, 0, 7)
        ticket_id = row * 8 + col
        print("%s: row %s, column %s, seat ID %s" % (ticket, row, col, ticket_id))
        decoded_tickets.append({'row': row, 'col': col, 'id': ticket_id})
    return decoded_tickets


def search(ticket, start, stop):
    if start == stop:
        return start

    delta = stop - start
    if ticket[0] in ['F', 'L']:
        new_stop = start + math.floor(delta / 2)
        return search(ticket[1:], start, new_stop)
    else:
        new_start = start + math.ceil(delta / 2)
        return search(ticket[1:], new_start, stop)


def getMaxID(tickets):
    max_id = 0
    for ticket in tickets:
        if ticket['id'] > max_id:
            max_id = ticket['id']
    print("Highest seat ID on a boarding pass: %s" % max_id)


def getMissingID(tickets):
    sorted_tickets = sorted(tickets, key=lambda i: i['id'])

    index = sorted_tickets[0]['id']  # Lowest id
    for ticket in sorted_tickets:
        if ticket['id'] != index:
            print("Missing seat ID: %s" % index)
            break
        index += 1


def main():
    print("---- PROGRAM ----")
    raw_tickets = readFile('day_05_input.txt')
    tickets = decode(raw_tickets)
    getMaxID(tickets)
    getMissingID(tickets)


def test():
    print("---- TEST ----")

    raw_tickets = readFile('day_05_test_input.txt')
    tickets = decode(raw_tickets)
    getMaxID(tickets)
    # FBFBBFFRLR
    assert tickets[0]['row'] == 44
    assert tickets[0]['col'] == 5
    assert tickets[0]['id'] == 357

        # FBFBBFFRLR
    assert tickets[1]['row'] == 70
    assert tickets[1]['col'] == 7
    assert tickets[1]['id'] == 567

        # FBFBBFFRLR
    assert tickets[2]['row'] == 14
    assert tickets[2]['col'] == 7
    assert tickets[2]['id'] == 119

        # FBFBBFFRLR
    assert tickets[3]['row'] == 102
    assert tickets[3]['col'] == 4
    assert tickets[3]['id'] == 820

    print()


if __name__ == '__main__':
    test()
    main()
