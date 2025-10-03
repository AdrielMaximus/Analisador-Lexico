import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# -----------------------------
# 1. Token-Definitionen (Liste enthält Token-Namen und ihre zugehörigen Regex-Muster)
# -----------------------------
token_spezifikationen = [
    ("GLEITKOMMA_ZAHL", r'\d+\.\d+'), # Gleitkommazahl (Float Number)
    ("GANZE_ZAHL",      r'\d+'),      # Ganze Zahl (Integer)
    ("ID",              r'[a-zA-Z_]\w*'), # Bezeichner (Identifier)
    ("ZUWEISUNG",       r'='),        # Zuweisungsoperator (Assignment Operator)
    ("GLEICHHEIT",      r'=='),       # Gleichheitsoperator (Equality Operator)
    ("PLUS",            r'\+'),       # Additionsoperator
    ("MINUS",           r'-'),        # Subtraktionsoperator
    ("MAL",             r'\*'),       # Multiplikationsoperator
    ("GETEILT",         r'/'),        # Divisionsoperator
    ("KLEINER_ALS",     r'<'),        # Kleiner-als Operator
    ("GROESSER_ALS",    r'>'),        # Größer-als Operator
    ("LINKSPARENTHESE", r'\('),     # Linke Klammer
    ("RECHTSPARENTHESE", r'\)'),    # Rechte Klammer
    ("LINKE_GESCHWEIFTE_KLAMMER", r'\{'), # Linke geschweifte Klammer
    ("RECHTE_GESCHWEIFTE_KLAMMER", r'\}'), # Rechte geschweifte Klammer
    ("SEMICOLON",       r';'),        # Semikolon
    ("UEBERSPRINGEN",   r'[ \t]+'),   # Leerzeichen/Tabs (wird übersprungen)
    ("NEUE_ZEILE",      r'\n'),       # Zeilenumbruch
    ("FEHLANPASSUNG",   r'.'),        # Nicht übereinstimmender Token (Fehler)
]
# -----------------------------
# Transforma o regex (z.B. ("MINUS", r'-')) in eine benannte Erfassungsgruppe (z.B. (?P<MINUS>{'-'})).
# Dies ist ein spezielles Format für die 're'-Bibliothek, das als Label für jede Regel dient.
# -----------------------------
regex_teile = []
for name, regex in token_spezifikationen:
    regex_teile.append(f"(?P<{name}>{regex})")
# Kompiliert alle Regeln in einen einzigen Master-Regex: (Regel a) | (Regel b) | ...
master_regex = re.compile("|".join(regex_teile))

# -----------------------------
# 2. Lexer-Funktion (Lexikalischer Analysator)
# -----------------------------
def lexer(code):
    tokens = []
    zeilen_nr = 1
    for match in master_regex.finditer(code): # DURCHSUCHT DEN GESAMTEN CODE
        kind = match.lastgroup # Extrahiert den Namen des passenden Labels
        value = match.group()  # Extrahiert den Wert des passenden Labels
        
        if kind == "GANZE_ZAHL":
            tokens.append((kind, int(value)))
        elif kind == "GLEITKOMMA_ZAHL":
            tokens.append((kind, float(value)))
        elif kind == "ID":
            # Prüft auf reservierte Schlüsselwörter
            if value in ("int", "float", "if", "else", "while"):
                tokens.append((value.upper(), value))
            else:
                tokens.append((kind, value))
        elif kind == "NEUE_ZEILE":
            zeilen_nr += 1
        elif kind == "UEBERSPRINGEN":
            continue # Ignoriert Leerzeichen
        elif kind == "FEHLANPASSUNG":
            # Löst einen Fehler für nicht erkannte Zeichen aus
            raise RuntimeError(f"Ungültiger Token '{value}' in Zeile {zeilen_nr}")
        else:
            tokens.append((kind, value))
    return tokens

# -----------------------------
# 3. Grafische Benutzeroberfläche (GUI)
# -----------------------------
class LexikalischerAnalysatorApp:
    def __init__(self, root):
        self.root = root # Speichert eine Referenz zum Haupt-Tkinter-Fenster
        self.root.title("Lexikalischer Analysator - C-Dateien")
        self.dateipfad = None
        self.datei_inhalt = None

        # Haupt-Schaltflächen
        self.oeffnen_schaltflaeche = tk.Button(root, text="C-Datei öffnen", command=self.datei_oeffnen)
        self.oeffnen_schaltflaeche.pack(pady=10)

        self.analyse_schaltflaeche = tk.Button(root, text="Lexikalische Analyse starten", command=self.analyse_starten, state=tk.DISABLED)
        self.analyse_schaltflaeche.pack(pady=10)

        self.schliessen_schaltflaeche = tk.Button(root, text="Schließen", command=root.quit)
        self.schliessen_schaltflaeche.pack(pady=10)

        # Textfeld zur Anzeige der Tokens
        self.ausgabe_bereich = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
        self.ausgabe_bereich.pack(pady=10)

    def datei_oeffnen(self):
        dateitypen = [("C-Dateien", "*.c")]
        self.dateipfad = filedialog.askopenfilename(title="Wählen Sie eine C-Datei aus", filetypes=dateitypen)

        if self.dateipfad:
            with open(self.dateipfad, "r", encoding="utf-8") as f:
                self.datei_inhalt = f.read()
            messagebox.showinfo("Datei geöffnet", f"Ausgewählte Datei: {self.dateipfad}")
            self.analyse_schaltflaeche.config(state=tk.NORMAL)

    def analyse_starten(self):
        if not self.datei_inhalt:
            messagebox.showwarning("Warnung", "Keine Datei geöffnet.")
            return

        try:
            tokens = lexer(self.datei_inhalt)
            self.ausgabe_bereich.config(state=tk.NORMAL)
            self.ausgabe_bereich.delete(1.0, tk.END)
            for token in tokens:
                self.ausgabe_bereich.insert(tk.END, f"{token}\n")
            self.ausgabe_bereich.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Fehler", str(e))


# -----------------------------
# 4. Ausführung
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LexikalischerAnalysatorApp(root)
    root.mainloop()