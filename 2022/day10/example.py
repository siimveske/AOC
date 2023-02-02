"""Solution to AoC 2022 Day 10 - Cathode-Ray Tube
https://github.com/djotaku/adventofcode/blob/47519fe2505d9ffe67d9a92895394224808be524/2022/Day_10/Python/solution.py
"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as f:
        return [line.rstrip() for line in f.readlines()]


def program_execution(assembly: list):
    """Take in list of assembly code and return list of signal strengths."""
    signal_strengths = []
    register_x = 1
    cycle = 1
    sprite = 0
    message = []
    checkpoints = [20, 60, 100, 140, 180, 220]
    for code in assembly:
        cycle += 1
        sprite = sprite_location(sprite)
        message.append(draw_sprite(sprite, register_x))
        if code.startswith("addx"):
            if cycle in checkpoints:
                signal_strengths.append(register_x * cycle)
            command = code.split()
            register_x += int(command[1])
            cycle += 1
            sprite = sprite_location(sprite)
            message.append(draw_sprite(sprite, register_x))
        if cycle in checkpoints:
            signal_strengths.append(register_x * cycle)

    return signal_strengths, message


def sprite_location(sprite: int) -> int:
    """Figure out next location for the sprite"""
    sprite += 1
    return sprite % 40


def draw_sprite(sprite: int, register_x: int) -> str:
    """Determine whether to draw a . or #"""
    if register_x == (sprite - 1) or register_x == sprite or register_x == (sprite + 1):
        return '▓'
    else:
        return '░'


if __name__ == "__main__":
    code_to_execute = input_per_line("input.txt")
    executed_signal_strengths, this_message = program_execution(code_to_execute)
    print(f"{this_message=}")
    print(f"Sum of the signal strengths is {sum(executed_signal_strengths)}")
    print("Message is:")
    print(this_message[0], end="")
    for index, character in enumerate(this_message, start=1):
        if index % 40 == 0:
            print()
        print(character, end="")
