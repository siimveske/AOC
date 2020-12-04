import os
import re


def parseData(filename: str):
    
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    passport = {}
    passport_list = []
    
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                items = line.split()
                for item in items:
                    key, value = item.split(":")
                    passport[key.strip()] = value.strip()
            elif passport:
                passport_list.append(passport)
                passport = {}
        if passport:
            passport_list.append(passport)
            passport = {}
            
    return passport_list

def getValidPassportsPart1(passport_list: list[dict]):
    
    valid_passports = []
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for passport in passport_list:
        isvalid = True
        for field in expected_fields:
            if field not in passport.keys():
                isvalid = False
                break
        if isvalid:
            valid_passports.append(passport)
    
    return valid_passports

def getValidPassportsPart2(passport_list):
    
    valid_passports = []
    filtered_passports = getValidPassportsPart1(passport_list)
    
    for passport in filtered_passports:
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
        valid_passports.append(passport)
        
    return valid_passports

def isValidBirthYear(birth_year: str):
    '''
    Validate that birth_year is:
        1. four digits
        2. at least 1920 and at most 2002
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(birth_year)
    if result:
        result = int(result.string)
        return 1920 <= result <= 2002
    else:
        return False

def isValidIssueYear(issue_year: str):
    '''
    Validate that issue_year is:
        1. four digits
        2. at least 2010 and at most 2020
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(issue_year)
    if result:
        result = int(result.string)
        return 2010 <= result <= 2020
    else:
        return False
    
def isValidExpirationYear(expiration_year: str):
    '''
    Validate that expiration_year is:
        1. four digits
        2. at least 2020 and at most 2030
    '''
    p = re.compile('^[0-9]{4}$')
    result = p.match(expiration_year)
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

def isValidHairColor(hair_color: str):
    '''
    Validate that hair_color is:
        1. a # followed by exactly six characters 0-9 or a-f
    '''
    p = re.compile('^#[0-9abcdef]{6}$')
    result = p.match(hair_color)
    if result:
        return True
    else:
        return False

def isValidEyeColor(eye_color: str):
    '''
    Validate that eye_color is exactly
    one of: amb blu brn gry grn hzl oth
    '''
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return eye_color in valid_eye_colors

def isValidPassportID(passport_id: str):
    '''
    Validate that passport_id is
    nine-digit number, including leading zeroes
    '''
    p = re.compile('^[0-9]{9}$')
    result = p.match(passport_id)
    if result:
        return True
    else:
        return False

def main():
    print("---- PROGRAM PART 1 ----")
    passports = parseData('day_04_input.txt')
    count = len(getValidPassportsPart1(passports))
    print("Solution for Part 1: %s\n" % count)
    
    print("---- PROGRAM PART 2 ----")
    passports = parseData('day_04_input.txt')
    count = len(getValidPassportsPart2(passports))
    print("Solution for Part 2: %s\n" % count)

def test():
    print("---- TEST PART 1 ----")
    passports = parseData('day_04_test_input.txt')
    solution_part1 = len( getValidPassportsPart1(passports))
    print("Solution for Part 1: %s\n" % solution_part1)
    assert solution_part1 == 2

    print("---- TEST PART 2 ----")
    passports = parseData('day_04_test_input2.txt')
    solution_part2 = len(getValidPassportsPart2(passports))
    print("Solution for Part 2: %s\n" % solution_part2)
    assert solution_part2 == 4

          
if __name__ == '__main__':
    test()
    main()