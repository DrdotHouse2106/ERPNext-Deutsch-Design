# Deutsch & Design für ERPNext

Eine Frappe-App für ERPNext v16:

- **Vollständig deutsche Oberfläche.** ERPNext und Frappe haben rund 1.300 Texte ohne deutsche Übersetzung. Die App liefert sie fertig mit, ohne API-Schlüssel oder laufende Kosten.
- **Frischeres Design** (geplant). Firmenfarbe für alle, eigene Farbe je Benutzer, farbige Kacheln und Kennzahlen.
- **Startseite.** Wer in seinem Benutzer einen Standard-Arbeitsbereich einträgt, landet beim ersten Öffnen der Kachelseite (`/`, `/desk`, nach dem Login) direkt dort. Die Kachelseite bleibt über das Logo erreichbar.

## Übersetzungen

Die Texte stehen in `deutsch_design/translations/de.csv`. Sie füllen nur Lücken:

1. Eigene Übersetzungen der Seite (Doctype „Übersetzung“) haben immer Vorrang.
2. Was ERPNext oder eine andere App schon übersetzt, wird nicht angefasst.
3. Nur Texte ohne deutsche Fassung kommen aus dieser App.

Abgedeckt sind Frappe, ERPNext und ERPNext Germany (Stand Version 16).

### Pflege nach Updates

```bash
pip install polib
python3 werkzeuge/abgleich.py
```

Das Werkzeug entfernt Einträge, die ERPNext inzwischen selbst übersetzt, und schreibt neue Lücken nach `werkzeuge/fehlend.json`. Die werden übersetzt und in die CSV übernommen.

## Installation

```bash
bench get-app https://github.com/DrdotHouse2106/ERPNext-Deutsch-Design
bench --site <site> install-app deutsch_design
```

Nach der Installation einmal den Cache leeren (`bench --site <site> clear-cache`), damit die Übersetzungen geladen werden.

## Lizenz

MIT
