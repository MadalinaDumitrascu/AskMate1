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


def read_data_base(filename):
    questions = []
<<<<<<< HEAD
    with open("D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv", "r") as file:
=======
    with open(filename, "r") as file:
>>>>>>> 4ef7480ff0b540fbe5c09c6d32d938b8a2b24fdb
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    for line in questions:
        line['submission_time'] = get_submission_time(line['submission_time'] )
    return questions


def select_by_id(filename, question_id):
    content = read_data_base(filename)
    question = []
    for line in content:
        if int(line['id']) == question_id:
            quest = line.get('title')
            question.append(quest)


def get_submission_time(elem):
    submit_time = util.converter(elem)
    return submit_time


# def read_data_answers(filename):
#     content = []
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             content.append(row)
#     return content


<<<<<<< HEAD
def get_answers(question_id):
    content = read_data_answers('D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv')
=======
def get_answers(filename, question_id):
    content = read_data_base(filename)
>>>>>>> 4ef7480ff0b540fbe5c09c6d32d938b8a2b24fdb
    answers = []
    for line in content:
        if int(line['question_id']) == question_id:
            answer = line.get('message')
            answers.append(answer)
    return answers

<<<<<<< HEAD
def get_message(question_id):
    filename= 'D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv'
=======

def get_message(filename, question_id):
>>>>>>> 4ef7480ff0b540fbe5c09c6d32d938b8a2b24fdb
    content= get_data(filename)
    messages = []
    for line in content:
        if int(line['id']) == question_id:
            mess = line.get('message')
            messages.append(mess)
    return messages


def generate_id_number(filename):
    content = get_data(filename)
    ids = []
    for line in content:
        for key, val in line.items():
            if key == 'id':
                ids.append(val)
    new_id = util.generate_id_number(ids)
    return new_id


def convert_new_line(headers, id_question, title, new_question):
    new_line = {}
    for elem in headers:
        new_line[elem] = ''
    new_line['id'] = id_question
    new_line['title'] = title
    new_line['message'] = new_question
    print(new_line)
    return new_line


def write_question(filename, headers, id_question, title, new_question):
    new_line = []
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_line)
    print(filename)
    return filename







