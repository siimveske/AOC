import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    with open(input_file_path, 'r') as f:
        instructions = [line.strip().split(' ') for line in f]

    return instructions


# 1 for Rock, 2 for Paper, and 3 for Scissors
shape_map = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
# Paper defeats Rock, Scissors defeats Paper and Rock defeats Scissors
win_map = {'A':2, 'B':3, 'C':1}
# Rock defeats Scissors, Paper defeats Rock and Scissors defeats Paper
loose_map = {'A':3, 'B':1, 'C':2}


def part1(inputFile: str):
    instructions = readInput(inputFile)
    
    score = 0
    for opponent, me in instructions:
        
        # shape you selected
        score += shape_map[me]
        
        # round was a draw
        if shape_map[me] == shape_map[opponent]:
            score += 3
        # you win
        elif win_map[opponent] == shape_map[me]:
            score += 6
    
    return score
        

def part2(inputFile: str):
    instructions = readInput(inputFile)
    
    score = 0
    for opponent, me in instructions:
        # round was a draw
        if me == 'Y':
            score += (shape_map[opponent] + 3)
        # you win
        elif me == 'Z':
            score += (win_map[opponent] + 6)
        # you loose
        else:
            score += loose_map[opponent]
            
    return score


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 15
    print('Part 1 OK')
    assert part2(filename) == 12
    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
