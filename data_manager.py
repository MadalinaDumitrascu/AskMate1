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


def get_answers(question_id):
    answers = connection.get_answers(question_id)
    return answers



