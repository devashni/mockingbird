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

source_dict = {"God": None, "Monty Python": monty_python, "Trump Tweets": trump_tweets, "Oscar Wilde": oscar_wilde, "Sigmund Freud": None, "George Carlin":None }


@app.route("/") #same as @app.route("/", methods=['GET']) because GET is default method
def homepage():
    """View homepage."""
    print('DEVZ: Someone requested the home page!')
    return render_template("index.html")

####### ! IMPORTANT #######
# ? What's happening below - understand exactly
@app.route("/gettweets/<sourcename>", methods=['GET'])
def show_markovtext(sourcename):
    print('DEVZ: in show markov text! sourcename is: ' + str(sourcename))
    """Get source text from user and return a markov chain to answer the selected question"""
    if (sourcename[:1] == '@'):
        markov_input_text = api.get_tweets_for_user(sourcename[1:])
    else:
        markov_input_text = source_dict[sourcename]

    print('DEVZ: Returning markov input text!')
    return markov_input_text
    # return render_template('index.html', markov_input_text= markov_input_text, text_source1=source_name)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)