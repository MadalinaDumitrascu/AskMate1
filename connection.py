import csv
import os
import util

 # QUESTIONS = os.environ['QUESTIONS']





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
        if line['question_id'] == question_id:
            answer = line.get('message')
            answers.append(answer)
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
    print(content)
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for line in content:
            # print(line)
            # writer.writerow(line)
            # print(filename)
            try:
                writer.writerow(line)
            except Exception as exc:
                exc.args += (line,)
                raise


def delete_question(filename, headers, question_id):
    content = get_data(filename)
    print(content)
    # results = [result for result in get_data(filename)if result["id"] != question_id]
    results = []
    for question in content:
        if question['id'] != question_id:
            results.append(question)
    print(f'rezultat {results}')
    rewrite_db(filename, headers, results)









