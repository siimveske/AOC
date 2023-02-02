#!/usr/bin/env python
'''
https://adventofcode.com/2022/day/17
https://github.com/terminalmage/adventofcode/blob/main/2022/day17.py

--- Day 17: Pyroclastic Flow ---

Your handheld device has located an alternative exit from the cave for you and
the elephants. The ground is rumbling almost continuously now, but the strange
valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large,
oddly-shaped rocks are falling into the chamber from above, presumably due to
all the rumbling. If you can't work out where the rocks will fall next, you
might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and
. is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

The rocks fall in the order shown above: first the - shape, then the + shape,
and so on. Once the end of the list is reached, the same order repeats: the -
shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming
out of the walls themselves. A quick scan reveals the effect the jets of hot
gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

In jet patterns, < means a push to the left, while > means a push to the right.
The pattern above means that the jets will push a falling rock right, then
right, then right, then left, then left, then right, and so on. If the end of
the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so
that its left edge is two units away from the left wall and its bottom edge is
three units above the highest rock in the room (or the floor, if there isn't
one).

After a rock appears, it alternates between being pushed by a jet of hot gas
one unit (in the direction indicated by the next symbol in the jet pattern) and
then falling one unit down. If any movement would cause any part of the rock to
move into the walls, floor, or a stopped rock, the movement instead does not
occur. If a downward movement would have caused a falling rock to move into the
floor or an already-fallen rock, the falling rock stops where it is (having
landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the
example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

To prove to the elephants your simulation is accurate, they want to know how
tall the tower will get after 2022 rocks have stopped (but before the 2023rd
rock begins falling). In this example, the tower of rocks will be 3068 units
tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped
falling?

--- Part Two ---

The elephants are not impressed by your simulation. They demand to know how
tall the tower will be after 1000000000000 rocks have stopped! Only then will
they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

How tall will the tower be after 1000000000000 rocks have stopped?
'''
import itertools
import sys

# Typing shortcuts
Coordinate = tuple[int, int]
Rock = set[Coordinate]


class AOC2022Day17():
    '''
    Day 17 of Advent of Code 2022
    '''
    day = 17
    width = 7

    def __init__(self) -> None:
        '''
        Load the jet pattern and define the rock sequence. The reset_chamber()
        function will create new itertools.cycle instances for both, which
        allow them to be repeated in a loop for as long as we need.
        '''

        # Translate the jet pattern into a sequence of left/right. This way we
        # only need to translate once, and not repeat this several times for
        # each rock that is dropped.
        jet_map = {'<': 'left', '>': 'right'}

        self.__jet_pattern = tuple(
            jet_map[item] for item in open('input.txt').read().rstrip()
        )

        # Define the sequence of rocks as a sequence of lambdas, to which the
        # current top row number is passed. Each of the lambdas will return a
        # Rock.
        #
        # A Rock is defined as a set of coordinates. This is what enables
        # collision detection: if the Rock's set of coordinates intersect with
        # that of the chamber's, then the rock has hit another Rock (or the
        # floor).
        #
        # Each Rock's left side will start in the third column (i.e. column
        # index 2).
        self.__rock_sequence = (
            #
            #  @@@@
            #
            lambda: {
                (2, self.top + 4), (3, self.top + 4), (4, self.top + 4), (5, self.top + 4),
            },
            #
            #  .@.
            #  @@@
            #  .@.
            #
            lambda: {
                (3, self.top + 6),
                (2, self.top + 5), (3, self.top + 5), (4, self.top + 5),
                (3, self.top + 4),
            },
            #
            #  ..@
            #  ..@
            #  @@@
            #
            lambda: {
                (4, self.top + 6),
                (4, self.top + 5),
                (2, self.top + 4), (3, self.top + 4), (4, self.top + 4),
            },
            #
            #  @
            #  @
            #  @
            #  @
            #
            lambda: {
                (2, self.top + 7),
                (2, self.top + 6),
                (2, self.top + 5),
                (2, self.top + 4),
            },
            #
            #  @@
            #  @@
            #
            lambda: {
                (2, self.top + 5), (3, self.top + 5),
                (2, self.top + 4), (3, self.top + 4),
            },
        )

        self.chamber = set()
        self.top = 0

    def move_down(self, rock: Rock) -> Rock:
        '''
        Move the Rock down by one row. If the new position intersects with the
        chamber, then the rock has collided, and no movement will take place
        (i.e. the original Rock will be returned back). If the movement is
        successful, a new Rock representing the updated coordinates will be
        returned.
        '''
        new_rock = {(col, row - 1) for col, row in rock}
        return rock if new_rock & self.chamber else new_rock

    def move_left(self, rock: Rock) -> Rock:
        '''
        Move the Rock to the left by one column. If the leftmost column is
        already 0, then the rock has been blown into the wall. If the new
        position of the Rock intersects with the chamber, then the Rock has
        been blown into another Rock. In both cases, no movement will take
        place (i.e. the original Rock will be returned back). If the movement
        is successful, a new Rock representing the updated coordinates will be
        returned.
        '''
        new_rock = {(col - 1, row) for col, row in rock}
        if any(coord[0] < 0 for coord in new_rock) or new_rock & self.chamber:
            # Rock was already against the wall or adjacent to another rock
            return rock
        return new_rock

    def move_right(self, rock: Rock) -> Rock:
        '''
        Move the Rock to the right by one column. If the rightmost column is
        already self.width, then the rock has been blown into the wall. If the new
        position of the Rock intersects with the chamber, then the Rock has
        been blown into another Rock. In both cases, no movement will take
        place (i.e. the original Rock will be returned back). If the movement
        is successful, a new Rock representing the updated coordinates will be
        returned.
        '''
        new_rock = {(col + 1, row) for col, row in rock}
        if any(coord[0] >= self.width for coord in new_rock) or new_rock & self.chamber:
            # Rock was already against the wall or adjacent to another rock
            return rock
        return new_rock

    def reset_chamber(self) -> None:
        '''
        Reset to an empty chamber. An empty chamber is represented by a set of
        coordinates covering all columns at row 0. This gives us something for
        the Rocks to collide with, and as a nice side benefit means that the
        height of the tower is the same as the max y-index of all the
        coordinates in the chamber.
        '''
        self.chamber.clear()
        self.chamber.update((col, 0) for col in range(self.width))
        self.top = 0
        # pylint: disable=attribute-defined-outside-init
        self.jet_pattern = itertools.cycle(enumerate(self.__jet_pattern))
        self.rock_sequence = itertools.cycle(enumerate(self.__rock_sequence))
        # pylint: enable=attribute-defined-outside-init

    def print_chamber(self) -> None:
        '''
        Print the current state of the chamber to stdout
        '''
        # Write the rows from the top down
        for row in range(self.top, 0, -1):
            sys.stdout.write('|')
            for col in range(self.width):
                sys.stdout.write('#' if (col, row) in self.chamber else '.')
            sys.stdout.write('|\n')

        # Write bottom border
        sys.stdout.write(f'+{"-" * self.width}+\n')
        sys.stdout.flush()

    def cavetris(self, num_rocks: int) -> int:
        '''
        Calculate chamber height after a specific number of rocks are dropped
        '''
        # Empty the chamber in case a simulation has already been run
        self.reset_chamber()

        tracked = {}

        for rock_num in range(num_rocks):
            rock_index, rock_gen = next(self.rock_sequence)
            rock = rock_gen()
            while True:
                jet_index, direction = next(self.jet_pattern)
                if rock_num > 1000:
                    # Perform cycle detection. For each rock, track the
                    # chamber's height for the current combination of
                    # rock_index and jet_index. When we encounter a combination
                    # we've seen before, calculate the difference between the
                    # current rock_num and the rock_num the first time this
                    # combination was encountered. This difference will be the
                    # proposed cycle period. If the current rock_num and the
                    # total number of rocks both share the same remainder when
                    # divided by the proposed period, then we know that we've
                    # detected a cycle. A cycle which, importantly, we know
                    # ends with the very last rock. With this knowledge, we can
                    # compute the eventual height by adding a multiple of the
                    # amount of remaining cycle iterations and the amount the
                    # chamber's height increases each cycle.
                    key = (rock_index, jet_index)
                    if key in tracked:
                        prev_rock_num, elevation = tracked[key]
                        period = rock_num - prev_rock_num
                        if rock_num % period == num_rocks % period:
                            print(
                                f'Cycle of period {period} detected '
                                f'(iterations {prev_rock_num} - {rock_num})'
                            )
                            cycle_height = self.top - elevation
                            rocks_remaining = num_rocks - rock_num
                            cycles_remaining = (rocks_remaining // period) + 1
                            return elevation + (cycle_height * cycles_remaining)
                    else:
                        tracked[key] = (rock_num, self.top)

                # Blow the rock to the right or left
                rock = getattr(self, f'move_{direction}')(rock)
                # Attempt to drop
                new_position = self.move_down(rock)
                if new_position == rock:
                    # Rock has stopped dropping, merge it with the chamber's
                    # set of coordinates.
                    self.chamber.update(rock)
                    # Calculate new top of tower
                    self.top = max(self.top, max(coord[1] for coord in rock))
                    # Nothing left to do for this rock, exit the loop
                    break

                # Update the position of the rock
                rock = new_position

        # Return the current height of the tower
        return self.top

    def part1(self) -> int:
        '''
        Calculate height of rock tower after 2022 rocks have dropped
        '''
        return self.cavetris(2022)

    def part2(self) -> int:
        '''
        Calculate height of rock tower after one trillion rocks have dropped
        '''
        return self.cavetris(1_000_000_000_000)


if __name__ == '__main__':
    # Run against test data
    aoc = AOC2022Day17()
    print("Part1: ", aoc.part1())
    print("Part2: ", aoc.part2())
