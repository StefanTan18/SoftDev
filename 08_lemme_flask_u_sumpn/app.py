#Stefan Tan
#SoftDev1 pd6
#K8 -- Fill Yer Flask
#2018-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my page!</h1> <h2>Choose one:</h2> <br> <a href='/more'>Want more?</a> <br> <a href='/bye'>Want to leave?</a>"

@app.route("/more")
def more():
    return "Smart choice! Expect more!"

@app.route("/bye")
def bye():
    return "<h1>No offense taken. Bye!</h1> <br> <a href='/'>Back</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
