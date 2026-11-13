// Startseite: Beim ersten Öffnen der Kachelseite in einem Tab zum Standard-Arbeitsbereich
// des Benutzers springen (Benutzer → Standard-Arbeitsbereich). Danach bleibt die Kachelseite
// über das Logo erreichbar.
(() => {
	const zuStart = () => {
		const ws = frappe.boot?.user?.default_workspace?.name;
		if (!ws || !["/", "/desk", "/desk/"].includes(location.pathname)) return;
		try {
			if (sessionStorage.getItem("dd_start")) return;
			sessionStorage.setItem("dd_start", "1");
		} catch (e) {}
		location.replace("/desk/" + frappe.router.slug(ws));
	};
	$(document).on("startup", zuStart);
})();
