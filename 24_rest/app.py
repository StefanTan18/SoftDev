from flask import Flask, render_template
import urllib, json

app= Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def display():
    return render_template("template.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
