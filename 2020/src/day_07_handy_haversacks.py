import os
import re


def parseRules(filename):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    rules = {}
    with open(input_file_path, 'r') as file:
        for line in file:
            bag, content = line.split(' bags contain ')
            inner_bags = re.findall('([0-9]+) ([a-z]+ [a-z]+)', content)
            rules[bag] = {clr:int(cnt) for cnt, clr in inner_bags}
    return rules


def isValidContainer(rules, key, value):
    if not rules[key]:
        return False
    if value in rules[key].keys():
        return True

    for color in rules[key].keys():
        if isValidContainer(rules, color, value):
            return True

    return False


def getValidContainers(rules, bag='shiny gold'):
    valid_containers = []
    for clr in rules.keys():
        if clr == bag:
            continue
        if isValidContainer(rules, clr, bag):
            valid_containers.append(clr)
    return valid_containers


def countBags(rules, bag='shiny gold'):
    return sum([n + n * countBags(rules, inner_bag) for inner_bag, n in rules[bag].items()])


def test():
    print('---- TEST ----')
    filepath = os.path.join('..', 'test', 'day_07_input.txt')
    rules = parseRules(filepath)
    containers = getValidContainers(rules)

    print(f"Part 1 solution: {len(containers)}")

    bagCount1 = countBags(rules)
    filepath = os.path.join('..', 'test', 'day_07_input2.txt')
    rules = parseRules(filepath)
    bagCount2 = countBags(rules)

    print(f"Part 2 solution 1: {bagCount1}")
    print(f"Part 2 solution 2: {bagCount2}")
    print()
    
    assert bagCount1 == 32
    assert bagCount2 == 126


def main():
    print('---- PROGRAM ----')
    filepath = os.path.join('..', 'data', 'day_07_input.txt')
    rules = parseRules(filepath)
    containers = getValidContainers(rules)
    bagCount = countBags(rules)

    print(f"Part 1 solution: {len(containers)}")
    print(f"Part 2 solution: {bagCount}\n")


if __name__ == '__main__':
    test()
    main()
