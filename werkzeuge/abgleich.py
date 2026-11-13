"""Gleicht deutsch_design/translations/de.csv mit den aktuellen deutschen Übersetzungen ab.

- Entfernt Einträge, die die jeweilige App inzwischen selbst übersetzt.
- Schreibt neue, noch fehlende Texte nach werkzeuge/fehlend.json (zum Übersetzen).

Aufruf: python3 werkzeuge/abgleich.py  (braucht: pip install polib)
"""

import csv
import json
import pathlib
import urllib.request

import polib

ZWEIG = "version-16"
APPS = {
	"frappe": "frappe/frappe",
	"erpnext": "frappe/erpnext",
	"erpnext_germany": "alyf-de/erpnext_germany",
}
CSV = pathlib.Path(__file__).parent.parent / "deutsch_design" / "translations" / "de.csv"


def katalog(app, repo):
	url = f"https://raw.githubusercontent.com/{repo}/{ZWEIG}/{app}/locale/de.po"
	return polib.pofile(urllib.request.urlopen(url, timeout=60).read().decode())


def main():
	eigene = {(r[2] if len(r) > 2 else "", r[0]): r[1] for r in csv.reader(CSV.open()) if r} if CSV.exists() else {}
	fertig, fehlend = set(), {}
	for app, repo in APPS.items():
		for e in katalog(app, repo):
			if e.obsolete:
				continue
			schluessel = (e.msgctxt or "", e.msgid)
			if e.translated():
				fertig.add(schluessel)
			elif schluessel not in eigene:
				fehlend[schluessel] = {"ctx": e.msgctxt, "id": e.msgid}
	fehlend = {k: v for k, v in fehlend.items() if k not in fertig}
	behalten = {k: v for k, v in eigene.items() if k not in fertig}
	with CSV.open("w", newline="") as f:
		w = csv.writer(f, lineterminator="\n")
		for (ctx, quelle), ziel in sorted(behalten.items(), key=lambda x: x[0][1].lower()):
			w.writerow([quelle, ziel, ctx] if ctx else [quelle, ziel])
	ziel = pathlib.Path(__file__).parent / "fehlend.json"
	ziel.write_text(json.dumps(list(fehlend.values()), ensure_ascii=False, indent=1))
	print(f"{len(eigene) - len(behalten)} entfernt (jetzt in der App übersetzt), {len(behalten)} bleiben, {len(fehlend)} neu fehlend → {ziel.name}")


if __name__ == "__main__":
	main()
