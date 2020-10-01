import os

from flask import Flask, render_template


app = Flask(__name__, template_folder='.', static_folder='./simulator')

@app.route("/sim")
def graphing():
    return render_template('index.html')