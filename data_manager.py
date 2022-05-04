import connection


def get_data_base(filename):
    content= connection.get_data(filename)
    return content


def get_one_question(filename, question_id):
    question = connection.select_by_id(filename, question_id)
    return question

def get_message(filename, question_id):
    message = connection.get_message(filename, question_id)
    return message

def get_answers(filename, question_id):
    answers = connection.get_answers(filename, question_id)
    return answers

def generate_id_number(filename):
    id = connection.generate_id_number(filename)

    return int(id)

def write_question(filename, headers, data):
    new_entry = connection.write_question(filename, headers, data)



