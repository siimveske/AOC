'''
Created on Dec 2, 2020

@author: siimv
'''
import os


class ValidatorVersion():
    part1 = 1
    part2 = 2
    
class Password:
    def __init__(self, minLength: int, maxLength: int, letter: str, pwd: str):
        self.minLength = minLength
        self.maxLength = maxLength
        self.letter    = letter
        self.pwd       = pwd
    
    def isValid(self, version: ValidatorVersion):
        if version is ValidatorVersion.part1:
            letterCount = self.pwd.count(self.letter)
            return letterCount >= self.minLength and letterCount <= self.maxLength
        elif version is ValidatorVersion.part2:
            A = self.pwd[self.minLength-1] == self.letter
            B = self.pwd[self.maxLength-1] == self.letter
            return (A and not B) or (B and not A)
        else:
            raise Exception("Invalid validator version")
    
def getValidCount(passwordList: [Password], version: ValidatorVersion):
    count = 0
    for password in passwordList:
        if password.isValid(version):
            count += 1
    return count

def parseData(filename: str):
    '''Parse line such as "1-3 a: abcde" into components
        # min:1
        # max:3
        # letter:a
        # pwd:abcde
        and store the result as Password object
        @Returns List[Password]
    '''
    data = []
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)
    
    with open(input_file_path, 'r') as f:
        for line in f:
            components = line.split()
            minLength, maxLength = components[0].split('-')
            letter = components[1][0]
            pwd = components[2]
            data.append(Password(int(minLength), int(maxLength), letter, pwd))
        f.close()
    
    return data

def test():
    filename = 'day_02_test_input.txt'
    
    passwordList = parseData(filename)
    v1 = getValidCount(passwordList, ValidatorVersion.part1)
    v2 = getValidCount(passwordList, ValidatorVersion.part2)
    
    assert v1 == 2
    assert v2 == 1

def main():
    filename = 'day_02_input.txt'
    
    passwordList = parseData(filename)
    count1 = getValidCount(passwordList, ValidatorVersion.part1)
    count2 = getValidCount(passwordList, ValidatorVersion.part2)
    
    print("Valid password count for part 1: %s" % count1)
    print("Valid password count for part 2: %s" % count2)
    
    
if __name__ == '__main__':
    test()
    main()

    