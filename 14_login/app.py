'''
Frozen Cookies - T. Fabiha && Stefan Tan
SoftDev1 pd6
K14 -- Do I Know You?
2018-10-01
'''

from flask import Flask, render_template, request, session, url_for, redirect
import os 

app= Flask(__name__) #create instance of class Flask

username = "Bob"
passwd = "bobby"

@app.route("/")
def hello_world():
    if session.get("username") == "Bob":
        return render_template("auth.html", username = session.get("username"))
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == username:
        if request.form["password"] == passwd:
            session["username"] = "Bob"
            return render_template("auth.html", username = session.get("username"))
        else:
            return render_template("error.html", message = "Wrong Password. Please try again.")
    else:
        return render_template("error.html", message = "Wrong Username. Please try again.")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("hello_world"))

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
    
