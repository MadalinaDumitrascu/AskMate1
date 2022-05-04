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


def select_by_id(filename, question_id):
    content = get_data(filename)
    question = []
    for line in content:
        if int(line['id']) == question_id:
            question.append(line)
    return question

# def read_data_answers(filename):
#     content = []
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             content.append(row)
#     return content


def get_answers(filename, question_id):
    content = get_data(filename)
    answers = []
    for line in content:
        if int(line['question_id']) == question_id:
            answer = line.get('message')
            answers.append(answer)
    return answers


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









