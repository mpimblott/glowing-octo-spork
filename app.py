from flask import Flask, render_template, session, redirect, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('under_construction.html')


@app.route('/civ')
def civ():
    return render_template('civ.html')


@app.route('/civ_result', methods=["POST"])
def civ_result():
    no_players = request.form.get("no_players")
    civ_selection = request.form.get("civ_selection")
    return render_template('civ_result.html', no_players=no_players, civ_selection=civ_selection)


# set secret for session
app.secret_key = os.urandom(50)

if __name__ == '__main__':
    app.run()
