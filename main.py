from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from funktionen import erfassen_speichern_studium, erfassen_speichern_lernsession, open_lernsessions, filter

app = Flask('Lernsessionmaster')

@app.route("/")
def home():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
    return render_template("index.html")

@app.route("/studium_erfassen", methods=["get", "post"])
def study_erfassen():
    if request.method.lower() == "post":
        # Die Antworten aus dem Formular studium_erfassen.html werden in Variablen gespeichert.
        name_study_antwort = request.form["study"]
        name_semester_antwort = request.form["semester"]
        name_subjects_antwort = request.form["subjects"]
        # Die Funktion erfassen_speichern_studium aus funktionen.py wird mit den obenstehenden Variablen ausgeführt.
        erfassen_speichern_studium(name_study_antwort,
                                   name_semester_antwort,
                                   name_subjects_antwort)
        return render_template("studium_erfassen.html", name=name_studium_erfassen_speichern)
    return redirect(url_for("lernsession_erfassen.html"))


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
        return render_template("bestaetigung.html", name=name_lernsessions_erfassen_speichern)
    return render_template("lernsession_erfassen.html")

@app.route("/vorschlaege_erfassen", methods=["get", "post"])
def vorschlaege_ausgabe():
    if request.method.lower() == "post":
        #Antworten aus dem Formular vorschlaege_lernsession werden in Variablen gespeichert.
        abfrage_vorschlag_subject_antwort = request.form["abfrage_subject"]
        abfrage_vorschlag_control_antwort = request.form["abfrage_control"]

        # Die Funktion filter aus funktionen.py wird mit den Variabeln ausgeführt. Passende Vorschläge werden zurückgegeben.
        vorschlaege = filter(abfrage_vorschlag_subject_antwort,
                            abfrage_vorschlag_control_antwort)
        return render_template("vorschlaege_lernsession.html", gespeicherte_lernsessions=open_lernsessions(), vorschlaege=vorschlaege)
    return render_template("abfrage_lernsession.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
