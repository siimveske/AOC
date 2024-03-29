from __future__ import annotations
import os
from typing import Callable


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


def is_nice(text: str) -> bool:
    vowels = set([*'aeiou'])
    bad_letters = set(['ab', 'cd', 'pq', 'xy'])

    vowel_cnt = 0
    has_doubble_letter = False

    for i in range(len(text) - 1):
        a = text[i]
        b = text[i + 1]
        ab = a + b

        if ab in bad_letters:
            return False
        if a == b:
            has_doubble_letter = True
        if a in vowels:
            vowel_cnt += 1

    if b in vowels:
        vowel_cnt += 1

    return (vowel_cnt >= 3) and has_doubble_letter


def is_nice2(text:str) -> bool:
    has_repeating_letter = False
    for i in range(len(text) - 2):
        if text[i] == text[i + 2]:
            has_repeating_letter = True
            break
    if has_repeating_letter == False:
        return False

    for i in range(len(text) - 2):
        pair = text[i:i + 2]
        if pair in text[i + 2:]:
            return True

    return False


def count_nice(strings: list, is_nice: Callable[str, bool]) -> int:
    cnt = 0
    for string in strings:
        if is_nice(string):
            cnt += 1
    return cnt


def part1(inputFile: str) -> int:
    strings = readInput(inputFile)
    return count_nice(strings, is_nice)


def part2(inputFile: str) -> int:
    strings = readInput(inputFile)
    return count_nice(strings, is_nice2)


def test():
    print('---- TEST ----')

    assert is_nice('aaa') == True
    assert is_nice('ugknbfddgicrmopn') == True
    assert is_nice('jchzalrnumimnmhp') == False
    assert is_nice('haegwjzuvuyypxyu') == False
    assert is_nice('dvszwmarrgswjxmb') == False
    print('Part 1 OK')

    assert is_nice2('qjhvhtzxzqqjkmpb') == True
    assert is_nice2('xxyxx') == True
    assert is_nice2('uurcxstgmygtbstg') == False
    assert is_nice2('ieodomkazucvgmuy') == False

    print('Part 2 OK\n')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')


if __name__ == '__main__':
    test()
    main()
