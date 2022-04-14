from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import random
from datetime import datetime


app = Flask(__name__)

@app.route("/Faecher-erfassen" = ["get", "post"])
def form_studium():
    if request.method.lower() == "get":
        return render_template("formular_faecher_erfassen.html")
    if request.method.lower() == "post":
        link to Lernsessions erfassen



@app.route("/Lernsessions-erfassen" = ["get", "post"])
def form_lernsession():
    if request.method.lower() == "get":
        return render_template("formular_lernsession_erfassen.html")
    if request.method.lower() == "post":
        link to Abfrage


@app.route("/Abfrage", methods = ["get", "post"])
def form_abfrage():
    if request.method.lower() == "get":
        return render_template("formular_abfrage.html")
    if request.method.lower() == "post":
        link to Uebersicht


@app.route("/Uebersicht")
def uebersicht():
    if request.method.lower() == "get":
        return render_template("formular_uebersicht.html")
    if request.method.lower() == "post":

if __name__ == "__main__":
    app.run(debug=True, port=5000)
