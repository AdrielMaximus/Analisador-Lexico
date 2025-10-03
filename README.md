# 🐍 Lexical Analyzer (Lexer) Project 🔎

Uma ferramenta educativa para analisar código C e transformá-lo em **tokens**! 💻✨

---

## 🇧🇷 Português

### ✨ Visão Geral do Projeto
Este é um **Analisador Léxico (Lexer)** simples, desenvolvido em **Python 🐍** com interface gráfica usando **Tkinter**.  
Ele atua como a primeira etapa de um compilador, lendo código-fonte C (`.c`) e transformando-o em uma lista estruturada de **Tokens**.

### 🛠️ Componentes Principais

| Componente | Função | Emoji |
|------------|--------|-------|
| `token_specs` | Define todas as regras (Regex) e seus rótulos (`NUM_INT`, `PLUS`, etc.) | 🏷️ |
| `master_regex` | Super-regra compilada que varre o código de forma eficiente | 🚀 |
| `lexer(code)` | Função central que reconhece, processa e descarta caracteres (como `SKIP`) | 🧠 |
| `LexicalAnalyzerApp` | Interface gráfica (GUI) para carregar arquivos e exibir o resultado | 🖥️ |

### ▶️ Como Executar

**Requisitos:**  
- Python 3.x  
- Tkinter instalado

**Execução:**  

python seu_analisador.py
Análise:

Clique em "Abrir Arquivo .c"

Selecione o arquivo desejado

Clique em "Iniciar Análise Léxica" para ver os tokens na caixa de texto

🧩 Tokens Reconhecidos
Tipos e Palavras-chave: INT, IF, WHILE

Dados: NUM_INT, NUM_FLOAT

Estrutura: ASSIGN (=), PLUS (+), SEMI (;), LPAREN (() )

Tratamento de Erros: qualquer caractere não reconhecido gera MISMATCH



🇺🇸 English
✨ Project Overview
This is a simple Lexical Analyzer (Lexer) built in Python 🐍 with a Tkinter GUI.
It works as the first stage of a compiler, reading C source code (.c) and converting it into a structured list of Tokens.

🛠️ Core Components
Component	Function	Emoji
token_specs	Defines all rules (Regex) and labels (NUM_INT, PLUS, etc.)	🏷️
master_regex	Compiled super-rule that efficiently scans the code	🚀
lexer(code)	Core function that recognizes, processes, and discards characters (like SKIP)	🧠
LexicalAnalyzerApp	GUI to load files and display output	🖥️

▶️ How to Run
Requirements:

Python 3.x

Tkinter installed

Execution:

python your_analyzer.py
Analysis:

Click "Open .c File"

Select a file

Click "Start Lexical Analysis" to see the tokens in the text box

🧩 Recognized Tokens
Types and Keywords: INT, IF, WHILE

Data: NUM_INT, NUM_FLOAT

Structure: ASSIGN (=), PLUS (+), SEMI (;), LPAREN (() )

Error Handling: any unrecognized character triggers a MISMATCH

🇩🇪 Deutsch
✨ Projektübersicht
Dies ist ein einfacher Lexikalischer Analysator (Lexer) in Python 🐍 mit einer Tkinter-GUI.
Er fungiert als erste Stufe eines Compilers, liest C-Quellcode (.c) und wandelt ihn in eine strukturierte Liste von Tokens um.

🛠️ Hauptkomponenten
Komponente	Funktion	Emoji
token_specs	Definiert alle Regeln (Regex) und Labels (GANZE_ZAHL, PLUS, etc.)	🏷️
master_regex	Kompilierte Super-Regel, die den Code effizient scannt	🚀
lexer(code)	Kernfunktion, die Zeichen erkennt, verarbeitet und verwirft (wie UEBERSPRINGEN)	🧠
LexicalAnalyzerApp	GUI zum Laden von Dateien und Anzeigen der Ausgabe	🖥️

▶️ Ausführung
Voraussetzungen:

Python 3.x

Tkinter installiert

Ausführung:


python ihr_analysator.py
Analyse:

Klicken Sie auf "C-Datei öffnen"

Datei auswählen

Klicken Sie auf "Lexikalische Analyse starten", um die Tokens im Textfeld zu sehen

🧩 Erkannte Tokens
Typen und Schlüsselwörter: INT, IF, WHILE

Daten: GANZE_ZAHL, GLEITKOMMA_ZAHL

Struktur: ZUWEISUNG (=), PLUS (+), SEMICOLON (;), LINKSPARENTHESE (() )

Fehlerbehandlung: jedes nicht erkannte Zeichen löst eine FEHLANPASSUNG aus