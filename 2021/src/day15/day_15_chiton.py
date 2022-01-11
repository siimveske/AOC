import os
import heapq
from collections import defaultdict
from math import inf as INFINITY


def readInput(filename: str):

    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    risk_levels = []
    graph = defaultdict(list)

    with open(input_file_path, 'r') as f:
        for line in f:
            risk_levels.append([int(i) for i in line.strip()])

    width = len(risk_levels[0])
    height = len(risk_levels)

    for i in range(height):
        for j in range(width):
            neighbours = []
            # top
            if (i - 1) >= 0:
                neighbours.append((i - 1, j))
            # right
            if (j + 1) <= (width - 1):
                neighbours.append((i, j + 1))
            # bottom
            if (i + 1) <= (height - 1):
                neighbours.append((i + 1, j))
            # left
            if (j - 1) >= 0:
                neighbours.append((i, j - 1))

            for n in neighbours:
                row, col = n
                graph[i, j].append((n, risk_levels[row][col]))
                graph[row, col].append(((i, j), risk_levels[i][j]))

    return (graph, (height - 1, width - 1))


def dijkstra(grid, destination):
    '''Dijkstra's shortest path Algorithm
    web: https://github.com/mebeim/aoc/tree/master/2021#day-12---passage-pathing
    '''

    source = (0, 0)
    queue = [(0, source)]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)

        # If we got to the destination, we have our answer.
        if node == destination:
            return dist

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue

        # Mark the node as visited.
        visited.add(node)

        # For each unvisited neighbor of this node...
        for neighbor, neighbor_dist in grid[node]:
            if neighbor in visited:
                continue

            # Calculate the total distance from the source
            # to this neighbor passing through this node.
            newdist = dist + neighbor_dist

            # If the new distance is lower than the minimum distance we have to
            # reach this neighbor, then update its minimum distance and add it
            # to the queue, as we found a "better" path to it.
            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))

    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    return INFINITY


def part1(inputFile: str):
    graph, destination = readInput(inputFile)
    cost = dijkstra(graph, destination)
    return cost


def part2(inputFile: str):
    template, instructions = readInput(inputFile)
    return result


def test():
    print('---- TEST ----')
    filename = 'test_input.txt'

    solution_part1 = part1(filename)
    assert solution_part1 == 40
    print('Part 1 OK')

    #solution_part2 = part2(filename)
    #assert solution_part2 == 2188189693529
    #print('Part 2 OK')


def main():
    print('---- MAIN ----')
    filename = 'input.txt'

    solution_part1 = part1(filename)
    print(f'Solution for Part 1: {solution_part1}')

    #solution_part2 = part2(filename)
    #print(f'Solution for Part 2: {solution_part2}')


if __name__ == '__main__':
    test()
    main()
