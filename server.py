from flask import Flask, render_template, request, redirect, url_for
import data_manager
import os
import util
import connection

app = Flask(__name__)

# QUESTIONS = os.environ['QUESTIONS']
headers=['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
questions_bd = 'C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\question.csv'
answers_bd = 'C:\\Users\\Madalina\\Desktop\\Projects\\web\\ask-mate-1-python-MadalinaDumitrascu\\sample_data\\answer.csv'

# print(QUESTIONS)


@app.route("/", methods=["POST", "GET"])
def display_questions():

    questions = data_manager.get_data_base(questions_bd)
    return render_template("list.html", questions=questions)


@app.route("/question/<question_id>", methods=["post", "get"])
def get_question_page(question_id):
    print('here')
    filename = questions_bd
    question_id = int(question_id)
    question = data_manager.get_one_question(filename, question_id)
    print(question)
    messages = data_manager.get_message(filename, question_id)
    answers = data_manager.get_answers(answers_bd, question_id)
    return render_template('question.html',question=question,messages=messages, answers=answers )


@app.route("/add-question", methods=["POST", "GET"])
def form():
    filename = questions_bd
    id_question = data_manager.generate_id_number(filename)
    if request.method == "POST":
        title = request.form.get("title")
        message = request.form.get("question")
        data_manager.write_question(filename, headers, data={
            'id': id_question,
            'submission_time': util.get_current_time(),
            'view_number': 0,
            'vote_number': 0,
            'title': title,
            'message': message,
            'image': None
        })
        return redirect(url_for('display_questions'))
    return render_template("add-question.html", id_question=id_question)


@app.route('/question/1/new-answer', methods=['POST', 'GET'])
def new_answer():

    return render_template('new_answer.html' )


@app.route('/question/<question_id>/delete', methods=['DELETE'])
def delete_question(question_id):
    filename = questions_bd
    if request.method == 'DELETE':
        deleted_question= connection.delete_question(filename, headers, question_id)
    return render_template('delete_question.html', question_id=question_id)



if __name__ == "__main__":
    app.run(debug=True)
