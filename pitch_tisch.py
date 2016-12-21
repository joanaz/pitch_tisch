import logging
import csv
import random
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("AnswerIntent", convert={'pitch': str})
def answer(pitch):
    responses = []

    with open('quotes.tsv', 'rb') as csvfile:
        for line in csv.reader(csvfile, delimiter='\t'):
            responses.append(line[0])

    response = random.choice(responses)

    response_template = render_template('response', response=response)
    return statement(response_template)


if __name__ == '__main__':
    app.run(debug=True)