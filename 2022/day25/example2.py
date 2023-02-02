s_to_d = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
d_to_s = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}

def from_snafu(number):
    return sum(s_to_d[c] * 5**p for (p,c) in enumerate(number[::-1]))

def to_snafu(number):
    snafu = ''
    while number > 0:
        number, rem = divmod(number, 5)
        snafu += d_to_s[rem]
        if rem > 2:
            number += 1
    return snafu[::-1] if snafu else '0'

print(to_snafu(sum(from_snafu(l.strip()) for l in open('input'))))