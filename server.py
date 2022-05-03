from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def display_questions():
    questions = data_manager.get_data_base()
    return render_template("list.html", questions=questions)

@app.route("/question/<question_id>", methods=["post", "get"])
def get_question_page(question_id):
    question_id = int(question_id)
    question = data_manager.get_one_question(question_id)
    messages = data_manager.get_message(question_id)
    answers = data_manager.get_answers(question_id)
    print(question)
    print(f'the mess: {messages}')
    print(answers)
    return render_template('question.html',question=question,messages=messages, answers=answers )

@app.route("/add-question", methods= ["Post"])
def add_question():
    pass


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
