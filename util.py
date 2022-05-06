from flask import redirect, url_for
from datetime import datetime
import time


def get_current_time():
    return datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S")


def generate_id_number(file):
    return max([int(item.get("id")) for item in file] + [0]) + 1


def vote_item(id, function, headers, filename):
    function(filename, headers, id)
    return redirect(url_for("display_questions", question_id=id))
