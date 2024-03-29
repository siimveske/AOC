'''
https://www.reddit.com/r/adventofcode/comments/3vr4m4/comment/cxpz4tq/?utm_source=share&utm_medium=web2x&context=3
'''
calc = dict()
results = dict()

with open('input.txt', 'r') as f:
    commands = f.readlines()

for command in commands:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
                res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
                res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
                res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
                res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]


part1 = calculate('a')
calc['b'] = [str(part1)]
results = dict()
part2 = calculate('a')
print("part1: %d" % part1)
print("part2: %d" % part2)
