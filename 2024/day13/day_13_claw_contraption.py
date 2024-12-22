import os
import re
import numpy as np


def read_input(filename: str) -> list:
    file_path = os.path.join(os.path.dirname(__file__), filename)

    configurations = []
    with open(file_path, 'r') as file:
        for machine in file.read().split('\n\n'):
            parsed_data: list = []
            for line in machine.split('\n'):
                numbers = re.findall(r'(\d+)', line)
                numbers = list(tuple(map(int, numbers)))
                parsed_data.append(numbers)
            configurations.append(parsed_data)
    return configurations


def press(config: tuple, btn_a_cnt: int, btn_b_cnt: int, memo: dict) -> int:
    btn_a, btn_b, dst = config
    btn_a_x, btn_a_y = btn_a
    btn_b_x, btn_b_y = btn_b
    dst_x, dst_y = dst

    key = (btn_a_cnt, btn_b_cnt)
    if key in memo:
        return memo[key]

    if btn_a_cnt > 100 or btn_b_cnt > 100:
        return float('inf')

    # Calculate current position
    x = btn_a_cnt * btn_a_x + btn_b_cnt * btn_b_x
    y = btn_a_cnt * btn_a_y + btn_b_cnt * btn_b_y

    if x > dst_x or y > dst_y:
        return float('inf')

    if x == dst_x and y == dst_y:
        return 3 * btn_a_cnt + btn_b_cnt

    result = float('inf')
    result = min(result, press(config, btn_a_cnt + 1, btn_b_cnt, memo))
    result = min(result, press(config, btn_a_cnt, btn_b_cnt + 1, memo))
    result = min(result, press(config, btn_a_cnt + 1, btn_b_cnt + 1, memo))

    # Use dynamic programming to avoid redundant calculations
    memo[key] = result
    return result


def part1(input_file: str) -> int:
    configs = read_input(input_file)
    result = 0
    for config in configs:
        r = press(config, btn_a_cnt=0, btn_b_cnt=0, memo={})
        if r != float('inf'):
            result += r
    return result


def part2(input_file: str) -> int:
    configurations = read_input(input_file)
    offset = 10**13
    total_cost = 0
    for configuration in configurations:
        button_a, button_b, destination = configuration
        ax, ay = button_a
        bx, by = button_b
        dx, dy = [value + offset for value in destination]

        matrix_a = np.array([[ax, bx], [ay, by]])
        vector_b = np.array([[dx], [dy]])

        solution = np.linalg.solve(matrix_a, vector_b).round()
        a = solution[0][0]
        b = solution[1][0]

        if (a * ax + b * bx) == dx and (a * ay + b * by) == dy:
            total_cost += 3 * a + b

    return total_cost

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 480
    print('Part 1 OK')

    assert part2(filename) == 875318608908
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 28753
    assert solution_part2 == 102718967795500


if __name__ == '__main__':
    test()
    main()
