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


def search(blueprint, time=24):
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

    best = 0     # Best number of geodes we are able to collect.
    visited = set()  # Visited states.

    # The "frontier" of our search, containing states to explore next.
    # In the initial state we only have 1 ore-mining robot.
    q = deque([(time, 0, 0, 0, 0, 1, 0, 0, 0, [])])
    ORE, CLAY, OBS, GEO = range(4)

    while q:
        tmp = q.pop()

        # This last list we added is not part of the state.
        state = tmp[:-1]
        if state in visited:
            continue

        visited.add(state)

        time, ore, clay, obs, geo, rore, rclay, robs, rgeo, did_not_build = tmp

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

        can_build = []
        # If we have enough materials for a geode-mining robot, we could also build that.
        if obs >= rgeo_cost_obs and ore >= rgeo_cost_ore:
            # Did we have the chance to build this robot type in the previous iteration
            # but decided to not build anything instead? If so, we just wasted precious
            # time, it's pointless to do it now that we are late, the result is inevitably
            # going to be worse.
            if GEO not in did_not_build:
                # Remember that we could have built a geode robot.
                can_build.append(GEO)
                # Pass along an empyy list, we built a robot so we don't have a list
                # of robots that we "could have built" but didn't.
                q.append((
                    time,
                    newore - rgeo_cost_ore,
                    newclay,
                    newobs - rgeo_cost_obs,
                    newgeo,
                    rore, rclay, robs, rgeo + 1, []
                ))

        # If we have enough materials for an obsidian-mining robot, we could also build that.
        # Avoid building more obsidian robots than the max obsidian per minute needed.
        if robs < max_obs_needed and clay >= robs_cost_clay and ore >= robs_cost_ore:
            if OBS not in did_not_build:
                can_build.append(OBS)
                q.append((
                    time,
                    newore - robs_cost_ore,
                    newclay - robs_cost_clay,
                    newobs,
                    newgeo,
                    rore, rclay, robs + 1, rgeo, []
                ))

        # If we have enough materials for a clay-mining robot, we could also build that.
        # Avoid building more clay robots than the max clay per minute needed.
        if rclay < max_clay_needed and ore >= rclay_cost:
            # Likewise.
            if CLAY not in did_not_build:
                can_build.append(CLAY)
                q.append((
                    time,
                    newore - rclay_cost,
                    newclay,
                    newobs,
                    newgeo,
                    rore, rclay + 1, robs, rgeo, []
                ))

        # If we have enough materials for an ore-mining robot, we could also build that.
        # Avoid building more ore robots than the max ore per minute needed.
        if rore < max_ore_needed and ore >= rore_cost:
            # Likewise.
            if ORE not in did_not_build:
                can_build.append(ORE)
                q.append((
                    time,
                    newore - rore_cost,
                    newclay,
                    newobs,
                    newgeo,
                    rore + 1, rclay, robs, rgeo, []
                ))

        # If we can also "wait" without building, pass along the list of robots
        # we couldhave built, but decided to not build instead.
        if (robs and obs < max_obs_needed) or (rclay and clay < max_clay_needed) or ore < max_ore_needed:
            # If so, we can also try just spending one minute only mining without building any robot.
            q.append((time, newore, newclay, newobs, newgeo, rore, rclay, robs, rgeo, can_build))

    return best


def part1(inputFile: str):
    blueprints = readInput(inputFile)
    total = 0
    for idx, *blueprint in blueprints:
        total += idx * search(blueprint)
    return total


def part2(inputFile: str):
    blueprints = readInput(inputFile)
    total = 1
    for _, *blueprint in blueprints[:3]:
        total *= search(blueprint, 32)
    return total


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    assert part1(filename) == 33
    print('Part 1 OK')

    assert part2(filename) == 3472
    print('Part 2 OK')


def main():
    print('\n---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')
    assert solution_part1 == 1382

    solution_part2 = part2(filename)
    print(f'Solution for Part 2: {solution_part2}\n')
    assert solution_part2 == 31740


if __name__ == '__main__':
    test()
    main()
