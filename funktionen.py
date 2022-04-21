import json

# Funktion zum Öffnen der Datenbank "faecher".
def open_faecher():
    try:
        with open("datenbank_faecher.json", "r", encoding="utf-8") as datenbank_faecher:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            faecher = json.load(datenbank_faecher)
    except:
        faecher = {}

    return faecher

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

# Funktion zum Öffnen der Datenbank "datenbank_vorschlaege_lernsessions".
def open_vorschlaege():
    try:
        with open("datenbank_vorschlaege_lernsessions.json", "r", encoding="utf-8") as datenbank_vorschlaege_lernsessions:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            vorschlaege = json.load(datenbank_vorschlaege_lernsessions)
    except:
        vorschlaege = {}

    return vorschlaege


def erfassen_speichern_faecher (name_faecher_erfassen_speichern,
                               name_study_antwort,
                               name_semester_antwort,
                               name_subjects_antwort):

    # Funktion open_faecher wird ausgeführt, gespeicherte Fächer werden geöffnet.
# faecher = open_faecher()
#     # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
#     faecher = {
#         name_faecher_erfassen_speichern: {
#             "Studium": name_study_antwort
#             "Semester": name_semester_antwort
#             "Fächer": name_subjects_antwort
#         }
#     }

def erfassen_speichern_lernsession (name_lernsessions_erfassen_speichern,
                                    name_subject_session_antwort,
                                    name_topic_session_antwort,
                                    name_time_session_antwort,
                                    control_session_antwort):

    # Funktion open_lernsessions wird ausgeführt, gespeicherte Fächer werden geöffnet.
    lernsessions = open_lernsessions()

    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernsessions = {
        name_lernsessions_erfassen_speichern: {
            "Fach": name_subject_session_antwort,
            "Thema": name_topic_session_antwort,
            "Lernzeit": name_time_session_antwort,
            "Beherrschungsgrad": control_session_antwort
        }
    }
# Gespeicherte Lernsession werden mit neuer Lernsession ergänzt.
lernsessions.update(lernsession)

# Der Neue Dictonary wird in der Json-Datei gespeichert.
with open('datenbank.lernsessions.json', 'w') as datenbank_lernsessions:
    json.dump(lernsessions, datenbank_lernsessions)

return name_subject_session_antwort, \
       name_topic_session_antwort, \
       name_time_session_antwort, \
       control_session_antwort
