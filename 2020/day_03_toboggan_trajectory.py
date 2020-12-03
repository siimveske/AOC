import os


class Version:
    part1 = 1
    part2 = 2
   
def parseData(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    fData = []
    with open(input_file_path, 'r') as file:
        for line in file:
            fData.append(line.strip())
    
    return fData

def solve(data: list[str], version: Version):
    if version is Version.part1:
        segmentWitdth = len(data[0])
        mapHeight = len(data) - 1
        x = 0
        y = 0
        treeCount = 0
        
        while y < mapHeight:
            x = (x + 3) % segmentWitdth
            y += 1
            print("X: %3s Y:%3s" % (x, y), end='')
            if y <= mapHeight and data[y][x] == '#':
                print('   #', end='')
                treeCount += 1
            print()
        
        return treeCount
    elif version is Version.part2:
        pass
    else:
        raise Exception('Invalid version!')
    
def test():
    print("---- TEST ----")
    
    data = parseData('day_03_test_input.txt')
    solution_part1 = solve(data, Version.part1)
    assert solution_part1 == 7
    
    print("---- END ----")

def main():
    print("---- PROGRAM ----")
    
    data = parseData('day_03_input.txt')
    solution_part1 = solve(data, Version.part1)
    
    print("---- END ----")
    print("Solution Part 1: %s" % solution_part1)
    
    
if __name__ == '__main__':
    test()
    main()
