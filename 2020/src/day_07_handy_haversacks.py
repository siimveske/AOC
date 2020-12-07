import os
import re


def parseRules(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    rules = {}
    pattern = '([0-9]+) ([a-z]+ [a-z]+)'
    with open(input_file_path, 'r') as file:
        for line in file:
            container, content = line.split('bags contain')
            result = re.findall(pattern, content)

            colors = []
            if result:
                for _, clr in result:
                    colors.append(clr)
            rules[container.strip()] = colors
    
    return rules


def isValidContainer(rules, key, value):
    if not rules[key]:
        return False
    if value in rules[key]:
        return True
    
    for color in rules[key]:
        if isValidContainer(rules, color, value):
            return True
        
    return False


def getValidContainers(rules, color='shiny gold'):
    valid_containers = []
    for clr in rules.keys():
        if clr == color:
            continue
        if isValidContainer(rules, clr, color):
            valid_containers.append(clr)
    return valid_containers


def test():
    print('---- TEST ----')
    filepath = os.path.join('..', 'test', 'day_07_input.txt')
    rules = parseRules(filepath)
    containers = getValidContainers(rules)
    print(f"Valid containers: {containers}")
    print(f"Part 1 solution: {len(containers)}\n")


def main():
    print('---- PROGRAM ----')
    filepath = os.path.join('..', 'data', 'day_07_input.txt')
    rules = parseRules(filepath)
    containers = getValidContainers(rules)
    print(f"Valid containers: {containers}")
    print(f"Part 1 solution: {len(containers)}")


if __name__ == '__main__':
    test()
    main()