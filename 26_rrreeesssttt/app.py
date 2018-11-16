'''
Stefan Tan
SoftDev1 pd6
K26 -- Getting More REST 
2018-11-15
'''

import urllib.request, json

from flask import Flask, render_template

app= Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def home():
    u0 = urllib.request.urlopen("https://www.poemist.com/api/v1/randompoems")
    u0 = u0.read()
    data0 = json.loads(u0)
    #print(data0)

    u1 = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    u1 = u1.read()
    data1 = json.loads(u1)
    #print(data1)

    u2 = urllib.request.urlopen("https://www.boredapi.com/api/activity")
    u2 = u2.read()
    data2 = json.loads(u2)
    #print(data2)
    
    return render_template("index.html", ptitle=data0[0]["title"], pcontent=data0[0]["content"], poet=data0[0]["poet"]["name"], dogpic=data1["message"], a=data2["activity"], peeps=data2["participants"], t=data2["type"])

if __name__ == "__main__":
    app.debug = True
    app.run()
