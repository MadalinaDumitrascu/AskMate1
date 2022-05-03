import connection
import util


def get_data_base():
    content = connection.read_data_base()
    return content

def get_one_question(question_id):
    content = get_data_base()
    question =[]
    for line in content:
        if int(line['id']) == question_id:
            quest = line.get('title')
            question.append(quest)
    return question

def get_message(question_id):
    message = connection.get_message(question_id)
    return message

def get_answers(question_id):
    answers = connection.get_answers(question_id)
    return answers

def generate_id_number():
    id = connection.generate_id_number()
    return id

def write_data_base(id_question, title, new_question):
    new_entry = connection.write_data_base(id_question, title, new_question)


