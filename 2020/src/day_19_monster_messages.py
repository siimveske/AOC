import os
import re
'''
    1. https://github.com/mebeim/aoc/tree/master/2020#day-19---monster-messages
    2. https://github.com/mdumke/aoc2020/blob/main/day19
'''


def read_file(file):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, file)

    with open(input_file_path, 'r') as file:
        rules, messages = file.read().split('\n\n')
        rules = dict(map(parse_rule, rules.splitlines()))
        messages = messages.splitlines()
        return (rules, messages)


def parse_rule(line):
    i, pattern = line.split(': ')
    if '|' in pattern:
        rule = [
            [int(n) for n in rule.split(' ')] for rule in pattern.split(' | ')
        ]
    elif '"' in pattern:
        rule = pattern[1:-1]
    else:
        rule = [[int(n) for n in pattern.split(' ')]]

    return int(i), rule


def build_regexp(rules, rule=0):
    rule = rules[rule]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        option = ''.join(build_regexp(rules, r) for r in option)
        options.append(option)

    return '(' + '|'.join(options) + ')'


def part1(file):
    rules, messages = read_file(file)
    rexp = re.compile('^' + build_regexp(rules) + '$')

    valid = 0
    for msg in messages:
        if rexp.match(msg):
            valid += 1

    print('part1:', valid)
    return valid


def part2(file):
    pass


def test():
    print('---- TEST ----')
    file = os.path.join('..', 'test', 'day_19_input.txt')
    assert part1(file) == 2


def main():
    print('---- PROGRAM ----')
    file = os.path.join('..', 'data', 'day_19_input.txt')
    part1(file)


if __name__ == '__main__':
    test()
    main()
