"""Server for Mocking Bird (a Markov Chain based text generator) web-app"""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect, flash, url_for)

import jinja2
from jinja2 import StrictUndefined

from model import connect_to_db

import markov
# import crud.py


app = Flask(__name__)

app.secret_key = "devashni"
app.jinja_env.undefined = StrictUndefined


# @app.route("/")
# def homepage():
#     """View homepage."""

#     return render_template("homepage.html")


# @app.route("/userprofile")
# def user_profile():
#     """View a user's user profile"""

#     user = crud.get_user() #write this
#     return render_template('all_movies.html')

# text = markovchain.open_and_read_file()

@app.route("/")
def show_markovtext():
    """View Homepage."""
# *Homepage currently displays freshly generated text with every refresh.

    chains = markov.make_chains(markov.make_sentence(markov.trump_tweets))
    random_text = markov.make_text(chains, markov.min_words)

    return render_template('homepage.html', chains = chains, random_text = random_text)


@app.route("/login")
def login_signup():
    """View login  / sign up page."""

    return render_template("login.html")

@app.route('/login', methods=['POST'])
def register_user():
    """Create a new user"""

    email = request.form.get('email')
    password = request.form.get('psw-repeat')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)