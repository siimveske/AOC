import os
import re


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
            elif passport:
                data.append(passport)
                passport = {}
        if passport:
            data.append(passport)
            passport = {}
            
    return data

def getValidPassportsPart1(passportList):
    
    validPassports = []
    expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for passport in passportList:
        isvalid = True
        for field in expectedFields:
            if field not in passport.keys():
                isvalid = False
                break
        if isvalid:
            validPassports.append(passport)
    
    return validPassports

def getValidPassportsPart2(passportList):
    
    validPassports = []
    filteredPassports = getValidPassportsPart1(passportList)
    
    for passport in filteredPassports:
        if not isValidBirthYear(passport.get('byr')):
            continue
        if not isValidIssueYear(passport.get('iyr')):
            continue
        if not isValidExpirationYear(passport.get('eyr')):
            continue
        if not isValidHeight(passport.get('hgt')):
            continue
        if not isValidHairColor(passport.get('hcl')):
            continue
        if not isValidEyeColor(passport.get('ecl')):
            continue
        if not isValidPassportID(passport.get('pid')):
            continue
        validPassports.append(passport)
        
    return validPassports

def isValidBirthYear(birthYear: str):
    '''
    Validate that birthYear is:
        1. four digits
        2. at least 1920 and at most 2002
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(birthYear)
    if result:
        result = int(result.string)
        return 1920 <= result <= 2002
    else:
        return False

def isValidIssueYear(issueYear: str):
    '''
    Validate that issueYear is:
        1. four digits
        2. at least 2010 and at most 2020
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(issueYear)
    if result:
        result = int(result.string)
        return 2010 <= result <= 2020
    else:
        return False
    
def isValidExpirationYear(expirationYear: str):
    '''
    Validate that expirationYear is:
        1. four digits
        2. at least 2020 and at most 2030
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(expirationYear)
    if result:
        result = int(result.string)
        return 2020 <= result <= 2030
    else:
        return False

def isValidHeight(height: str):
    '''
    Validate that height is:
        1. a number followed by either cm or in
        2. If cm, the number must be at least 150 and at most 193
        3. If in, the number must be at least 59 and at most 76.
    '''
    p = re.compile('^([0-9]{2,3}(cm|in))$')
    result = p.match(height)
    if result:
        if 'cm' in result.string:
            result = int(result.string.replace('cm', ''))
            return 150 <= result <= 193
        else:
            result = int(result.string.replace('in', ''))
            return 59 <= result <= 76
    else:
        return False

def isValidHairColor(hairColor: str):
    '''
    Validate that hairColor is:
        1. a # followed by exactly six characters 0-9 or a-f
    '''
    p = re.compile('^#[0-9abcdef]{6}$')
    result = p.match(hairColor)
    if result:
        return True
    else:
        return False

def isValidEyeColor(eyeColor: str):
    '''
    Validate that eyeColor is exactly
    one of: amb blu brn gry grn hzl oth
    '''
    validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return eyeColor in validEyeColors

def isValidPassportID(passportID: str):
    '''
    Validate that passportID is
    nine-digit number, including leading zeroes
    '''
    p = re.compile('^[0-9]{9}$')
    result = p.match(passportID)
    if result:
        return True
    else:
        return False

def main():
    print("---- PROGRAM PART 1 ----")
    passportList = parseData('day_04_input.txt')
    count = len(getValidPassportsPart1(passportList))
    print("Solution for Part 1: %s\n" % count)
    
    print("---- PROGRAM PART 2 ----")
    passportList = parseData('day_04_input.txt')
    count = len(getValidPassportsPart2(passportList))
    print("Solution for Part 2: %s\n" % count)

def test():
    print("---- TEST PART 1 ----")
    passportList = parseData('day_04_test_input.txt')
    filteredPassports = getValidPassportsPart1(passportList)
    part1Solution = len(filteredPassports)
    print("Solution for Part 1: %s\n" % part1Solution)
    assert part1Solution == 2

    print("---- TEST PART 2 ----")
    passportList = parseData('day_04_test_input2.txt')
    validPassports = getValidPassportsPart2(passportList)
    part2Solution = len(validPassports)
    print("Solution for Part 2: %s\n" % part2Solution)
    assert part2Solution == 4

          
if __name__ == '__main__':
    test()
    main()