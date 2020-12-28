import os


def readFile(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as file:
        lines = file.read()
        groups = lines.split('\n\n')

    return groups


def getAnswers(groups):
    answers = []
    for group in groups:
        all_answers = ''.join(group.split())
        answers.append(set(all_answers))

    return answers


def getSharedAnswers(groups):
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
    print('---- TEST ----')
    filepath = os.path.join('..', 'test', 'day_06_input.txt')
    groups = readFile(filepath)

    answers = getAnswers(groups)
    answer_count = getAnswerCount(answers)
    print(f'Sum of counts part 1: { answer_count }')

    assert answer_count == 11

    shared_answers = getSharedAnswers(groups)
    shared_answer_count = getAnswerCount(shared_answers)
    print(f'Sum of counts part 2: { shared_answer_count }\n')

    assert shared_answer_count == 6


def main():
    print('---- PROGRAM ----')
    filepath = os.path.join('..', 'data', 'day_06_input.txt')
    groups = readFile(filepath)

    answers = getAnswers(groups)
    answer_count = getAnswerCount(answers)
    print(f'Sum of counts part 1: {answer_count}')

    shared_answers = getSharedAnswers(groups)
    shared_answer_count = getAnswerCount(shared_answers)
    print(f'Sum of counts part 2: { shared_answer_count }\n')


if __name__ == '__main__':
    test()
    main()
