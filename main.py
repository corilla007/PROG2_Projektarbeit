from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    name = "Lernsessionmaster"
        cards = [
            {"titel": "Fächer erfassen", "inhalt": "In der Rubrik "Fächer erfassen" kannst du deine aktuellen Fächer in eine Datenbank abspeichern"},
            {"titel": "Lernsession erfassen", "inhalt": "In der Rubrik "Lernsession erfassen" kannst du deine erledigten Lernsession dokumentieren"},
            {"titel": "Vorschläge", "inhalt": "In der Rubrik Vorschläge kannst du verschiedene Kriterien eingeben, erhältst einen Vorschlag für eine Lernsession, welche dann als offener To-Do Punkt unter "Übersicht" aufgelistet wird."},
            {"titel": "Übersicht", "inhalt": "Auf der Übersicht findest du die offenen Vorschläge für deine Lernsessions, welche du noch abarbeiten musst.
                    Ausserdem befindet sich auf der Seite eine Analyse zu deinen erledigten Lernsessions."}
        ]
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
        return render_template("start.html", name=name, cards=cards)

@app.route("/faecher-erfassen", methods= ["get", "post"])
def study_erfassen():
    if request.method.lower() == "post":
        name_study_antwort = request.form['study']
        name_semester_antwort = request.form['semester']
        name_subjects_antwort = request.form['subjects']

        erfassen_speichern_faecher (name_study_antwort,
                           name_semester_antwort,
                           name_time_session_antwort,
                           name_subjects_antwort)

    return render_template('facher_erfassen.html')


@app.route("/lernsession-erfassen", methods=["get", "post"])
def lernsession_erfassen():
    if request.method.lower() == "post":
        name_subject_session_antwort = request.form['subject_session']
        name_topic_session_antwort = request.form['topic_session']
        name_time_session_antwort = request.form['time_session']
        name_time_session_antwort = int(name_time_session_antwort)
        control_session_antwort = request.form['control_session']

        erfassen_speichern_lernsession (name_subject_session_antwort,
                           name_topic_session_antwort,
                           name_time_session_antwort,
                           name_time_session_antwort,
                           control_session_antwort)
    return render_template('lernsession_erfassen.html')



@app.route("/vorschlaege", methods=["get", "post"])
def vorschlaege_ausgabe():
    if request.method.lower() == "post":


@app.route("/uebersicht")
def uebersicht():
    return render_template('uebersicht.html',
                           lernsessions_gespeichert=lernsessions_gespeichert_oeffnen())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
