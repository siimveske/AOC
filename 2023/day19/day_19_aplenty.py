import collections
import os
import re


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        workflows, ratings = f.read().split('\n\n')
        workflows = workflows.splitlines()
        ratings = ratings.splitlines()

        xmas_workflows = {}
        for workflow in workflows:
            name, cmd = workflow.split('{')
            cmd = cmd[:-1]
            cmd = cmd.split(',')
            xmas_workflows[name] = cmd

        xmas_pattern = r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}"
        xmas_ratings = []
        for rating in ratings:
            match = re.search(xmas_pattern, rating)
            x, m, a, s = match.groups()
            xmas_ratings.append({'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)})

        return xmas_ratings, xmas_workflows


def part1(input_file: str) -> int:
    total = 0
    xmas_ratings, xmas_workflows = read_input(input_file)
    for rating in xmas_ratings:
        queue = collections.deque(xmas_workflows['in'])
        while queue:
            cmd = queue.popleft()
            if cmd == 'R':
                break
            elif cmd == 'A':
                total += sum(rating.values())
                break
            elif '<' in cmd:
                condition, next_flow = cmd.split(':')
                letter, val = condition.split('<')
                if rating[letter] < int(val):
                    queue.clear()
                    if next_flow in xmas_workflows:
                        queue.extend(xmas_workflows[next_flow])
                    else:
                        queue.extend(next_flow)
            elif '>' in cmd:
                condition, next_flow = cmd.split(':')
                letter, val = condition.split('>')
                if rating[letter] > int(val):
                    queue.clear()
                    if next_flow in xmas_workflows:
                        queue.extend(xmas_workflows[next_flow])
                    else:
                        queue.extend(next_flow)
            else:
                queue.extend(xmas_workflows[cmd])
    return total


def part2(input_file: str) -> int:
    tokens = read_input(input_file)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 19114
    print('Part 1 OK')

    # assert part2(filename) == 952408144115
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 323625
    # assert solution_part2 == 52240187443190


if __name__ == '__main__':
    test()
    main()
