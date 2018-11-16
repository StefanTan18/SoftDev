'''
Stefan Tan
SoftDev1 pd6
K25 --Getting More REST
2018-11-14
'''

from flask import Flask, render_template
import urllib, json

app= Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def home():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date=2018-11-12&api_key=9TceDW5Qs9Uoe5qTaHeDarSuMq3o3xraObPLjFvq")
    u = u.read()
    data = json.loads(u)
    #print(data)

    u1 = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/us?fullText=true")
    u1 = u1.read()
    data1 = json.loads(u1)
    #print(data1)
    
    return render_template("template.html", title=data["title"], heading=data["title"], image=data["url"], expl=data["explanation"], country=data1[0]["name"], capital=data1[0]["capital"], flag=data1[0]["flag"])

if __name__ == "__main__":
    app.debug = True
    app.run()
