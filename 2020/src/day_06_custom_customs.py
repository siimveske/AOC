import os


def readFile(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as file:
        lines = file.read()
        groups = lines.split("\n\n")

    return groups


def getAnyoneAnswers(groups):
    answers = []
    for group in groups:
        unique_answers = set()
        for line in group.split():
            unique_answers |= set(line)
        answers.append(unique_answers)

    return answers


def getEveryoneAnswers(groups):
    answers = []
    for group in groups:
        lines = group.split()
        unique_answers = set(lines[0])
        for i in range(1, len(lines)):
            unique_answers &= set(lines[i])
        answers.append(unique_answers)

    return answers


def getAnswerCount(answers):
    return sum([len(i) for i in answers])


def test():
    print("---- TEST ----")
    filepath = os.path.join('..', 'test', 'day_06_input.txt')
    groups = readFile(filepath)
    
    anyone_answers = getAnyoneAnswers(groups)
    anyone_answers_count = getAnswerCount(anyone_answers)
    print(f"Sum of counts part 1: { anyone_answers_count }")

    assert anyone_answers_count == 11

    everyone_answers = getEveryoneAnswers(groups)
    everyone_answers_count = getAnswerCount(everyone_answers)
    print(f"Sum of counts part 2: { everyone_answers_count }\n")

    assert everyone_answers_count == 6


def main():
    print("---- PROGRAM ----")
    filepath = os.path.join('..', 'data', 'day_06_input.txt')
    groups = readFile(filepath)

    anyone_answers = getAnyoneAnswers(groups)
    anyone_answers_count = getAnswerCount(anyone_answers)
    print(f"Sum of counts part 1: {anyone_answers_count}")

    everyone_answers = getEveryoneAnswers(groups)
    everyone_answers_count = getAnswerCount(everyone_answers)
    print(f"Sum of counts part 2: { everyone_answers_count }\n")


if __name__ == '__main__':
    test()
    main()
