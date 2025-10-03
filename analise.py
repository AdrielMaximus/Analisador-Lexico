import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# -----------------------------
# 1. Token Definitions (List contains token names and their respective regex)
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
    ("LT",        r'<'), # Less Than
    ("GT",        r'>'), # Greater Than
    ("LPAREN",    r'\('), # Left Parenthesis
    ("RPAREN",    r'\)'), # Right Parenthesis
    ("LBRACE",    r'\{'), # Left Brace
    ("RBRACE",    r'\}'), # Right Brace
    ("SEMI",      r';'), # Semicolon
    ("SKIP",      r'[ \t]+'), # Spaces and Tabs (to be skipped)
    ("NEWLINE",   r'\n'), # Newline
    ("MISMATCH",  r'.'), # Any other character (error)
]
# -----------------------------
# Transforms the regex (e.g., ("MINUS", r'-')) into a named capture group (e.g., (?P<MINUS>{'-'}))
# This special format is used by the 're' library to label each rule.
# -----------------------------
regex_parts = []
for name, regex in token_specs:
    regex_parts.append(f"(?P<{name}>{regex})")
# Compiles all rules into a single master regex: (rule a) | (rule b) | ...
master_regex = re.compile("|".join(regex_parts))

# -----------------------------
# 2. Lexical Analyzer Function
# -----------------------------
def lexer(code):
    tokens = []
    line_num = 1
    for match in master_regex.finditer(code): # SCANS THE ENTIRE CODE
        kind = match.lastgroup # Extracts the name of the compatible label (kind)
        value = match.group()  # Extracts the value of the compatible label (value)
        
        if kind == "NUM_INT":
            tokens.append((kind, int(value)))
        elif kind == "NUM_FLOAT":
            tokens.append((kind, float(value)))
        elif kind == "ID":
            # Checks for reserved keywords
            if value in ("int", "float", "if", "else", "while"):
                tokens.append((value.upper(), value))
            else:
                tokens.append((kind, value))
        elif kind == "NEWLINE":
            line_num += 1
        elif kind == "SKIP":
            continue # Ignores whitespace
        elif kind == "MISMATCH":
            # Raises an error for any unrecognized character
            raise RuntimeError(f"Invalid token '{value}' on line {line_num}")
        else:
            tokens.append((kind, value))
    return tokens

# -----------------------------
# 3. Graphical Interface (GUI)
# -----------------------------
class LexicalAnalyzerApp:
    def __init__(self, root):
        self.root = root # Stores a reference to the main Tkinter window
        self.root.title("Lexical Analyzer - C Files")
        self.file_path = None
        self.file_content = None

        # Main buttons
        self.open_button = tk.Button(root, text="Open .c File", command=self.open_file)
        self.open_button.pack(pady=10)

        self.analyze_button = tk.Button(root, text="Start Lexical Analysis", command=self.start_analysis, state=tk.DISABLED)
        self.analyze_button.pack(pady=10)

        self.close_button = tk.Button(root, text="Close", command=root.quit)
        self.close_button.pack(pady=10)

        # Text box to display tokens
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
        self.output_area.pack(pady=10)

    def open_file(self):
        filetypes = [("C Files", "*.c")]
        self.file_path = filedialog.askopenfilename(title="Select a .c file", filetypes=filetypes)

        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.file_content = f.read()
            messagebox.showinfo("File Opened", f"Selected file: {self.file_path}")
            self.analyze_button.config(state=tk.NORMAL)

    def start_analysis(self):
        if not self.file_content:
            messagebox.showwarning("Warning", "No file opened.")
            return

        try:
            tokens = lexer(self.file_content)
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete(1.0, tk.END)
            for token in tokens:
                self.output_area.insert(tk.END, f"{token}\n")
            self.output_area.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))


# -----------------------------
# 4. Execution
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerApp(root)
    root.mainloop()