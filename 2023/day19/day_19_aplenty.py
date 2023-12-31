import collections
import os
import re
from copy import deepcopy


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        workflows, ratings = f.read().split('\n\n')
        workflows = workflows.splitlines()
        ratings = ratings.splitlines()

        xmas_workflows = {'A': 'A', 'R': 'R'}
        workflow_pattern = r'([xmas])([<>])(\d+):([a-zA-Z]+)'
        for workflow in workflows:
            name, cmd = workflow.split('{')
            cmd = cmd[:-1]
            cmd = cmd.split(',')
            last_cmd = cmd.pop()
            cmd_list = []
            for c in cmd:
                a, op, b, func = re.search(workflow_pattern, c).groups()
                cmd_list.append((a, op, int(b), func))
            cmd_list.append(last_cmd)
            xmas_workflows[name] = cmd_list

        xmas_pattern = r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}'
        xmas_ratings = []
        for rating in ratings:
            match = re.search(xmas_pattern, rating)
            x, m, a, s = match.groups()
            xmas_ratings.append({'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)})

        return xmas_ratings, xmas_workflows


def part1(input_file: str) -> int:
    total = 0
    ratings, rules = read_input(input_file)
    for rating in ratings:
        queue = collections.deque(rules['in'])
        while queue:
            rule = queue.popleft()
            if rule == 'R':
                break
            elif rule == 'A':
                total += sum(rating.values())
                break
            elif '<' in rule:
                category, op, val, next_rule = rule
                if rating[category] < val:
                    queue.clear()
                    queue.extend(rules[next_rule])
            elif '>' in rule:
                category, op, val, next_rule = rule
                if rating[category] > val:
                    queue.clear()
                    queue.extend(rules[next_rule])
            else:
                queue.extend(rules[rule])
    return total


def part2(input_file: str) -> int:
    _, WORKFLOW_MAP = read_input(input_file)

    def propagate_workflow(current_workflow, ranges):
        """Recursive function that propagates among different branching workflows
        Accepted/Rejected intervals + current workflow state get updated and function is called again
        until current workflow is in 'A' or 'R' (terminal condition).

        Args:
            current_workflow (str): current workflow key
            ranges (dict[str, range]): current possible intervals for variables x,m,a,s

        Returns:
            count: total count of combination of accepted pieces quadruplet (x,m,a,s)

        Link to initial solution:
            https://github.com/henriupton99/AdventOfCode/blob/main/2023/day_19/sub_part2.py
        """

        # If current workflow is A (accepted), we reach a valid terminal branch:
        # we compute the total possibilities by prod_{i in (x,m,a,s)}(len(values_intervals_{i}))
        if current_workflow == 'A':
            possibilities = 1
            for i in 'xmas':
                possibilities *= len(ranges[i])
            return possibilities

        # If current workflow is R (rejected), we reach an unvalid terminal branch:
        # we don't update the count and return 0
        if current_workflow == 'R':
            return 0

        # Otherwise, we aren't in a terminal state and need to continue branching search:
        count = 0
        # loop over all rules of the current workflow:
        for rule in WORKFLOW_MAP[current_workflow]:
            if '<' in rule or '>' in rule:
                category, op, value, next_workflow = rule
                start, stop = ranges[category].start, ranges[category].stop
                # Case of rule type 'category < value'
                # We split the full package of values into two groups:
                #   1. branch_acceped: ranges of values that match the condition
                #   2. branch_rejected: ranges of values that doesnt match the conditions
                if op == '<':
                    # Compute the ranges for accepted and rejected:
                    branch_accepted = range(start, value)
                    branch_rejected = range(value, stop)

                # Case of rule type 'category > value'
                else:
                    branch_accepted = range(value + 1, stop)
                    branch_rejected = range(start, value + 1)

                # Deep copy in order to get detached from origin ranges:
                accepted_ranges = deepcopy(ranges)

                # Update intervals of concerned category and assign branch_rejected to ranges
                accepted_ranges[category] = branch_accepted
                ranges[category] = branch_rejected

                # Propagate the process for accepted_intervals into the associated workflow:
                count += propagate_workflow(next_workflow, accepted_ranges)

            else:
                next_workflow = rule
                count += propagate_workflow(next_workflow, ranges)
        return count

    intervals = {i: range(1, 4001) for i in 'xmas'}
    result = propagate_workflow('in', intervals)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 19114
    print('Part 1 OK')

    assert part2(filename) == 167409079868000
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 323625
    assert solution_part2 == 127447746739409


if __name__ == '__main__':
    test()
    main()
