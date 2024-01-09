import os


class Hailstone:
    def __init__(self, pos: list[int], vel: list[int]) -> None:
        self.x_pos, self.y_pos, self.z_pos = pos
        self.x_velocity, self.y_velocity, self.z_velocity = vel

        # the a value of y=ax+b
        self.gradient = self.y_velocity / self.x_velocity

        # the b value of y=ax+b
        # y=ax+b -> b=y-ax
        self.y_intercept = self.y_pos - self.gradient * self.x_pos

    def __repr__(self) -> str:
        return f"({self.x_pos},{self.y_pos},{self.z_pos})@({self.x_velocity},{self.y_velocity},{self.z_velocity})"

    def intersects(self, other: "Hailstone"):
        """
        Line 1: y1=a1x+b1
        Line 2: y2=a2x+b2

        At intersection
        a1x+b1=a2x+b2
        a1x-a2x=b2-b1
        x(a1-a2)=b2-b1
        x=(b2-b1)/(a1-a2)
        """
        if self.gradient == other.gradient:
            raise ValueError("Parallel paths")

        x = (other.y_intercept - self.y_intercept) / (self.gradient - other.gradient)
        y = self.gradient * x + self.y_intercept
        return x, y

    def time_at_pos(self, current_pos: tuple[float, ...]) -> float:
        """
        Determine the time that this stone was at this position.
        t = (xi - x0) / vx
        where xi is the x coord at a given location
              x0 is the original x coord
              vx is the velocity in the x direction
        """

        return (current_pos[0] - self.x_pos) / self.x_velocity


def read_input(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    hailstones = []
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            pos, vel = line.split(" @ ")
            pos = list(map(int, pos.split(", ")))
            vel = list(map(int, vel.split(", ")))
            hailstones.append(Hailstone(pos, vel))

    return hailstones


def part1(input_file: str, range_min: int, range_max: int) -> int:
    stones = read_input(input_file)
    result = 0
    for i, this_stone in enumerate(stones):
        for that_stone in stones[:i]:
            try:
                intersection = this_stone.intersects(that_stone)
                this_time = this_stone.time_at_pos(intersection)
                that_time = that_stone.time_at_pos(intersection)
                x_inbounds = range_min <= intersection[0] <= range_max
                y_inbounds = range_min <= intersection[1] <= range_max
                time_in_future = this_time > 0 and that_time > 0
                if x_inbounds and y_inbounds and time_in_future:
                    result += 1
            except ValueError as e:
                print(f"Stone {this_stone} and {that_stone} move in parallel")
    return result


def part2(input_file: str) -> int:
    pass


def test():
    print("---- TEST ----")

    filename = "test_input.txt"

    assert part1(filename, 7, 27) == 2
    print("Part 1 OK")

    # assert part2(filename) == 154
    # print('Part 2 OK')


def main():
    print("\n---- MAIN ----")
    filename = "input.txt"

    solution_part1 = part1(filename, 200000000000000, 400000000000000)
    print(f"Solution for Part 1: {solution_part1}")

    # solution_part2 = part2(filename)
    # print(f"Solution for Part 2: {solution_part2}\n")

    assert solution_part1 == 26611
    # assert solution_part2 == 6654


if __name__ == "__main__":
    test()
    main()
