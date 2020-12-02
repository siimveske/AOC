'''
Created on Dec 2, 2020

@author: siimv
'''
import os

class Password:
    def __init__(self, minLength: int, maxLength: int, letter: str, pwd: str):
        self.minLength = minLength
        self.maxLength = maxLength
        self.letter    = letter
        self.pwd       = pwd
    
    def isValid(self):
        letterCount = self.pwd.count(self.letter)
        return letterCount >= self.minLength and letterCount <= self.maxLength
    
def getValidCount(passwordList: [Password]):
    count = 0
    for password in passwordList:
        if password.isValid():
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
            # parse line "1-3 a: abcde" into components:
            # min:1
            # max:3
            # letter:a
            # pwd: abcde
            components = line.split()
            minLength, maxLength = components[0].split('-')
            letter = components[1][0]
            pwd = components[2]
            item = Password(int(minLength), int(maxLength), letter, pwd)
            data.append(item)
        
        f.close()
    
    return data

def test():
    filename = 'day_02_test_input.txt'
    passwordList = parseData(filename)
    count = getValidCount(passwordList)
    assert count == 2

def main():
    filename = 'day_02_input.txt'
    passwordList = parseData(filename)
    count = getValidCount(passwordList)
    print("Valid password count: %s" % count)
    
    
if __name__ == '__main__':
    test()
    main()

    