from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def display_questions():
    questions = data_manager.get_data_base()
    # print(questions)
    return render_template("list.html", questions=questions)

# @app.route("/add-question", methods= ["Post"])
# def add_question():


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
