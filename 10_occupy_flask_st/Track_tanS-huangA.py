'''
Team Track -- Addison Huang and Stefan Tan
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-21
'''

from flask import Flask, render_template
import csv, random

app=Flask(__name__)


@app.route("/")
def link():
    return "<a href = 'http://127.0.0.1:5000/occupations'> Occupations!</a>"

@app.route("/occupations")
def occupations():
    reader = csv.reader(open('occupations.csv')) #opens and reads the csv file
    next(reader) # skips the headers
    d={} #intialized the dictionary
    for row in reader: #iterates through the csv file and updates the dictionary accordingly
        d[row[0]]=float(row[1])
    d.pop('Total') # gets rid of the last row
    occupations = list(d.keys()) #makes a list of all the occupations
    percentages = list(d.values()) #makes a list of all the occuaption
    result = random.choices(occupations, percentages)
    #returns a list of size 1 with a random occupation choosen based on the percentages
    return render_template("template.html",
                           boo = result.pop(),
                       foo="Occupations in the United States", #the title will be "Occupations in the United States"
                       collection=d #d replaces collection in the html
)

if __name__ == "__main__":
    app.debug = True
    app.run()


