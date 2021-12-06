import os


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        numbers = [int(i) for i in f.readline().split(',')]
        board = []
        boards = []
        for line in f:
            if line == '\n':
                if board:
                    boards.append(board)
                    board = []
            else:
                board.append([int(i) for i in line.split()])
        else:
            boards.append(board)
            board = []

    return (numbers, boards)


def play_bingo(numbers, boards):

    # Check rows
    drawn_numbers = numbers[0:5]
    for nr in numbers[5:]:
        for board in boards:
            for row in range(5):
                h_bingo = True
                v_bingo = True
                for col in range(5):
                    if board[row][col] not in drawn_numbers:
                        h_bingo = False
                    if board[col][row] not in drawn_numbers:
                        v_bingo = False
                    if not h_bingo and not v_bingo:
                        break
                    if col == 4:
                        unmarked_numbers = get_unmarked_numbers(board, drawn_numbers)
                        return sum(unmarked_numbers) * drawn_numbers[-1]

        drawn_numbers.append(nr)

    raise Exception("Failed to solve bingo!")


def play_bingo2(numbers, boards):

    completed_boards = []
    drawn_numbers = numbers[0:5]
    for nr in numbers[5:]:
        for board in boards:
            if board in completed_boards:
                continue

            # Check rows
            for row in range(5):
                if board in completed_boards:
                    break
                h_bingo = True
                v_bingo = True
                for col in range(5):
                    if board[row][col] not in drawn_numbers:
                        h_bingo = False
                    if board[col][row] not in drawn_numbers:
                        v_bingo = False
                    if not h_bingo and not v_bingo:
                        break
                    if col == 4:
                        completed_boards.append(board)
                        if len(completed_boards) == len(boards):
                            unmarked_numbers = get_unmarked_numbers(board, drawn_numbers)
                            return sum(unmarked_numbers) * drawn_numbers[-1]

        drawn_numbers.append(nr)

    raise Exception("Failed to solve bingo!")


def get_unmarked_numbers(board, drawn_numbers):
    unmarked_numbers = []
    for row in board:
        for nr in row:
            if nr not in drawn_numbers:
                unmarked_numbers.append(nr)
    return unmarked_numbers


def part1(inputFile: str):
    numbers, boards = readInput(inputFile)
    return play_bingo(numbers, boards)


def part2(inputFile: str):
    numbers, boards = readInput(inputFile)
    return play_bingo2(numbers, boards)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'
    assert part1(filename) == 4512
    print('Part 1 OK')
    assert part2(filename) == 1924
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
