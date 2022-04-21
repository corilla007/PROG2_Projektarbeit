from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from funktionen import erfassen_speichern_faecher

app = Flask('Lernsessionmaster')

@app.route("/")
def home():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
    return render_template("index.html")

@app.route("/faecher-erfassen", methods= ["get", "post"])
def study_erfassen():
    if request.method.lower() == "post":
        # Die Antworten aus dem Formular faecher-erfassen.html werden in Variablen gespeichert.
        name_study_antwort = request.form["study"]
        name_semester_antwort = request.form["semester"]
        name_subjects_antwort = request.form["subjects"]
        # Die Funktion erfassen_speichern_faecher aus funktionen.py wird mit den Variablen ausgeführt.
        erfassen_speichern_faecher(name_faecher_erfassen_speichern,
                                   name_study_antwort,
                                   name_semester_antwort,
                                   name_subjects_antwort)
        return render_template("faecher_erfassen.html", name=name_faecher_erfassen_speichern)
    return redirect(url_for("lernsession_erfassen.html")


@app.route("/lernsession-erfassen", methods= ["get", "post"])
def lernsession_erfassen():
    if request.method.lower() == "post":
        # Die Antworten aus dem Formular faecher-erfassen.html werden in Variablen gespeichert.
        name_subject_session_antwort = request.form["subject_session"]
        name_topic_session_antwort = request.form["topic_session"]
        name_time_session_antwort = request.form["time_session"]
        # Antwort wird in Integer umgewandelt - damit kann später gerechnet werden.
        name_time_session_antwort = int(name_time_session_antwort)
        control_session_antwort = request.form["control_session"]

        # Die Funktion erfassen_speichern_lernsession aus funktionen.py wird mit den Variablen durchgeführt
        erfassen_speichern_lernsession(name_lernsessions_erfassen_speichern,
                                       name_subject_session_antwort,
                                       name_topic_session_antwort,
                                       name_time_session_antwort,
                                       control_session_antwort)

    return render_template("lernsession_erfassen.html", name=name_lernsessions_erfassen_speichern)




@app.route("/vorschlaege", methods=["get", "post"])
def vorschlaege_ausgabe():
    if request.method.lower() == "post":


#@app.route("/uebersicht")
#def uebersicht():
    #
#   return render_template('uebersicht.html',
#                          lernsessions_gespeichert=lernsessions_gespeichert_oeffnen())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
