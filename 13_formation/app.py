'''
Stefan Tan 
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request

app= Flask(__name__) #create instance of class Flask

@app.route("/")
def hello_world():
    print(app)
    return render_template("welcome.html")

@app.route("/auth")
def authenticate():
    print(request)
    print(request.args)
    print(request.headers)
    return render_template('auth.html', username = request.args['username'], method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
