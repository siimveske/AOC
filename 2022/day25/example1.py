'''https://github.com/greb/aoc2022/blob/master/days/day25.py'''
import os


def parse(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as f:
        data = f.read().splitlines()

    return data


def decode(n):
    out = 0
    for d in n:
        out *= 5
        match d:
            case '2':
                out += 2
            case '1':
                out += 1
            case '-':
                out -= 1
            case '=':
                out -= 2
    return out


def encode(n):
    out = []
    while n:
        d = n % 5
        match d:
            case 0:
                out.append('0')
            case 1:
                out.append('1')
            case 2:
                out.append('2')
            case 3:
                out.append('=')
                n += 2
            case 4:
                out.append('-')
                n += 1
        n //= 5
    return ''.join(reversed(out))


def part1(numbers):
    s = sum(map(decode, numbers))
    return encode(s)


data = parse('input.txt')
print(part1(data))
