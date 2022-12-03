import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    shape_map = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    instructions = []
    with open(input_file_path, 'r') as f:
        for line in f:
            a, b = line.strip().split(' ')
            instructions.append((shape_map[a], shape_map[b]))

    return instructions


def part1(inputFile: str):
    instructions = readInput(inputFile)
    
    score = 0
    win_map = {1:2, 2:3, 3:1}
    for him, me in instructions:
        
        # shape you selected
        score += me
        
        # round was a draw
        if me == him:
            score += 3
        # you won
        elif win_map[him] == me:
            score += 6
    
    return score
        

def part2(inputFile: str):
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 15
    print('Part 1 OK')
    #assert part2(filename) == 900
    #print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'
    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
