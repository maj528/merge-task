# Coding Task "merge"

## Aufgabe: 
Implementieren Sie eine Funktion MERGE die eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von Intervallen zurückgibt. Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein. Alle nicht überlappenden Intervalle bleiben unberührt.

## Vorgehensweise
* Liste von Intervallen wird sortiert
* wird geprüft, ob Eingaben falsch sind
* eine Überlappung findet statt wenn: die untere Zahl des ersten Intervalls größer als die des zweiten Intervalls ist


## Wie ist die Laufzeit Ihres Programms ? 
* die Laufzeit wird von unittest gerechnet. Dies ist allerdings nicht optimal. Für zukünftige Tests und größere Datenmengen habe ich einen Test geschrieben, der eine genauere Laufzeit rechnet.
## Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben ?
* das Ausfiltern von falschen Eingaben ist extrem wichtig, um die Robustheit aufrechtzuerhalten. Größere Datenmenge müssen vorgeprüft werden um fehlerhafte Eingaben im Voraus abzufangen. 
## Wie verhält sich der Speicherverbrauch ihres Programms ?

## Weitergehende Überlegungen
* in Zukunft würde ich gern besser lernen, wie man sehr große zufällige Datenmengen generieren kann um die Robustheit des Programms weiter zu prüfen
