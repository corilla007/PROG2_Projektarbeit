from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot
from funktionen import erfassen_speichern_lernstoff, erfassen_speichern_lernsession, ranking_grad, best, worst
from datetime import date



app = Flask('Lernrock')


@app.route("/")
def home():
    return render_template("index.html")
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.


@app.route("/lernstoff_erfassen", methods=["get", "post"])
def lernstoff_erfassen():
    if request.method.lower() == "post":
        # Die Antworten aus dem Formular lernstoff_erfassen werden in Variablen gespeichert.
        name_lernstoff_subjects_antwort = request.form["subjects_lernstoff"]
        name_lernstoff_topic_antwort = request.form["topic_lernstoff"]
        name_lernstoff_control_antwort = request.form["control_lernstoff"]

        # Die Funktion erfassen_speichern_lernstoff aus funktionen.py wird mit den obenstehenden Variablen ausgeführt
        erfassen_speichern_lernstoff(name_lernstoff_subjects_antwort,
                                     name_lernstoff_topic_antwort,
                                     name_lernstoff_control_antwort)
        return render_template("Ranking_Lernstoff.html")
    return render_template("lernstoff_erfassen.html")


@app.route("/ranking", methods=["get", "post"])
def ranking():
    daten = ranking_grad()
    return render_template("Ranking_Lernstoff.html", mein_ranking=daten)


@app.route("/lernsession_erfassen", methods=["get", "post"])
def lernsession_erfassen():
    if request.method.lower() == "post":
        # Die Antworten aus dem Formular lernsession_erfassen.html werden in Variablen gespeichert.
        name_subject_session_antwort = request.form["subject_session"]
        name_topic_session_antwort = request.form["topic_session"]
        name_time_session_antwort = request.form["time_session"]
        # Antwort wird in Integer umgewandelt - damit kann später gerechnet werden.
        name_time_session_antwort = int(name_time_session_antwort)
        control_session_antwort = request.form["control_session"]

        # Die Funktion erfassen_speichern_lernsession aus funktionen.py wird mit den obenstehenden Variablen ausgeführt.
        erfassen_speichern_lernsession(name_subject_session_antwort,
                                       name_topic_session_antwort,
                                       name_time_session_antwort,
                                       control_session_antwort)
        return render_template("bestaetigung.html")
    return render_template("lernsession_erfassen.html")


@app.route("/uebersicht")
def berechnungen():
    daten = best()
    datensicht_2 = worst()
    return render_template("uebersicht.html", best_list=daten, worst_list=datensicht_2)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
