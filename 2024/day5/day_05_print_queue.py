from collections import defaultdict
import os


def read_input(filename: str) -> tuple[dict, list[list[int]]]:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, filename)

    rules = defaultdict(set)
    pages = []
    with open(input_path, 'r', encoding='utf-8') as file:
        rule_text, page_text = file.read().split('\n\n')
        for rule in rule_text.splitlines():
            key, value = map(int, rule.split('|'))
            rules[key].add(value)
        for page in page_text.splitlines():
            pages.append(list(map(int, page.split(','))))

    return rules, pages


def filter_valid_pages(rules: dict, pages: list) -> list:
    filtered_pages = []

    for page_list in pages:
        is_valid = True

        for i, page in enumerate(page_list[:-1]):
            next_page = page_list[i + 1]
            if next_page not in rules[page]:
                is_valid = False
                break

        if is_valid:
            filtered_pages.append(page_list)

    return filtered_pages

def part1(input_file: str) -> int:
    """Returns the sum of the middle pages after filtering pages according to rules."""
    rules, page_lists = read_input(input_file)
    valid_page_lists = filter_valid_pages(rules, page_lists)
    middle_pages = [page_list[len(page_list) // 2] for page_list in valid_page_lists]
    return sum(middle_pages)


# def part2(input_file: str) -> int:
#     first_list, second_list = read_input(input_file)
#     total = 0
#     count_map = {}

#     for num in first_list:
#         if num not in count_map:
#             count_map[num] = second_list.count(num)
#         total += num * count_map[num]

#     return total



def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 143
    print('Part 1 OK')

    # assert part2(filename) == 31
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 4814
    # assert solution_part2 == 20520794


if __name__ == '__main__':
    test()
    main()
