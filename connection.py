import csv
import os
import util


def get_data(filename):
    content = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append(row)
    return content


def select_by_id(filename, question_id):
    content = get_data(filename)
    for line in content:
        if line['id'] == question_id:
            return line


def get_answers(filename, question_id):
    content = get_data(filename)
    answers = []
    for line in content:
        if line['question_id'] == question_id:
            # answer = line.get('message')
            answers.append(line)
    return answers


def get_message(filename, question_id):
    content= get_data(filename)
    messages = []
    for line in content:
        if line['id'] == question_id:
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


def write(filename, headers, data):
    with open(filename, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(data)


def rewrite_db(filename, headers, content):
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for line in content:
            try:
                writer.writerow(line)
            except Exception as exc:
                exc.args += (line,)
                raise


def modify_id(filename_two, headers, question_id):
    content = get_data(filename_two)
    results = []
    for line in content:
        if line['question_id'] != question_id:
            results.append(line)
    rewrite_db(filename_two, headers, results)


def delete_info(filename, headers, question_id):
    content = get_data(filename)
    results = []
    for question in content:
        if question['id'] != question_id:
            results.append(question)
    rewrite_db(filename, headers, results)



def get_answer_id(filename, answer_id):
    content = get_data(filename)
    question_id = ''
    for line in content:
        if line['id'] == answer_id:
            question_id = line['question_id']
    return question_id


def increase_vote(filename, headers, question_id):
    content = get_data(filename)
    result = []
    for line in content:
        if line['id'] == question_id:
            vote = int(line['vote_number'])+1
            line.update({'vote_number': str(vote)})
        result.append(line)
    rewrite_db(filename, headers, result)
    return result











