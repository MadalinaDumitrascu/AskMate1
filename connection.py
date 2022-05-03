import csv
import os
import util

# QUESTIONS = os.environ['QUESTIONS']


def read_data_base():
    questions = []
    with open("D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    for line in questions:
        line['submission_time'] = get_submission_time(line['submission_time'] )

    return questions


def get_submission_time(elem):
    submit_time = util.converter(elem)
    return submit_time

