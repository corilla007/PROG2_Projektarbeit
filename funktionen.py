import json


# Funktion zum Öffnen der Datenbank "datenbank_studium  ".
def open_db(datei):
    try:
        with open(datei, "r", encoding="utf-8") as datenbank_datei:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            dateiinhalte = json.load(datenbank_datei)

    except FileNotFoundError:
        dateiinhalte = []

    return dateiinhalte


def erfassen_speichern_lernstoff(name_lernstoff_subjects_antwort,
                                 name_lernstoff_topic_antwort,
                                 name_lernstoff_control_antwort):

    #Funktion open_lernstoff wird ausgeführt, gespeicherte Angaben werden geöffnet.
    lernstoff = open_db("datenbank_lernstoff.json")
    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernstoff_einzel = {
            "Fach": name_lernstoff_subjects_antwort,
            "Thema": name_lernstoff_topic_antwort,
            "Beherrschungsgrad": name_lernstoff_control_antwort
    }

    lernstoff.append(lernstoff_einzel)

    # Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernstoff.json', 'w') as datenbank_lernstoff:
        json.dump(lernstoff, datenbank_lernstoff, indent=2)


def erfassen_speichern_lernsession(name_subject_session_antwort,
                                   name_topic_session_antwort,
                                   name_time_session_antwort,
                                   control_session_antwort):

    # Funktion open_lernsessions wird ausgeführt, gespeicherte Fächer werden geöffnet.
    lernsessions = open_db("datenbank_lernsessions.json")

    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernsession = {
            "Fach": name_subject_session_antwort,
            "Thema": name_topic_session_antwort,
            "Lernzeit": name_time_session_antwort,
            "Beherrschungsgrad": control_session_antwort
    }
# Gespeicherte Lernsessions werden mit neuer Lernsession ergänzt.
    lernsessions.append(lernsession)

# Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernsessions.json', 'w') as datenbank_lernsessions:
        json.dump(lernsessions, datenbank_lernsessions, indent=2)


def ranking_grad():
    #datenbank datenbank_lernstoffe wird geöffnet
    datei_inhalt = open_db("datenbank_lernstoff.json")
    mein_ranking = []
    p1_liste = []
    p2_liste = []
    p3_liste = []

    for element in datei_inhalt:
        if element["Beherrschungsgrad"] == "Sehr schlecht":
            grad = "Prio 1"
            p1_liste.append({"Fach": element["Fach"], "Thema": element["Thema"], "Beherrschungsgrad": element["Beherrschungsgrad"],"Grad": grad})
        elif element["Beherrschungsgrad"] == "Schlecht":
            grad = "Prio 2"
            p2_liste.append({"Fach": element["Fach"], "Thema": element["Thema"], "Beherrschungsgrad": element["Beherrschungsgrad"],"Grad": grad})
        else:
            grad = "Prio 3"
            p3_liste.append({"Fach": element["Fach"], "Thema": element["Thema"], "Beherrschungsgrad": element["Beherrschungsgrad"],"Grad": grad})

    mein_ranking = mein_ranking + p1_liste + p2_liste + p3_liste
    return mein_ranking


def best():
    dateninhalt = open_db("datenbank_lernsessions.json")
    best_list = []
    for listen_element in dateninhalt:
        if listen_element["Beherrschungsgrad"] == "Sehr gut":
            best_list.append({"Thema": listen_element["Thema"]})
    return best_list

def worst():
    dateninhalt_2 = open_db("datenbank_lernsessions.json")
    worst_list = []
    for listen_element in dateninhalt_2:
        if listen_element["Beherrschungsgrad"] == "Sehr schlecht":
            worst_list.append({"Thema": listen_element["Thema"]})
    return worst_list







