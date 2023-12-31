import collections
import os
import re
from copy import deepcopy


class Conjunction:
    def __init__(self, name, outputs: list):
        self.name = name
        self.outputs = outputs
        self.inputs = {}
        self.pulse_cnt = {0: 0, 1: 0}

    def set_pulse(self, input_name, pulse):
        self.inputs[input_name] = pulse

    def process(self):
        if all(i == 1 for i in self.inputs.values()):
            for output in self.outputs:
                output.set_pulse(0)
                self.pulse_cnt[0] += 1
        else:
            for output in self.outputs:
                output.set_pulse(1)
                self.pulse_cnt[1] += 1


class FlipFlop:
    def __init__(self, name, outputs: list):
        self.name = name
        self.outputs = outputs
        self.is_on = False
        self.pulse = None
        self.pulse_cnt = {0: 0, 1: 0}

    def set_pulse(self, pulse):
        self.pulse = pulse

    def process(self):
        if self.pulse == 1:
            return []

        if self.is_on:
            self.is_on = False
            for output in self.outputs:
                output.set_pulse(0)
                self.pulse_cnt[0] += 1
        else:
            self.is_on = True
            for output in self.outputs:
                output.set_pulse(1)
                self.pulse_cnt[1] += 1
        return self.outputs


class Broadcaster:
    def __init__(self, outputs: list):
        self.name = 'broadcaster'
        self.outputs = outputs
        self.pulse = None
        self.pulse_cnt = {0: 0, 1: 0}

    def set_pulse(self, pulse):
        self.pulse = pulse

    def process(self):
        for output in self.outputs:
            output.set_pulse(self.pulse)
            self.pulse_cnt[self.pulse] += 1
        return self.outputs


class Button:
    def __init__(self, broadcaster):
        self.name = 'button'
        self.broadcaster = broadcaster
        self.pulse_cnt = {0: 0, 1: 0}

    def press(self):
        self.broadcaster.set_pulse(0)
        self.pulse_cnt[0] += 1
        return self.broadcaster


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    graph = {}
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            name, outputs = line.split(' -> ')
            if ', ' in outputs:
                outputs = outputs.split(', ')
            else:
                outputs = [outputs]

            if name == 'broadcaster':
                graph['broadcaster'] = Broadcaster(outputs)
            elif name.startswith('%'):
                name = name[1:]
                flipflop = FlipFlop(name, outputs)
                graph[name] = flipflop
            else:
                name = name[1:]
                conjunction = Conjunction(name, outputs)
                graph[name] = conjunction
        graph['button'] = Button(graph['broadcaster'])
    return graph


def part1(input_file: str) -> int:
    graph = read_input(input_file)
    btn = graph.get('button')


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
    #
    # assert solution_part1 == 323625
    # assert solution_part2 == 127447746739409


if __name__ == '__main__':
    test()
    main()
