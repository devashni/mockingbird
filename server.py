"""Server for Mockingbird (a Markov Chain based text generator) web-app"""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect, flash, url_for)

import jinja2
from jinja2 import StrictUndefined

from model import connect_to_db

import markov
import crud
from testtext import trump_tweets, monty_python, oscar_wilde

import api

app = Flask(__name__)

source_dict = {"God": None, "Monty Python": monty_python, "Trump Tweets": trump_tweets,
               "Oscar Wilde": oscar_wilde, "Sigmund Freud": None, "George Carlin": None}

# same as @app.route("/", methods=['GET']) because GET is default method
@app.route("/")
def homepage():
    """View homepage."""
    print('DEVZ: Someone requested the home page!')
    return render_template("index.html")

def get_text_for_source(sourcename):
    if (sourcename[:1] == '@'):
        return api.get_tweets_for_user(sourcename[1:])
    else:
        return source_dict[sourcename]

####### ! IMPORTANT #######
# ? What's happening below - understand exactly
@app.route("/gettweets/<firstsourcename>/<secondsourcename>", methods=['GET'])
def show_markovtext(firstsourcename, secondsourcename):
    final_return_text = ''

    if (firstsourcename != 'IGNOREVALUE'):
        final_return_text += get_text_for_source(firstsourcename)
    if (secondsourcename != 'IGNOREVALUE'):
        final_return_text += get_text_for_source(secondsourcename)

    return final_return_text

    """Get source text from user and return a markov chain to answer the selected question"""
    # return render_template('index.html', markov_input_text= markov_input_text, text_source1=source_name)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
