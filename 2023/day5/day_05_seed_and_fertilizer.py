import os
import re


def read_input(filename: str) -> list:
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    almanac = []
    p = re.compile(r'\d+')
    with open(input_file_path, 'r') as f:
        sections = f.read().split('\n\n')
        seeds = [int(number) for number in p.findall(sections[0])]
        almanac.append(seeds)

        seed_to_soil = [list(map(int, p.findall(line))) for line in sections[1].split('\n')[1:]]
        seed_to_soil.sort(key=lambda x: x[1])
        almanac.append(seed_to_soil)

        soil_to_fertilizer = [list(map(int, p.findall(line))) for line in sections[2].split('\n')[1:]]
        soil_to_fertilizer.sort(key=lambda x: x[1])
        almanac.append(soil_to_fertilizer)

        fertilizer_to_water = [list(map(int, p.findall(line))) for line in sections[3].split('\n')[1:]]
        fertilizer_to_water.sort(key=lambda x: x[1])
        almanac.append(fertilizer_to_water)

        water_to_light = [list(map(int, p.findall(line))) for line in sections[4].split('\n')[1:]]
        water_to_light.sort(key=lambda x: x[1])
        almanac.append(water_to_light)

        light_to_temperature = [list(map(int, p.findall(line))) for line in sections[5].split('\n')[1:]]
        light_to_temperature.sort(key=lambda x: x[1])
        almanac.append(light_to_temperature)

        temperature_to_humidity = [list(map(int, p.findall(line))) for line in sections[6].split('\n')[1:]]
        temperature_to_humidity.sort(key=lambda x: x[1])
        almanac.append(temperature_to_humidity)

        humidity_to_location = [list(map(int, p.findall(line))) for line in sections[7].split('\n')[1:]]
        humidity_to_location.sort(key=lambda x: x[1])
        almanac.append(humidity_to_location)

    return almanac


def part1(input_file: str) -> int:
    almanac = read_input(input_file)
    seeds = almanac[0]
    maps = almanac[1:]

    locations = []
    for seed in seeds:
        for m in maps:
            for row in m:
                dst, src, _len = row
                if src <= seed < (src + _len):
                    seed = dst + (seed - src)
                    break
        locations.append(seed)

    return min(locations)


def part2(input_file: str) -> int:
    pass


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 35
    print('Part 1 OK')

    # assert part2(filename) == 30
    # print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    #
    # assert solution_part1 == 23441
    # assert solution_part2 == 5923918


if __name__ == '__main__':
    test()
    main()
