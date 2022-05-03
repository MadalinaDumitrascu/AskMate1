from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)

headers=['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
questions_bd = "C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv"
answers_bd = "C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv"


@app.route("/", methods=["POST", "GET"])
def display_questions():
    filename = questions_bd
    questions = data_manager.get_data_base(filename)
    return render_template("list.html", questions=questions)


@app.route("/question/<question_id>", methods=["post", "get"])
def get_question_page(question_id):
    filename = questions_bd
    question_id = int(question_id)
    question = data_manager.get_one_question(filename, question_id)
    messages = data_manager.get_message(filename, question_id)
    answers = data_manager.get_answers(answers_bd, question_id)
    return render_template('question.html',question=question,messages=messages, answers=answers )


@app.route("/add-question", methods= ["POST", "GET"])
def form():
    filename = questions_bd
    id_question = data_manager.generate_id_number(filename)
    if request.method == "POST":
        title = request.form.get("title")
        new_question = request.form.get("new_question")
        data_manager.write_question(filename, headers, id_question, title, new_question)
    return render_template("add-question.html", id_question=id_question)

@app.route('/question/1/new-answer', methods = ['POST', 'GET'])
def new_answer():
    return render_template('new_answer.html' )



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
