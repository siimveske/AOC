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


def hasGold(bag, rules):
    for inner_bag in rules[bag]:
        return (inner_bag == 'shiny gold' or hasGold(inner_bag, rules))


def getValidContainers(rules):
    return [bag for bag in rules if hasGold(bag, rules)]


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
