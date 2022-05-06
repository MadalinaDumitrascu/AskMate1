import connection


def get_data_base(filename):
    return connection.get_data(filename)


def get_one_question(filename, question_id):
    return connection.select_by_id(filename, question_id)


def get_message(filename, question_id):
    return connection.get_message(filename, question_id)


def get_answers(filename, question_id):
    return connection.get_answers(filename, question_id)


def generate_id_number(filename):
    return connection.generate_id_number(filename)


def write(filename, headers, data):
    connection.write(filename, headers, data)


def delete_info(filename, headers, answer_id):
    connection.delete_info(filename, headers, answer_id)


def modify_id(filename_two, headers, question_id):
    connection.modify_id(filename_two, headers, question_id)


def increase_vote(filename, headers, id):
    connection.increase_vote(filename, headers, id)


def decrease_vote(filename, headers, id):
    connection.decrease_vote(filename, headers, id)


def edit(filename, headers, question_id, title, message):
    connection.edit(filename, headers, question_id, title, message)
