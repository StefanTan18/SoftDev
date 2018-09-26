'''
Team Track -- Addison Huang and Stefan Tan
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-21
'''

from flask import Flask, render_template
from util import ants
import csv, random

app=Flask(__name__)


@app.route("/")
def link():
    return "<a href = 'http://127.0.0.1:5000/occupations'> Occupations!</a>"

@app.route("/occupations")
def occupations():
    return render_template("template.html",
                           randomOcc = ants.randomizer(ants.occReader()),
                       title ="Occupations in the United States", #the title will be "Occupations in the United States"
                       collection = ants.occReader() #replaces collection in the html
)

if __name__ == "__main__":
    app.debug = True
    app.run()


