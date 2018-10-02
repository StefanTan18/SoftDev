'''
Frozen Cookies - T. Fabiha && Stefan Tan
SoftDev1 pd6
K14 -- Do I Know You?
2018-10-01
'''

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)

# hardcopy of the user data
user = "bob"
pswd = "bobby"

@app.route("/")
def home():
    login = session.get("username") == user and session.get("password") == pswd # checks to see if user is logged in correctly
    mistake = "" # will hold the mistake messages
    #print(login)

    # sees if there needs to be mistake messages added to the site
    # if user is not logged in but has attemped to log in then there's something wrong
    if not login and session.get("attempted"):

        # if the username is incorrect
        if not (session.get("username") == user):
            #mistake += "Username is incorrect. "
            flash("Username is incorrect.")
    
            # if the password is incorrect
            if not (session.get("password") == pswd):
                #mistake += "Password is incorrect."
                flash("Password is incorrect.")

                #print("Session's value of logged: ")
                #print(session.get("logged"))
            
                return render_template("login.html", logged = login, name = session.get("username")) # name of user
    
            @app.route("/auth")
            def authorization():
                session["username"] = request.args["username"] # stores username
                session["password"] = request.args["password"] # stores password
                session["attempted"] = True # has the user attempted to log in
                return redirect(url_for("home"))

            @app.route("/logout")
            def logout():
                # removes stored data
                session.pop("username")
                session.pop("password")
                session.pop("attempted")
    
                return redirect(url_for("home"))
                                           
            if __name__ == "__main__":
                app.secret_key = os.urandom(32)
                app.debug = True
                app.run()
