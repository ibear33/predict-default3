# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:14:55 2022

@author: Soph
"""


from flask import Flask
app = Flask(__name__)
import joblib

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method=="POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model = load_model("PredictDefault")
        pred = model.predict([[float(income),float(age),float(loan)]])
        print(pred)
        s = "The predicted default score is:" + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="1"))

if __name__ == "__main__": 
    app.run()