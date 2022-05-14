from datetime import date
import json


# Funktion zum Öffnen der Datenbank "datenbank_studium  ".
def open_lernstoff():
    try:
        with open("datenbank_lernstoff.json", "r", encoding="utf-8") as datenbank_lernstoff:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            lernstoff = json.load(datenbank_lernstoff)

    except FileNotFoundError:
        lernstoff = {}

    return lernstoff


# Funktion zum Öffnen der Datenbank "datenbank_lernsessions".
def open_lernsessions():
    try:
        with open("datenbank_lernsessions.json", "r", encoding="utf-8") as datenbank_lernsessions:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            lernsessions = json.load(datenbank_lernsessions)
    except FileNotFoundError:
        lernsessions = {}

    return lernsessions


# Funktion zum Öffnen der Datenbank "datenbank_vorschlaege_lernsessions".
def open_vorschlaege():
    try:
        with open("datenbank_vorschlaege_lernsessions.json", "r", encoding="utf-8") as datenbank_vorschlaege_lernsessions:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            vorschlaege = json.load(datenbank_vorschlaege_lernsessions)
    except FileNotFoundError:
        vorschlaege = {}

    return vorschlaege


def erfassen_speichern_lernstoff(name_lernstoff_subjects_antwort,
                                 name_lernstoff_topic_antwort,
                                 name_lernstoff_control_antwort):

    #Funktion open_lernstoff wird ausgeführt, gespeicherte Angaben werden geöffnet.
    lernstoff = open_lernstoff()
    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernstoff_einzel = {
            "Fach": name_lernstoff_subjects_antwort,
            "Thema": name_lernstoff_topic_antwort,
            "Beherrschungsgrad": name_lernstoff_control_antwort
    }

    lernstoff.update(lernstoff_einzel)

    # Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernstoff.json', 'w') as datenbank_lernstoff:
        json.dump(lernstoff, datenbank_lernstoff)


def erfassen_speichern_lernsession(name_subject_session_antwort,
                                   name_topic_session_antwort,
                                   name_time_session_antwort,
                                   control_session_antwort):

    # Funktion open_lernsessions wird ausgeführt, gespeicherte Fächer werden geöffnet.
    lernsessions = open_lernsessions()

    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernsession = {
            "Fach": name_subject_session_antwort,
            "Thema": name_topic_session_antwort,
            "Lernzeit": name_time_session_antwort,
            "Beherrschungsgrad": control_session_antwort
    }
# Gespeicherte Lernsessions werden mit neuer Lernsession ergänzt.
    lernsessions.update(lernsession)

# Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernsessions.json', 'w') as datenbank_lernsessions:
        json.dump(lernsessions, datenbank_lernsessions)


def ranking_auflistung(name_lernstoff_subjects_ranking_antwort,
                       name_lernstoff_topic_ranking_antwort,
                       name_lernstoff_control_ranking_antwort):
    for option in "lernstoff_erfassen.html":
        if option == "Sehr Schlecht" or "Schlecht":
            auflistung = {
                "Fach": name_lernstoff_subjects_ranking_antwort,
                "Thema": name_lernstoff_topic_ranking_antwort,
                "Beherrschungsgrad": name_lernstoff_control_ranking_antwort
            }
            return auflistung






