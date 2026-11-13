import frappe


def boot(bootinfo):
	"""Farbe für den Desk: eigene Farbe des Benutzers, sonst Firmenfarbe."""
	try:
		e = frappe.get_cached_doc("Design Einstellungen")
	except Exception:
		return  # Doctype noch nicht angelegt (vor der Migration)
	eigene = next((z.farbe for z in e.benutzerfarben if z.benutzer == frappe.session.user), None)
	bootinfo.dd_farbe = eigene or e.firmenfarbe
