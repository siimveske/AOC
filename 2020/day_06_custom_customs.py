import os


def readFile(filename: str):
    script_location = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_location, filename)

    with open(input_file_path, 'r') as file:
        lines = file.read()
        groups = lines.split("\n\n")

    return groups


def getAnswers(groups):
    answers = []
    for group in groups:
        unique_answers = set()
        for line in group.split():
            unique_answers.update(set(line))
        answers.append(unique_answers)

    return answers


def getSumOfCounts(answers):
    return sum([len(i) for i in answers])


def test():
    print("---- TEST ----")
    groups = readFile('day_06_test_input.txt')
    answers = getAnswers(groups)
    sum_of_counts = getSumOfCounts(answers)
    print(f"Sum of counts: { sum_of_counts }\n")

    assert sum_of_counts == 11


def main():
    print("---- PROGRAM ----")
    groups = readFile('day_06_input.txt')
    answers = getAnswers(groups)
    sum_of_counts = getSumOfCounts(answers)
    print(f"Sum of counts: {sum_of_counts}")


if __name__ == '__main__':
    test()
    main()
