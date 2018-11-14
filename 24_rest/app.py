'''
Stefan Tan
SoftDev1 pd6
K24 -- A RESTful Journey Skyward
2018-11-13
'''

from flask import Flask, render_template
import urllib, json

app= Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def home():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date=2018-11-12&api_key=9TceDW5Qs9Uoe5qTaHeDarSuMq3o3xraObPLjFvq")
    u = u.read()
    data = json.loads(u)
    return render_template("template.html", title=data["title"], heading=data["title"], image=data["url"], expl=data["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()
