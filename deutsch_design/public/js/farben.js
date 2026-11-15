// Farben: Firmenfarbe bzw. eigene Farbe des Benutzers (Design Einstellungen) für Hauptknöpfe
// und den aktiven Eintrag der Seitenleiste.
$(document).on("startup", () => {
	const f = frappe.boot.dd_farbe;
	if (!/^#[0-9a-f]{3,8}$/i.test(f || "")) return;
	const css = document.createElement("style");
	css.textContent = `
		:root { --brand-color: ${f}; }
		.es-button[data-variant="solid"]:not([data-theme]):not(.btn-danger),
		.es-button.btn-primary {
			--bt-solid-bg: ${f};
			--bt-solid-bg-hover: color-mix(in srgb, ${f} 85%, black);
			--bt-solid-bg-active: color-mix(in srgb, ${f} 75%, black);
			--bt-solid-fg: #fff;
		}
		.standard-sidebar-item.active-sidebar { box-shadow: inset 3px 0 0 ${f}; }
		.standard-sidebar-item.active-sidebar .sidebar-item-label,
		.standard-sidebar-item.active-sidebar svg { color: ${f}; }`;
	document.head.appendChild(css);
});
