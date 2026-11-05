(() => {
  const storageKey = "study-studio-theme";
  let saved = null;
  try { saved = localStorage.getItem(storageKey); } catch (_) {}
  const systemPrefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  const applyTheme = (theme) => {
    document.documentElement.dataset.theme = theme;
    const toggle = document.getElementById("theme-toggle");
    if (!toggle) return;
    const dark = theme === "dark";
    toggle.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
    toggle.setAttribute("aria-pressed", String(dark));
    toggle.title = dark ? "Switch to light mode" : "Switch to dark mode";
    const glyph = toggle.querySelector(".theme-glyph");
    const label = toggle.querySelector(".theme-label");
    if (glyph) glyph.textContent = dark ? "☀" : "☾";
    if (label) label.textContent = dark ? "Light mode" : "Dark mode";
  };
  applyTheme(saved || (systemPrefersDark ? "dark" : "light"));
  document.getElementById("theme-toggle")?.addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem(storageKey, next); } catch (_) {}
    applyTheme(next);
  });
})();
