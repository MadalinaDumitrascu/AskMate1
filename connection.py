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


    with open(filename, "r") as file:

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



def get_answers(question_id):
    content = read_data_answers('D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv')

def get_answers(filename, question_id):
    content = read_data_base(filename)

    answers = []
    for line in content:
        if int(line['question_id']) == question_id:
            answer = line.get('message')
            answers.append(answer)
    return answers


def get_message(question_id):
    filename= 'D:\\Programare\\Proiecte GitHub\\Web and SQL\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv'


def get_message(filename, question_id):

    content= get_data(filename)
    messages = []
    for line in content:
        if int(line['id']) == question_id:
            mess = line.get('message')
            messages.append(mess)
    return messages


def generate_id_number(filename):
    data = get_data(filename)
    if not len(data):
        return 1
    id_list = max([int(el.get("id")) for el in data])
    return id_list + 1


def convert_new_line(headers, id_question, title, new_question):
    new_line = {}
    for elem in headers:
        new_line[elem] = ''
    new_line['id'] = id_question
    new_line['title'] = title
    new_line['message'] = new_question
    print(new_line)
    return new_line


def write_question(filename, headers, data):
    with open(filename, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(data)
    print(filename)
    return filename









