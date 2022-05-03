import csv
import os
import util

# QUESTIONS = os.environ['QUESTIONS']


def read_data_base():
    questions = []
    with open("C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    for line in questions:
        line['submission_time'] = get_submission_time(line['submission_time'] )

    return questions


def get_submission_time(elem):
    submit_time = util.converter(elem)
    return submit_time


def read_data_answers(filename):
    content = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append(row)
    return content


def get_answers(question_id):
    content = read_data_answers('C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv')
    answers = []
    for line in content:
        if int(line['id']) == question_id:
            answ = line.get('message')
            answers.append(answ)
    return answers

