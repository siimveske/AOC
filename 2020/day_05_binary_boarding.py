import os

class Ticket:
    def __init__(self, row, column, seat_id):
        self.row     = row
        self.column  = column
        self.seat_id = seat_id
        
def readFile(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    data = []
    with open(input_file_path, 'r') as file:
        for line in file:
            data.append(line.strip())
    
    return data

def decode(raw_tickets):
    for ticket in raw_tickets:
        pass
    
def test():
    raw_tickets = readFile('day_05_test_input.txt')
    decoded_tickets = decode(raw_tickets)
    
    # FBFBBFFRLR
    assert decoded_tickets[0].row == 44
    assert decoded_tickets[0].column == 5
    assert decoded_tickets[0].row == 357
    
if __name__ == '__main__':
    test()