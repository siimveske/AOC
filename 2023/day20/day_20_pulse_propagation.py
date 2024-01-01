import collections
import os
from enum import Enum


class ModuleType(Enum):
    FLIPFLOP = 1
    CONJUNCTION = 2
    BROADCASTER = 3


class Module:
    def __init__(self, module_name: str, module_type: ModuleType, outputs: list[str]):
        self.name = module_name
        self.type = module_type
        self.outputs = outputs

        if self.type == ModuleType.FLIPFLOP:
            self.memory = False
        elif self.type == ModuleType.CONJUNCTION:
            self.memory = {}

    def update_state(self, sender: str, pulse: bool):
        if self.type == ModuleType.FLIPFLOP:
            if not pulse:
                self.memory = not self.memory
                return self.memory

        elif self.type == ModuleType.CONJUNCTION:
            self.memory[sender] = pulse
            return False if all([i for i in self.memory.values()]) else True

        return None


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            name, outputs = line.split(' -> ')
            prefix = name[0]
            name = name[1:]
            outputs = outputs.split(', ')
            if prefix == 'b':
                graph['broadcaster'] = Module('broadcaster', ModuleType.BROADCASTER, outputs)
            elif prefix == '%':
                graph[name] = Module(name, ModuleType.FLIPFLOP, outputs)
            elif prefix == '&':
                graph[name] = Module(name, ModuleType.CONJUNCTION, outputs)

    for name, module in graph.items():
        for output in module.outputs:
            if output in graph and graph[output].type == ModuleType.CONJUNCTION:
                graph[output].memory[name] = False

    return graph


def part1(input_file: str) -> int:
    graph = read_input(input_file)
    broadcaster = graph.get('broadcaster')

    low, high = 0, 0
    for i in range(1000):
        low += 1
        q = collections.deque([('broadcaster', destination, False) for destination in broadcaster.outputs])
        while q:
            src, dst, pulse = q.popleft()
            # print(f'{src} -> {pulse} -> {dst}')
            if pulse:
                high += 1
            else:
                low += 1

            # skip the 'output' debug node
            if dst not in graph:
                continue

            module = graph[dst]
            out_pulse = module.update_state(src, pulse)
            if out_pulse is not None:
                for output in module.outputs:
                    q.append((module.name, output, out_pulse))

    return low * high


def part2(input_file: str) -> int:
    WORKFLOW_MAP = read_input(input_file)


def test():
    print('---- TEST ----')

    filename = 'test_input.txt'
    assert part1(filename) == 32000000

    filename = 'test_input2.txt'
    assert part1(filename) == 11687500

    print('Part 1 OK')

    # assert part2(filename) == 167409079868000
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')

    assert solution_part1 == 898557000
    # assert solution_part2 == 127447746739409


if __name__ == '__main__':
    test()
    main()
