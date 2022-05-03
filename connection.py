import csv
import os
import util

QUESTIONS = os.environ['QUESTIONS']


def read_data_base():
    questions = []
    with open(QUESTIONS, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    result = []
    for line in questions:
        new_line = []
        for elem in line:
            new_line.append(elem)
            if elem == elem[1]:
                new_line.append(get_submission_time(int(elem[1])))
                result.append(new_line)
    return questions


def get_submission_time(elem):
    submit_time = util.converter(elem)
    return submit_time

