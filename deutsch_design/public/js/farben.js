// Farben: Firmenfarbe bzw. eigene Farbe des Benutzers (Design Einstellungen) für Knöpfe,
// Hervorhebungen und die aktive Seitenleiste.
$(document).on("startup", () => {
	const farbe = frappe.boot.dd_farbe;
	if (!farbe) return;
	for (const v of ["--primary", "--brand-color", "--btn-primary", "--primary-color"])
		document.documentElement.style.setProperty(v, farbe);
});
