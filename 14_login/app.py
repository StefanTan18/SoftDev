'''
Stefan Tan 
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request, session
import os 

app= Flask(__name__) #create instance of class Flask

@app.route("/")
def hello_world():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('auth.html')

@app.route("/auth", methods=["POST"])
def authenticate():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
