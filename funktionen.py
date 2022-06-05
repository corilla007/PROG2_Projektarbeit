import json
import plotly.express as px
from plotly.offline import plot


# Funktion zum Öffnen der Datenbank "datenbank_studium  ".
def open_db(datei):
    try:
        with open(datei, "r") as datenbank_datei:
            # Inhalt der Datenbank wird als Dictonary gespeichert.
            dateiinhalte = json.load(datenbank_datei)

    except FileNotFoundError:
        dateiinhalte = []
        print("no file found or file is corrupted")

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

# Eintragene Antwort wird mit Datenbank verglichen. Ein Thema kann nur einmalig vorkommen.
    # Wenn das Thema bereits existiert, wird der neue dictionary nicht hinzugefügt.

    new_topic = True
    for element in lernstoff:
        if element["Thema"] == name_lernstoff_topic_antwort:
            print('Topic already exists')
            new_topic = False

# Gibt es das Thema noch nicht in der Datenbank, wird der Lernstoff hinzugefügt.

    if new_topic == True:
        lernstoff.append(lernstoff_einzel)
        print('new Topic', name_lernstoff_topic_antwort, 'has been added')


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
    # Funktion open_db wird ausgeführt, gespeicherte Lernstoffe werden geöffnet.
    dateninhalt = open_db("datenbank_lernsessions.json")
    best_list = []
    #Wenn beherrschunsgrad "sehr gut" ist, wird das thema der liste hinzugefügt.
    for listen_element in dateninhalt:
        if listen_element["Beherrschungsgrad"] == "Sehr gut":
            best_list.append({"Thema": listen_element["Thema"]})
    return best_list


def worst():
    # Funktion open_db wird ausgeführt, gespeicherte Lernstoffe werden geöffnet.
    dateninhalt_2 = open_db("datenbank_lernsessions.json")
    worst_list = []
    #Wenn beherrschunsgrad "sehr schlecht" ist, wird das thema der liste hinzugefügt.
    for listen_element in dateninhalt_2:
        if listen_element["Beherrschungsgrad"] == "Sehr schlecht":
            worst_list.append({"Thema": listen_element["Thema"]})
    return worst_list


#Die Lernzeit wird von der Json-Datei "datenbank_lernsessions" herangezogen.
#Fach wird in Liste subject_list abgespeichert, wird Fach in subject_list gefunden (was mindestens 1x der fall ist), erhöht sich counter um 1.
#Beim erstmaligen Aufruf der For-Schlaufe pro Fach wird der Counter "meistens" 1 sein. Damit wird der index als counter_2 gespeichert.
#counter_2 erhöht sich jedesmal beim Aufruf der for-Schlaufe.
#Wenn 2 identische Fächer enthalten sind, wird der urspüngliche Index gelöscht und die Zeit wird aufsummiert.
#Ansonsten wird nur die Lernzeit hinzugefügt.
#Wenn die Daten der neuen liste zugeordnet werden, erhöht sich der index um 1.

def zeit():
    dateninhalt_3 = open_db("datenbank_lernsessions.json")
    zeit_list = []
    subject_list = []
    time = []

    for listen_elemente in dateninhalt_3:
        subject_list.append(listen_elemente["Fach"])
        index = 0
        counter = 0
        counter_2 = 0
        for listindex in subject_list:
            if listen_elemente["Fach"] == listindex:
                counter = counter + 1
                if counter == 1:
                    index = counter_2
            counter_2 = counter_2 + 1

        if counter == 2:
            subject_list = subject_list[:-1]
            time[index] = time[index] + listen_elemente["Lernzeit"]
        else:
            time.append(listen_elemente["Lernzeit"])

    index = 0
    for listindex in subject_list:
        zeit_list.append({"Fach": subject_list[index], "Lernzeit": time[index]})
        index = index + 1

    return zeit_list


#  Funktion dient für die Datenaufbereitung eines Barcharts.
# Daten von der einten Datenbank herausziehen, aufsummiert und in die andere Datenbank abgespeichert.

def thema():
    dateninhalt_4 = open_db("datenbank_lernstoff.json")
    summe_1 = 0
    summe_2 = 0
    summe_3 = 0
    summe_4 = 0
    summe_5 = 0

    # Wie viele Themen welchen Beherrschungsgrad (sehr gut, gut, ok, schlecht, sehr schlecht) haben
    for listen_element in dateninhalt_4:
        if listen_element["Beherrschungsgrad"] == "Sehr gut":
            summe_1 = summe_1 + 1
        elif listen_element["Beherrschungsgrad"] == "Gut":
            summe_2 = summe_2 + 1
        elif listen_element["Beherrschungsgrad"] == "O.K.":
            summe_3 = summe_3 + 1
        elif listen_element["Beherrschungsgrad"] == "Schlecht":
            summe_4 = summe_4 + 1
        else:
            summe_5 = summe_5 + 1

    # print('summe_1 =', summe_1)
    # print('summe_2 =', summe_2)
    # print('summe_3 =', summe_3)
    # print('summe_4 =', summe_4)
    # print('summe_5 =', summe_5)

    # Funktion open_db wird ausgeführt
    anzahl_beherrschungen = open_db("datenbank_anzahl_grad.json")

    #Werte werden in einem einzelnen Dictionary abgespeichert.
    grad_einzel =[
        {"Beherrschungsgrad": "Sehr gut", "Anzahl": summe_1},
        {"Beherrschungsgrad": "Gut", "Anzahl": summe_2},
        {"Beherrschungsgrad": "O.K.", "Anzahl": summe_3},
        {"Beherrschungsgrad": "Schlecht", "Anzahl": summe_4},
        {"Beherrschungsgrad": "Sehr schlecht", "Anzahl": summe_5}
    ]

    # Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_anzahl_grad.json', 'w') as datenbank_anzahl_beherrschungen:
        json.dump(grad_einzel, datenbank_anzahl_beherrschungen, indent=2)

#Daten aus der Datenbank "Datenbank_anzahl_grad" werden in zwei neue Listen abgespeichert für die x und y-Achsenwerte.
def get_data():
    list_anzahl = []
    list_beherrschungsgrad = []
    dateninhalt_5 = open_db("datenbank_anzahl_grad.json")
    for element in dateninhalt_5:
        list_anzahl.append(int(element["Anzahl"]))
        list_beherrschungsgrad.append(element["Beherrschungsgrad"])
    return list_beherrschungsgrad, list_anzahl

#Funktion ruft Funktion "get_data" auf und speichert die x und y-Achsenwerte aus den Listen in die definitiven Variablen "x" und "y" von Plotly.
#Titel und Achsenbeschriften werden vergeben.

def viz():
    beherrschungsgrad, anzahl = get_data()
    fig = px.bar(x=beherrschungsgrad, y=anzahl)
    fig.update_layout(
        title="Anzahl Lernstoffe nach Beherrschungsgrad",
        xaxis_title="Beherrschungsgrad",
        yaxis_title="Anzahl")
    div = plot(fig, output_type="div")
    return div












