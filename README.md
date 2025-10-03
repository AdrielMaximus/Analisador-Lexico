

🐍 Lexical Analyzer (Lexer) Project 🔎
🇧🇷 Português
✨ Visão Geral do Projeto
Este é um Analisador Léxico (Lexer) simples, construído em Python 🐍 com uma Interface Gráfica (GUI) em Tkinter. Ele funciona como a primeira etapa de um compilador, lendo o código-fonte C (.c) e o transformando em uma lista estruturada de Tokens.

🛠️ Componentes Principais
Componente	Função	Emoji
token_specs	Define todas as regras (Regex) e seus rótulos (NUM_INT, PLUS).	🏷️
master_regex	A Super-Regra compilada que varre o código de forma eficiente.	🚀
lexer(code)	A função central que reconhece, processa e descarta (como SKIP) os caracteres.	🧠
LexicalAnalyzerApp	A interface gráfica (GUI) para carregar arquivos e exibir a saída.	🖥️
▶️ Como Executar
Para colocar este analisador em funcionamento, siga os passos:

Requisitos: Certifique-se de ter o Python 3.x e o Tkinter instalados.

Execução: Salve o código e rode-o diretamente:

*python seu_analisador.py*


Análise: Clique em "Abrir Arquivo .c", selecione um arquivo, e então clique em "Iniciar Análise Léxica" para ver o resultado na caixa de texto.

🧩 Tokens Reconhecidos
O analisador traduz o código em pares (TIPO, VALOR), reconhecendo:

Tipos e Palavras-chave: INT, IF, WHILE

Dados: NUM_INT, NUM_FLOAT

Estrutura: ASSIGN (=), PLUS (+), SEMI (;), LPAREN (()

Tratamento de Erros: Qualquer caractere não reconhecido gera um MISMATCH.

🇺🇸 English
✨ Project Overview
This is a simple Lexical Analyzer (Lexer), built in Python 🐍 with a Graphical User Interface (GUI) using Tkinter. It functions as the first stage of a compiler, reading C source code (.c) and transforming it into a structured list of Tokens.

🛠️ Core Components
Component	Function	Emoji
token_specs	Defines all rules (Regex) and their labels (NUM_INT, PLUS).	🏷️
master_regex	The compiled Super-Rule that efficiently scans the code.	🚀
lexer(code)	The central function that recognizes, processes, and discards (like SKIP) characters.	🧠
LexicalAnalyzerApp	The GUI for loading files and displaying the output.	🖥️
▶️ How to Run
To get this analyzer running, follow these steps:

Requirements: Ensure you have Python 3.x and Tkinter installed.

Execution: Save the code and run it directly:


*python your_analyzer.py*

Analysis: Click "Open .c File", select a file, and then click "Start Lexical Analysis" to see the output in the text box.

🧩 Recognized Tokens
The analyzer translates the code into (TYPE, VALUE) pairs, recognizing:

Types and Keywords: INT, IF, WHILE

Data: NUM_INT, NUM_FLOAT

Structure: ASSIGN (=), PLUS (+), SEMI (;), LPAREN (()

Error Handling: Any unrecognized character throws a MISMATCH.

🇩🇪 Deutsch
✨ Projektübersicht
Dies ist ein einfacher Lexikalischer Analysator (Lexer), der in Python 🐍 mit einer Grafischen Benutzeroberfläche (GUI) unter Verwendung von Tkinter erstellt wurde. Er fungiert als erste Stufe eines Compilers, indem er C-Quellcode (.c) liest und diesen in eine strukturierte Liste von Tokens umwandelt.

🛠️ Hauptkomponenten
Komponente	Funktion	Emoji
token_spezifikationen	Definiert alle Regeln (Regex) und ihre Labels (GANZE_ZAHL, PLUS).	🏷️
master_regex	Die kompilierte Super-Regel, die den Code effizient scannt.	🚀
lexer(code)	Die zentrale Funktion, die Zeichen erkennt, verarbeitet und verwirft (wie UEBERSPRINGEN).	🧠
LexikalischerAnalysatorApp	Die GUI zum Laden von Dateien und Anzeigen der Ausgabe.	🖥️
▶️ Ausführung
Um diesen Analysator auszuführen, folgen Sie diesen Schritten:

Voraussetzungen: Stellen Sie sicher, dass Python 3.x und Tkinter installiert sind.

Ausführung: Speichern Sie den Code und führen Sie ihn direkt aus:



*python ihr_analysator.py*


Analyse: Klicken Sie auf "C-Datei öffnen", wählen Sie eine Datei aus und klicken Sie dann auf "Lexikalische Analyse starten", um die Ausgabe im Textfeld zu sehen.

🧩 Erkannte Tokens
Der Analysator übersetzt den Code in (TYP, WERT)-Paare und erkennt:

Typen und Schlüsselwörter: INT, IF, WHILE

Daten: GANZE_ZAHL, GLEITKOMMA_ZAHL

Struktur: ZUWEISUNG (=), PLUS (+), SEMICOLON (;), LINKSPARENTHESE (()

Fehlerbehandlung: Jedes nicht erkannte Zeichen löst eine FEHLANPASSUNG aus.