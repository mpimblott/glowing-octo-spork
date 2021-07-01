from flask import Flask, render_template, session, redirect
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('under_construction.html')


# set secret for session
app.secret_key = os.urandom(50)

if __name__ == '__main__':
    app.run()
