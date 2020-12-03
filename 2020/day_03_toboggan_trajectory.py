import os


class Version:
    part1 = 1
    part2 = 2
   
def parseData(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    data = []
    with open(input_file_path, 'r') as file:
        for line in file:
            data.append(line.strip())
    
    return data

def solve(data: list[str], version: Version):
      
    if version is Version.part1:
        return getTreeCount(data, deltaX=3, deltaY=1)
    elif version is Version.part2:
        product = 1
        routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        
        for deltaX, deltaY in routes:
            product *= getTreeCount(data, deltaX, deltaY)
            
        return product
    else:
        raise Exception('Invalid version!')
    
def getTreeCount(data: list[str], deltaX: int, deltaY: int):
    
    x = 0
    y = 0
    treeCount = 0
    segmentWidth = len(data[0])
    mapHeight = len(data) - 1
    
    while y < mapHeight:
        x = (x + deltaX) % segmentWidth
        y += deltaY
        if y <= mapHeight and data[y][x] == '#':
            treeCount += 1
            
    print("Tree count for route (%s %s) == %s" % (deltaX, deltaY, treeCount))
    return treeCount
    
def test():
    print("---- TEST PART 1 ----")
    data = parseData('day_03_test_input.txt')
    solution_part1 = solve(data, Version.part1)
    print("Solution for Part 1: %s\n" % solution_part1)
    assert solution_part1 == 7
    
    print("---- TEST PART 2 ----")
    solution_part2 = solve(data, Version.part2)
    print("Solution for Part 2: %s\n" % solution_part2)
    assert solution_part2 == 336

def main():
    print("---- PROGRAM PART 1 ----")
    data = parseData('day_03_input.txt')
    solution_part1 = solve(data, Version.part1)
    print("Solution for Part 1: %s\n" % solution_part1)
          
    print("---- PROGRAM PART 2 ----")
    solution_part2 = solve(data, Version.part2)
    print("Solution for Part 2: %s" % solution_part2)
    
    
if __name__ == '__main__':
    test()
    main()
