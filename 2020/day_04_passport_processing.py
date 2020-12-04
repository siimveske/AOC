import os


class Version:
    part1 = 1
    part2 = 2

def parseData(filename: str):
    
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    data = []
    passport = {}
    
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                items = line.split()
                for item in items:
                    key, value = item.split(":")
                    passport[key.strip()] = value.strip()
            else:
                data.append(passport)
                passport = {}
        if passport:
            data.append(passport)
            passport = {}
            
    return data

def getValidPassportCount(passportList):
    
    count = 0
    expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for passport in passportList:
        isvalid = True
        for field in expectedFields:
            if field not in passport.keys():
                isvalid = False
                break
        if isvalid:
            count += 1
    
    return count

              
def main():
    print("---- PROGRAM PART 1 ----")
    passportList = parseData('day_04_input.txt')
    count = getValidPassportCount(passportList)
    print("Solution for Part 1: %s\n" % count)

def test():
    print("---- TEST PART 1 ----")
    passportList = parseData('day_04_test_input.txt')
    count = getValidPassportCount(passportList)
    print("Solution for Part 1: %s\n" % count)
    assert count == 2

            
if __name__ == '__main__':
    test()
    main()