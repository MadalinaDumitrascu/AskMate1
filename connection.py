import csv
import os
import util


def get_data(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def select_by_id(filename, question_id):
    return [line for line in get_data(filename) if line.get("id") == question_id][0]


def get_answers(filename, question_id):
    return [
        line for line in get_data(filename) if line.get("question_id") == question_id
    ]


def get_message(filename, question_id):
    return [
        line.get("message")
        for line in get_data(filename)
        if line.get("id") == question_id
    ]


def generate_id_number(filename):
    return util.generate_id_number(filename)


def write(filename, headers, data):
    with open(filename, "a") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(data)


def rewrite_db(filename, headers, content):
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for line in content:
            writer.writerow(line)


def modify_id(filename_two, headers, question_id):
    rewrite_db(
        filename_two,
        headers,
        [
            line
            for line in get_data(filename_two)
            if line.get("question_id") != question_id
        ],
    )


def delete_info(filename, headers, question_id):
    rewrite_db(
        filename,
        headers,
        [line for line in get_data(filename) if line.get("id") != question_id],
    )


def get_answer_id(filename, answer_id):
    return [
        line.get("question_id")
        for line in get_data(filename)
        if line.get("id") == answer_id
    ][0]


def vote(filename, headers, id, modifier):
    result = []
    for line in get_data(filename):
        if line["id"] == id:
            vote = int(line["vote_number"]) + modifier
            line.update({"vote_number": str(vote)})
        result.append(line)
    rewrite_db(filename, headers, result)
    return result


def increase_vote(filename, headers, id):
    return vote(filename, headers, id, 1)


def decrease_vote(filename, headers, id):
    return vote(filename, headers, id, -1)


def edit(filename, headers, question_id, title, message):
    content = get_data(filename)
    result = []
    for line in content:
        if line["id"] == question_id:
            line.update(
                {
                    "title": title,
                    "message": message,
                }
            )
        result.append(line)
    rewrite_db(filename, headers, result)
