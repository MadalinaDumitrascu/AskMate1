import csv
import os
import util

# QUESTIONS = os.environ['QUESTIONS']

def get_data(filename):
    content = []
    with open( filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append(row)
    return content

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


def read_data_answers(filename):
    content = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append(row)
    return content


def get_answers(question_id):
    content = read_data_answers('D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv')
    answers = []
    for line in content:
        print(line)
        if int(line['question_id']) == question_id:
            answ = line.get('message')
            answers.append(answ)
    return answers

def get_message(question_id):
    filename= 'D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv'
    content= get_data(filename)
    messages = []
    for line in content:
        if int(line['id']) == question_id:
            mess = line.get('message')
            print(mess)
            messages.append(mess)
    return messages
