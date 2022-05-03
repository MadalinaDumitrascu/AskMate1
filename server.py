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
    return render_template('question.html',question=question,messages=messages, answers=answers )


@app.route("/add-question", methods= ["Post"])
def form():
    id_question = data_manager.generate_id_number()
    if request.method == "POST":
        title = request.form.get("title")
        new_question = request.form.get("new_question")
        data_manager.write_data_base(id_question, title, new_question)
    return render_template("list.html", id_question=id_question)

@app.route('/question/1/new-answer', methods = ['POST', 'GET'])
def new_answer():
    return render_template('new_answer.html' )



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
