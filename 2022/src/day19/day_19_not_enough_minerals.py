from collections import deque
import os
import re

'''https://github.com/mebeim/aoc/tree/master/2022#day-19---not-enough-minerals'''


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    pattern = re.compile(r'\d+')
    blueprints = []
    with open(input_file_path, 'r') as f:
        for line in f:
            blueprints.append(tuple(map(int, pattern.findall(line))))
    return blueprints


def best_case_scenario(initial_amount, robots, t):
    return initial_amount + robots * (t + 1) + t * (t + 1) // 2


def search(blueprint):
    (rore_cost,      # Cost in ore to build an ore-mining robot.
     rclay_cost,     # Cost in ore to build a clay-mining robot.
     robs_cost_ore,  # Cost in ore to build an obsidian-mining robot.
     robs_cost_clay,  # Cost in clay to build an obsidian-mining robot.
     rgeo_cost_ore,  # Cost in ore to build a geode-mining robot.
     rgeo_cost_obs   # Cost in obsidian to build a geode-mining robot.
     ) = blueprint

    max_ore_needed = max(rore_cost, rclay_cost, robs_cost_ore, rgeo_cost_ore)
    max_clay_needed = robs_cost_clay
    max_obs_needed = rgeo_cost_obs

    time = 24
    best = 0     # Best number of geodes we are able to collect.
    visited = set()  # Visited states.

    # The "frontier" of our search, containing states to explore next.
    # In the initial state we only have 1 ore-mining robot.
    q = deque([(time, 0, 0, 0, 0, 1, 0, 0, 0)])

    while q:
        time, ore, clay, obs, geo, rore, rclay, robs, rgeo = state = q.pop()
        if state in visited:
            continue

        visited.add(state)

        # Each robot we have mines 1 resource of its type, taking 1 minute.
        newore = ore + rore
        newclay = clay + rclay
        newobs = obs + robs
        newgeo = geo + rgeo
        time -= 1

        # If we run out of time, we reached a "goal" state. Update the best
        # number of geodes we were able to mine.
        if time == 0:
            best = max(best, newgeo)
            continue

        # If we can't mine more geodes in the best-case scenario, bail out.
        if best_case_scenario(newgeo, rgeo, time) < best:
            continue

        # If we can't mine enough obsidian to build new geode robots even in the
        # best-case scenario, we already know how many geodes we'll be able to get.
        if best_case_scenario(newobs, robs, time) < rgeo_cost_obs:
            best = max(best, newgeo + rgeo * time)
            continue

        # Likewise for ore.
        if best_case_scenario(newore, rore, time) < rgeo_cost_ore:
            best = max(best, newgeo + rgeo * time)
            continue

        # Following are the possible actions (transitions) to take...

        # Does it make sense to wait for a resource? I.E. do I have less than
        # the max needed and do I also have robots to produce it?
        if (robs and obs < max_obs_needed) or (rclay and clay < max_clay_needed) or ore < max_ore_needed:
            # If so, we can also try just spending one minute only mining without building any robot.
            q.append((time, newore, newclay, newobs, newgeo, rore, rclay, robs, rgeo))

        # If we have enough materials for a geode-mining robot, we could also build that.
        if obs >= rgeo_cost_obs and ore >= rgeo_cost_ore:
            q.append((
                time,
                newore - rgeo_cost_ore,
                newclay,
                newobs - rgeo_cost_obs,
                newgeo,
                rore, rclay, robs, rgeo + 1
            ))

        # If we have enough materials for an obsidian-mining robot, we could also build that.
        if clay >= robs_cost_clay and ore >= robs_cost_ore:
            # Avoid building more obsidian robots than the max obsidian per minute needed.
            if obs < max_obs_needed:
                q.append((
                    time,
                    newore - robs_cost_ore,
                    newclay - robs_cost_clay,
                    newobs,
                    newgeo,
                    rore, rclay, robs + 1, rgeo
                ))

        # If we have enough materials for a clay-mining robot, we could also build that.
        if ore >= rclay_cost:
            # Avoid building more clay robots than the max clay per minute needed.
            if rclay < max_clay_needed:
                q.append((
                    time,
                    newore - rclay_cost,
                    newclay,
                    newobs,
                    newgeo,
                    rore, rclay + 1, robs, rgeo
                ))

        # If we have enough materials for an ore-mining robot, we could also build that.
        if ore >= rore_cost:
            # Avoid building more ore robots than the max ore per minute needed.
            if rore < max_ore_needed:
                q.append((
                    time,
                    newore - rore_cost,
                    newclay,
                    newobs,
                    newgeo,
                    rore + 1, rclay, robs, rgeo
                ))

    return best


def part1(inputFile: str):
    blueprints = readInput(inputFile)
    result = 0
    for blueprint in blueprints:
        idx = blueprint[0]
        data = blueprint[1:]
        best = search(data)
        result += (idx * best)
    return result


def part2(inputFile: str):
    cubes = readInput(inputFile)


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 33
    print('Part 1 OK')

    # assert part2(filename) == 58
    # print('Part 2 OK\n')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 1382

    # solution_part2 = part2(filename)
    # print(f'Solution for Part 2: {solution_part2}\n')
    # assert solution_part1 == 2610


if __name__ == '__main__':
    test()
    main()
