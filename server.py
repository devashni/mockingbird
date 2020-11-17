"""Server for Mocking Bird (a Markov Chain based text generator) web-app"""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect, flash, url_for)

import jinja2
from jinja2 import StrictUndefined

from model import connect_to_db

import markov
import crud
from testtext import trump_tweets, monty_python


app = Flask(__name__)

app.secret_key = "devashni"
app.jinja_env.undefined = StrictUndefined

source_dict = {"God": None, "Monty Python": monty_python, "Oscar Wilde": None, "Sigmund Freud": None, "George Carlin":None, "Trump Tweets": trump_tweets }

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")



@app.route("/", methods=['GET','POST'])
def show_markovtext():
    """Get source text from user and return a markov chain to answer the selected question"""

    # ! checking method
    if request.method == 'POST':
        print("DEVZ: We are in POST!")
    else:
        print("DEVZ: We are in GET!")

    # ! print test BEFORE getting form value
    print("DEVZ: About to request the value of firsttextsource")
    text_source1 = request.form.get('firsttextsource')
    # ! print test AFTER getting form value
    print("DEVZ: Result of request: " + str(text_source1))

    # text_source2 = request.form.get('twitterhandle2')
    text = source_dict[text_source1]

    chains = markov.make_chains(markov.make_sentence(text))
    markov_generated_text = markov.make_text(chains, markov.min_words)
    # print (markov_generated_text)

    return render_template('homepage.html', chains = chains, markov_generated_text = markov_generated_text, text_source1 = text_source1 )


@app.route("/login")
def login_signup():
    """View login  / sign up page."""

    return render_template("login.html")
    

@app.route('/login', methods=['POST'])
def register_user():
    """Create a new user"""
    
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password, name)
        flash('Account created! Please log in.')

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)