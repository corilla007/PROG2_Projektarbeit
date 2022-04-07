<h1>Webapplikation "Lernsessionmaster"</h1>
<h2>1. Ausganslage</h2>
In der Lernphase vor den Semesterprüfungen ist es zum Teil unübersichtlich und chaotisch mit der Planung der jeweilligen Lernsessions. Oftmals  wird ein nicht beherrschter Lernstoff vernächlässigt im Verhältnis zum Lernstoff, welche ich bereits beherrsche.
Mit dieser Webappliaktion werden die Lernsessions dokumentiert. Daraus können Rückschlüsse zu Lernstoffen gezogen werden. Ausserdem bietet die Applikation eine zusätzliche Funktion, welches es ermöglicht, das System einen zufälligen Lernstoff auszuwählen und dieser wird vom Anwender anschliessend gelernt. 

<h2>2. Projektidee</h2>
Die Webapplikation soll mir die Planung der jeweiligen Lernsessions pro Fach und Thema erleichtern und mir aufzeigen, welchen Lernstoff ich noch nicht beherrsche. Ausserdem soll die Applikation Aufschluss darüber geben, für welches Fach am meisten investiert wurde.

<h2>3. Betrieb</h2>
Damit die Applikation korrekt funktioniert, müssen folgende Module importiert werden:Flask (Flask, render_template, request, redirect, url_for)
Plotly (plotly.express as px)
Pandas

<h2>4. Workflow</h2>
![](../Flowchart_Projekt_PROG2.png)

<h2>5. Architektur</h2>
<h3>5.1 Home</h3>
Durch das Anwählen des jeweiligen Buttons gelangt der User auf die Seiten Dein Studium, Lernsessions erfassen, Abfrage, Übersicht.
<h3>5.2 Dein Studium</h3>
Der User muss zu Beginn folgende Daten eingeben, welche dann beim Erfassen einer Lernsession hineingezogen werden: 
Was studierst du? (Text)
In welchem Semester befindest du dich? (Zahl)
Welche Fächer hast du in diesem Semester zu absolvieren? (Text)
Button Speichern
<h3>5.3 Lernsession erfassen</h3>
Der User kann eine neue Lernsession erfassen. Folgende Daten müssen eingegeben werden:
Welches Fach hast du gelernt? (Auswahl durch vorherig definierte Fächer)
Welches Thema hast du gelernt?
WIe lange hast du gelernt (in min)?
Wie gut beherrst du den Lernstoff..Sei ehrlich! (Auswahl)
Die Eingabe wird mit dem Klick auf den Button "Speichern" gespeichert. Ausserdem kann noch eine weitere Lernsession mit dem Button "Weitere Lernsession erfassen" erfasst werden.
Wird ein Feld leer gelassen, erscheint eine Fehlermeldung
Das Feld für die Stundenangabe benötigt eine Zahleneingabe. Dafür wird ebenfalls eine Logik eingebaut, welche nur einen Wert der grösser als 1 ist akzeptiert. Andernfalls erscheint eine Fehlermeldung.
<h3>5.4 Abfrage</h3>
Der User kann eine Abfrage starten. Folgende Daten müssen eingegeben werden:
Fach (Auswahl)
Beherrschungsgrad (Auswahl)
Zeit (Zahl, welche mit weniger oder mehr als "Zahl" ausgewählt werden kann)
Wird der Button "Vorschläge für eine Lernsessions" angewählt, werden die Angaben des Users mit den Einträgen in der Datenbank verglichen
Wird ein Feld leer gelassen, erscheint eine Fehlermeldung
Die Felder welche eine Zahl benötigen, müssen einen Wert grösser gleich 1 haben, andernfalls erscheint eine Fehlermeldung
Gibt es keine passende Lernsession, kann der User die Abfrage erneut starten
Gibt es einen passenden Vorschlag, wird dieser Angezeigt.
<h3>5.5 Übersicht</h3>
Die gespeicherten Lernsessions werden auf der Seite Übersicht ausgegeben. Die Seite ist nach Thema und Fach geclustert.
Für die Übersicht kann noch folgende Analyse gestartet werden:
Dieses Fach/Thema wurde am häufigsten gelernt.
Dieses Fach/Thema beherrschst du am besten.
Was solltest du dir nochmals ansehen.
<h2>6. Funktionen</h2>
Dateneingabe: neue Lernsession erfassen, Abfrage für Lernsession
Datenspeicherung: mögliche Lernsessions und durchgeführte Lernsessions werden in JSON-Datei gespeichert
Datenverarbeitung: Abfrage wird mittels For-Schleife mit der Datenbank Lernsessions verglichen, Berechnung für mögliche Lernsession.
Datenausgabe: Ausgabe des Fachs/Themas, mit höchster Lernzeit, Ausgabe des Fachs/Themas, mit bester Beherrschung, Ausgabe des Fachs/Themas, mit niedrigster Beherrschung