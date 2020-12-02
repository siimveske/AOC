import os


class ValidatorVersion():
    part1 = 1
    part2 = 2
    
class Password:
    def __init__(self, start: int, stop: int, letter: str, pwd: str):
        self.start  = start
        self.stop   = stop
        self.letter = letter
        self.pwd    = pwd
    
    def isValid(self, version: ValidatorVersion):
        if version is ValidatorVersion.part1:
            letterCount = self.pwd.count(self.letter)
            return letterCount >= self.start and letterCount <= self.stop
        elif version is ValidatorVersion.part2:
            A = self.pwd[self.start-1] == self.letter
            B = self.pwd[self.stop-1] == self.letter
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
    '''Parse line such as "1-3 a: abcde" into Password components
        # start:1
        # stop:3
        # letter:a
        # pwd:abcde
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

    