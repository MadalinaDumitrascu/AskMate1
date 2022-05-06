from flask import Flask, render_template, request, redirect, url_for
import data_manager
from os.path import dirname, join
import util

app = Flask(__name__)

# QUESTIONS = os.environ['QUESTIONS']
headers = [
    "id",
    "submission_time",
    "view_number",
    "vote_number",
    "title",
    "message",
    "image",
]
questions_bd = join(dirname(__file__), "sample_data", "question.csv")
answers_bd = join(dirname(__file__), "sample_data", "answer.csv")
ans_headers = [
    "id",
    "submission_time",
    "vote_number",
    "question_id",
    "message",
    "image",
]


@app.route("/")
def display_questions():
    questions = data_manager.get_data_base(questions_bd)
    return render_template("all-questions.html", questions=questions)


@app.route("/question/<question_id>")
def get_question_page(question_id):
    filename = questions_bd
    question = data_manager.get_one_question(filename, question_id)
    messages = data_manager.get_message(filename, question_id)
    answers = data_manager.get_answers(answers_bd, question_id)
    return render_template(
        "question.html",
        question=question,
        messages=messages,
        answers=answers,
    )


@app.route("/add-question", methods=["POST", "GET"])
def form():
    filename = questions_bd
    id_question = data_manager.generate_id_number(filename)

    if request.method == "POST":
        title = request.form.get("title")
        message = request.form.get("question")
        data_manager.write(
            filename,
            headers,
            data={
                "id": id_question,
                "submission_time": util.get_current_time(),
                "view_number": 0,
                "vote_number": 0,
                "title": title,
                "message": message,
                "image": "",
            },
        )
        return redirect(url_for("display_questions"))

    return render_template("add-question.html", id_question=id_question)


@app.route("/question/<question_id>/new-answer", methods=["POST", "GET"])
def new_answer(question_id):
    filename = answers_bd
    id_answer = data_manager.generate_id_number(filename)
    if request.method == "POST":
        message = request.form.get("message")
        data_manager.write(
            filename,
            ans_headers,
            data={
                "id": id_answer,
                "submission_time": util.get_current_time(),
                "vote_number": 0,
                "question_id": question_id,
                "message": message,
                "image": "",
            },
        )
        return redirect(url_for("get_question_page", question_id=question_id))
    return render_template("new-answer.html", question_id=question_id)


@app.route("/question/<question_id>/edit", methods=["POST", "GET"])
def edit_question(question_id):
    filename = questions_bd
    question = data_manager.get_one_question(filename, question_id)
    title = question["title"]
    message = question["message"]

    if request.method == "POST":
        title = request.form.get("title")
        message = request.form.get("message")
        data_manager.edit(filename, headers, question_id, title, message)
        return redirect(url_for("display_questions"))

    return render_template("edit.html", question_id=question_id, question=question)


@app.route("/question/<question_id>/delete", methods=["POST", "GET"])
def delete_question(question_id):
    filename = questions_bd
    filename_two = answers_bd

    if request.method == "POST":
        data_manager.delete_info(filename, headers, question_id)
        data_manager.modify_id(filename_two, ans_headers, question_id)

    return redirect(url_for("display_questions"))


@app.route("/answer/<question_id>/<answer_id>/delete")
def delete_answer(question_id, answer_id):
    filename = answers_bd
    data_manager.delete_info(
        filename,
        ans_headers,
        answer_id,
    )
    return redirect(url_for("get_question_page", question_id=question_id))


@app.route("/question/<question_id>/vote-up")
def vote_up(question_id):
    return util.vote_item(
        question_id,
        data_manager.increase_vote,
        headers,
        questions_bd,
    )


@app.route("/question/<question_id>/vote-down")
def vote_down(question_id):
    return util.vote_item(
        question_id,
        data_manager.decrease_vote,
        headers,
        questions_bd,
    )


@app.route("/answer/<answer_id>/vote-up", methods=["POST", "GET"])
def vote_up_answer(answer_id):
    return util.vote_item(
        answer_id,
        data_manager.increase_vote,
        ans_headers,
    )


@app.route("/answer/<answer_id>/vote-down ", methods=["POST", "GET"])
def vote_down_answer(answer_id):
    return util.vote_item(
        answer_id,
        data_manager.decrease_vote,
        ans_headers,
        answers_bd,
    )


if __name__ == "__main__":
    app.run(debug=True)
