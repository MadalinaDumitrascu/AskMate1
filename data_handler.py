import csv
import os

QUESTIONS = os.environ['QUESTIONS']

def read_questions():
    questions = []
    with open(QUESTIONS, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions
