import json


# Funktion zum Öffnen der Datenbank "datenbank_studium  ".
def open_db(datei):
    try:
        with open(datei, "r") as datenbank_datei:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            dateiinhalte = json.load(datenbank_datei)

    except FileNotFoundError:
        dateiinhalte = []

    return dateiinhalte


def erfassen_speichern_lernstoff(name_lernstoff_subjects_antwort,
                                 name_lernstoff_topic_antwort,
                                 name_lernstoff_control_antwort):

    # Funktion open_db wird ausgeführt, gespeicherte Lernstoffe werden geöffnet.
    lernstoff = open_db("datenbank_lernstoff.json")
    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernstoff_einzel = {
            "Fach": name_lernstoff_subjects_antwort,
            "Thema": name_lernstoff_topic_antwort,
            "Beherrschungsgrad": name_lernstoff_control_antwort
    }
    # for value in lernstoff:
    #     if not any(d["Thema"] == value for d in lernstoff):
    lernstoff.append(lernstoff_einzel)
    #     else:
    #         lernstoff = lernstoff
    # Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernstoff.json', 'w') as datenbank_lernstoff:
        json.dump(lernstoff, datenbank_lernstoff, indent=2)


def erfassen_speichern_lernsession(name_subject_session_antwort,
                                   name_topic_session_antwort,
                                   name_time_session_antwort,
                                   control_session_antwort):

    # Funktion open_db wird ausgeführt, gespeicherte Lernsession werden geöffnet.
    lernsessions = open_db("datenbank_lernsessions.json")

    # Neuer Dictionary wird mit den eingetragenen Daten befüllt.
    lernsession = {
            "Fach": name_subject_session_antwort,
            "Thema": name_topic_session_antwort,
            "Lernzeit": name_time_session_antwort,
            "Beherrschungsgrad": control_session_antwort
    }
# Gespeicherte Lernsessions werden mit neuer Lernsession ergänzt.
    for element in lernsessions:
        if not any(d["Thema"] == element for d in lernsessions):
            lernsessions.append(lernsession)

# Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_lernsessions.json', 'w') as datenbank_lernsessions:
        json.dump(lernsessions, datenbank_lernsessions, indent=2)


def ranking_grad():
    # Funktion open_db wird ausgeführt, gespeicherte Lernstoffe werden geöffnet.
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


def zeit():
    dateninhalt_3 = open_db("datenbank_lernsessions.json")
    summe = 0
    zeit_list = []
    for listen_elemente in dateninhalt_3:
        if listen_elemente["Fach"] == listen_elemente["Fach"]:
            summe += listen_elemente["Lernzeit"]
            zeit_list.append({"Fach": listen_elemente["Fach"], "Lernzeit": listen_elemente["Lernzeit"]})
    return zeit_list


def thema():
    dateninhalt_4 = open_db("datenbank_lernstoff.json")
    zero_list = []
    summe_1 = 0
    summe_2 = 0
    summe_3 = 0
    summe_4 = 0
    summe_5 = 0
    # Wie viele Themen welchen Beherrschungsgrad (sehr gut, gut, ok, schlecht, sehr schlecht) haben
    a_key = "Beherrschungsgrad"
    zero_list.append([a_dict[a_key] for a_dict in dateninhalt_4])
    for listen_element in zero_list:
        if listen_element == "Sehr gut":
            summe_1 = summe_1 + 1
        elif listen_element == "Gut":
            summe_2 = summe_2 + 1
        elif listen_element == "O.K.":
            summe_3 = summe_3 + 1
        elif listen_element == "Schlecht":
            summe_4 = summe_4 + 1
        else:
            summe_5 = summe_5 + 1

    # Funktion open_db wird ausgeführt
        anzahl_beherrschungen = open_db("datenbank_anzahl_grad.json")

        grad_einzel = {
            {"Beherrschungsgrad": "Sehr gut", "Anzahl": summe_1},
            {"Beherrschungsgrad": "Gut", "Anzahl": summe_2},
            {"Beherrschungsgrad": "O.K.", "Anzahl": summe_3},
            {"Beherrschungsgrad": "Schlecht", "Anzahl": summe_4},
            {"Beherrschungsgrad": "Sehr schlecht", "Anzahl": summe_5}
        }

        anzahl_beherrschungen.append(grad_einzel)

        # Der Neue Dictonary wird in der Json-Datei gespeichert.
        with open('datenbank_anzahl_grad.json', 'w') as datenbank_anzahl_beherrschungen:
            json.dump(anzahl_beherrschungen, datenbank_anzahl_beherrschungen, indent=2)













