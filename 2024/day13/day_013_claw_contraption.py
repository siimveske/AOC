import os
import re

def read_input(filename: str) -> tuple[list[int], list[int]]:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    configurations = []
    with open(input_file_path, 'r') as f:
        machines = f.read().split('\n\n')
        for machine in machines:
            parsed_data = []
            for line in machine.split('\n'):
                numbers = re.findall(r'(\d+)', line)
                numbers = tuple(map(int, numbers))
                parsed_data.append(numbers)
            configurations.append(tuple(parsed_data))
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

    dist_a_x = btn_a_cnt * btn_a_x
    dist_a_y = btn_a_cnt * btn_a_y
    dist_b_x = btn_b_cnt * btn_b_x
    dist_b_y = btn_b_cnt * btn_b_y
    x = dist_a_x + dist_b_x
    y = dist_a_y + dist_b_y
    if x > dst_x or y > dst_y:
        return float('inf')

    if x == dst_x and y == dst_y:
        return 3*btn_a_cnt + btn_b_cnt

    result = []
    result.append(press(config, btn_a_cnt + 1, btn_b_cnt, memo))
    result.append(press(config, btn_a_cnt, btn_b_cnt + 1, memo))
    result.append(press(config, btn_a_cnt + 1, btn_b_cnt + 1, memo))
    result = min(result)

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
    data = read_input(input_file)
    return 0

def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 480
    print('Part 1 OK')

    # assert part2(filename) == 80
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 28753
    # assert solution_part2 == 902742


if __name__ == '__main__':
    test()
    main()
