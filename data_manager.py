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

def write(filename, headers, data):
    new_entry = connection.write(filename, headers, data)

def delete_info(filename, headers, answer_id):
    connection.delete_info(filename, headers, answer_id)

def increase_vote(filename, headers, question_id):
    connection.increase_vote(filename, headers, question_id)

def modify_id(filename_two, headers, question_id):
    connection.modify_id(filename_two, headers, question_id)

def decrease_vote(filename, headers, question_id):
    connection.decrease_vote(filename, headers, question_id)




