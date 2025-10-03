import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# -----------------------------
# 1. Definição dos TOKENS
# -----------------------------
token_specs = [
    ("NUM_FLOAT", r'\d+\.\d+'),
    ("NUM_INT",   r'\d+'),
    ("ID",        r'[a-zA-Z_]\w*'),
    ("ASSIGN",    r'='),
    ("EQ",        r'=='),
    ("PLUS",      r'\+'),
    ("MINUS",     r'-'),
    ("MUL",       r'\*'),
    ("DIV",       r'/'),
    ("LT",        r'<'),
    ("GT",        r'>'),
    ("LPAREN",    r'\('),
    ("RPAREN",    r'\)'),
    ("LBRACE",    r'\{'),
    ("RBRACE",    r'\}'),
    ("SEMI",      r';'),
    ("SKIP",      r'[ \t]+'),
    ("NEWLINE",   r'\n'),
    ("MISMATCH",  r'.'),
]

regex_parts = []
for name, regex in token_specs:
    regex_parts.append(f"(?P<{name}>{regex})")
master_regex = re.compile("|".join(regex_parts))

# -----------------------------
# 2. Função do analisador léxico
# -----------------------------
def lexer(code):
    tokens = []
    line_num = 1
    for match in master_regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == "NUM_INT":
            tokens.append((kind, int(value)))
        elif kind == "NUM_FLOAT":
            tokens.append((kind, float(value)))
        elif kind == "ID":
            if value in ("int", "float", "if", "else", "while"):
                tokens.append((value.upper(), value))
            else:
                tokens.append((kind, value))
        elif kind == "NEWLINE":
            line_num += 1
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Token inválido '{value}' na linha {line_num}")
        else:
            tokens.append((kind, value))
    return tokens

# -----------------------------
# 3. Interface Gráfica
# -----------------------------
class LexicalAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador Léxico - Arquivos C")
        self.file_path = None
        self.file_content = None

        # Botões principais
        self.open_button = tk.Button(root, text="Abrir Arquivo .c", command=self.open_file)
        self.open_button.pack(pady=10)

        self.analyze_button = tk.Button(root, text="Iniciar Análise Léxica", command=self.start_analysis, state=tk.DISABLED)
        self.analyze_button.pack(pady=10)

        self.close_button = tk.Button(root, text="Fechar", command=root.quit)
        self.close_button.pack(pady=10)

        # Caixa de texto para exibir tokens
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
        self.output_area.pack(pady=10)

    def open_file(self):
        filetypes = [("Arquivos C", "*.c")]
        self.file_path = filedialog.askopenfilename(title="Selecione um arquivo .c", filetypes=filetypes)

        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.file_content = f.read()
            messagebox.showinfo("Arquivo Aberto", f"Arquivo selecionado: {self.file_path}")
            self.analyze_button.config(state=tk.NORMAL)

    def start_analysis(self):
        if not self.file_content:
            messagebox.showwarning("Aviso", "Nenhum arquivo aberto.")
            return

        try:
            tokens = lexer(self.file_content)
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete(1.0, tk.END)
            for token in tokens:
                self.output_area.insert(tk.END, f"{token}\n")
            self.output_area.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Erro", str(e))


# -----------------------------
# 4. Execução
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerApp(root)
    root.mainloop()
