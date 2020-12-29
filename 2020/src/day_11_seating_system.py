import os
import copy

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'


def load_program(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        plan = [list(line.strip()) for line in file]

    return plan


def get_occupied_seat_count(plan, row, col):
    count = 0

    top = max(row - 1, 0)
    bottom = min(row + 2, len(plan))
    left = max(col - 1, 0)
    right = min(col + 2, len(plan[row]))

    for i in range(top, bottom):
        for j in range(left, right):
            if i == row and j == col:
                continue
            if plan[i][j] == OCCUPIED:
                count += 1

    return count


def get_occupied_visible_seat_count(plan, row, col):

    top = 0
    bottom = len(plan)
    left = 0
    right = len(plan[row])

    count = 0

    # Check left
    j = col - 1
    while j >= left:
        item = plan[row][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        j -= 1

    # Check right
    j = col + 1
    while j < right:
        item = plan[row][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        j += 1

    # Check top
    i = row - 1
    while i >= top:
        item = plan[i][col]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i -= 1

    # Check bottom
    i = row + 1
    while i < bottom:
        item = plan[i][col]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i += 1

    # Check top-left
    i = row - 1
    j = col - 1
    while i >= top and j >= left:
        item = plan[i][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i -= 1
        j -= 1

    # Check top-right
    i = row - 1
    j = col + 1
    while i >= top and j < right:
        item = plan[i][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i -= 1
        j += 1

    # Check bottom-right
    i = row + 1
    j = col + 1
    while i < bottom and j < right:
        item = plan[i][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i += 1
        j += 1

    # Check bottom-left
    i = row + 1
    j = col - 1
    while i < bottom and j >= left:
        item = plan[i][j]
        if item == EMPTY:
            break
        if item == OCCUPIED:
            count += 1
            break
        i += 1
        j -= 1

    return count


def distribute_people(plan):
    new_plan = copy.deepcopy(plan)

    for row in range(len(plan)):
        for col in range(len(plan[row])):
            seat = plan[row][col]
            if seat == FLOOR:
                continue
            cnt = get_occupied_seat_count(plan, row, col)
            if seat == EMPTY and cnt == 0:
                new_plan[row][col] = OCCUPIED
            elif seat == OCCUPIED and cnt >= 4:
                new_plan[row][col] = EMPTY

    return new_plan


def distribute_people2(plan):
    new_plan = copy.deepcopy(plan)

    for row in range(len(plan)):
        for col in range(len(plan[row])):
            seat = plan[row][col]
            if seat == FLOOR:
                continue
            cnt = get_occupied_visible_seat_count(plan, row, col)
            if seat == EMPTY and cnt == 0:
                new_plan[row][col] = OCCUPIED
            elif seat == OCCUPIED and cnt >= 5:
                new_plan[row][col] = EMPTY

    return new_plan


def print_plan(plan):
    for row in range(len(plan)):
        for col in range(len(plan[row])):
            print(plan[row][col], end=" "),
        print()


def is_equal(l1, l2):
    num_equal = sum(x == y for x, y in zip(l1, l2))
    return num_equal == len(l1) == len(l2)


def count_seats(plan):
    seat_count = 0
    for row in range(len(plan)):
        for col in range(len(plan[row])):
            if plan[row][col] == OCCUPIED:
                seat_count += 1
    return seat_count


def part1(plan):
    # count = 1
    while True:
        # print(f'round ', count)
        new_plan = distribute_people(plan)
        # print_plan(new_plan)
        if is_equal(plan, new_plan):
            break
        else:
            plan = new_plan
            # count += 1

    seat_count = count_seats(plan)
    print("part 1: ", seat_count)


def part2(plan):
    # count = 1
    # print_plan(plan)
    while True:
        # print(f'round ', count)
        new_plan = distribute_people2(plan)
        # print_plan(new_plan)
        if is_equal(plan, new_plan):
            break
        else:
            plan = new_plan
            # count += 1

    seat_count = count_seats(plan)
    print("part 2: ", seat_count)


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_11_input.txt')
    plan = load_program(file)
    part1(plan)
    part2(plan)


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_11_input.txt')
    plan = load_program(file)
    part1(plan)
    part2(plan)


if __name__ == '__main__':
    # test()
    main()
