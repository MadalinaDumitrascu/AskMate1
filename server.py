from flask import Flask, render_template, request, redirect, url_for
import connection

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def display_questions():
    questions = connection.read_questions()
    print(questions)
    return render_template("list.html", questions=questions)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
