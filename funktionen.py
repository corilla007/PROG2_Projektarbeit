import json

# Funktion zum Öffnen der Datenbank "datenbank_studium  ".
def open_studium():
    try:
        with open("datenbank_studium.json", "r", encoding="utf-8") as datenbank_studium:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            studium = json.load(datenbank_studium)
    except:
        studium = {}

    return studium

# Funktion zum Öffnen der Datenbank "datenbank_lernsessions".
def open_lernsessions():
    try:
        with open("datenbank_lernsessions.json", "r", encoding="utf-8") as datenbank_lernsessions:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            lernsessions = json.load(datenbank_lernsessions)
    except:
        lernsessions = {}

    return lernsessions

# Funktion zum Öffnen der Datenbank "datenbank_vorschlaege_lernsessions".
def open_vorschlaege():
    try:
        with open("datenbank_vorschlaege_lernsessions.json", "r", encoding="utf-8") as datenbank_vorschlaege_lernsessions:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            vorschlaege = json.load(datenbank_vorschlaege_lernsessions)
    except:
        vorschlaege = {}

    return vorschlaege

def erfassen_speichern_studium (name_study_antwort,
                               name_semester_antwort,
                               name_subjects_antwort):
    #Funktion open_studium wird ausgeführt, gespeicherte Angaben werden geöffnet.
    studium = open_studium()
    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    studies = {
        name_studium_erfassen_speichern: {
            "Studium": name_study_antwort,
            "Semester": name_semester_antwort,
            "Fächer": name_subjects_antwort
        }
    }

    studium.update(studies)

def erfassen_speichern_lernsession (name_subject_session_antwort,
                                    name_topic_session_antwort,
                                    name_time_session_antwort,
                                    control_session_antwort):

    # Funktion open_lernsessions wird ausgeführt, gespeicherte Fächer werden geöffnet.
    lernsessions = open_lernsessions()

    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernsession = {
        name_lernsessions_erfassen_speichern: {
            "Fach": name_subject_session_antwort,
            "Thema": name_topic_session_antwort,
            "Lernzeit": name_time_session_antwort,
            "Beherrschungsgrad": control_session_antwort
        }
    }
# Gespeicherte Lernsessions werden mit neuer Lernsession ergänzt.
    lernsessions.update(lernsession)

# Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernsessions.json', 'w') as datenbank_lernsessions:
        json.dump(lernsessions, datenbank_lernsessions)

    return name_subject_session_antwort, \
           name_topic_session_antwort, \
           name_time_session_antwort,\
           control_session_antwort


def filter(abfrage_vorschlag_subject_antwort,
           abfrage_vorschlag_control_antwort):

    # Funktion filter wird ausgeführt, gespeicherte Lernsessions werden geöffnet.
    lernsessions = open_lernsessions()

    # Leerer Dict wird abgefüllt
    vorschlaege = {}

    """
    Der Dict lernsessions wird in key (fach) und 
    value (Beherrschungsgrad) geteilt.
    """
    for key, value in lernsessions.items():
        #Es wird bei allen keys überprüft, ob sie der entsprechenden Variable entsprechen.
        if lernsessions[key]["Fach"] == abfrage_vorschlag_subject_antwort\
                and lernsessions[key]["Beherrschunsgrad"] == abfrage_vorschlag_control_antwort:

        #Values, welche der Abfrage entsprechen, werden in den Vorschlägen angezeigt
            vorschlag = {
            "Fach": lernsessions[key]["Fach"],
            "Beherrschungsgrad": lernsessions[key]["Beherrschunsgrad"]
            }
            vorschlaege.update(vorschlag)

        #Der befüllte Dict "vorschläge" wird in der Datenbank "datenbank_vorschlaege_lernsession gespeichert.
        #Sollte keine Lernsession mit der Abfrage übereinstimmen, wird der String "Leider keine Vorschläge für diese Abfrage vorhanden" ausgegeben.

        if not vorschlaege:
            vorschlaege = {"Fach":{
                "name" : "Leider keine Vorschläge für diese Abfrage vorhanden"
            }}

