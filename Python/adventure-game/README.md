# Übungsaufgabe: Textbasiertes Abenteuer "Die verlorene Schatzsuche"

## Aufgabenstellung

Entwickle ein textbasiertes Abenteuerspiel namens **"Die verlorene Schatzsuche"**, bei dem der Spieler durch verschiedene Räume navigiert, Rätsel löst und letztendlich den Schatz findet. Das Ziel dieser Übung ist es, die Vorteile von Funktionen und das Auslagern von Code in externe Dateien kennenzulernen.

## Anforderungen

1. ### Funktionen verwenden
   - **Erstelle Funktionen** für die folgenden Aufgaben:
     - `greeting()`: Begrüßt den Spieler und erklärt die Spielregeln.
     - `enter_room(room)`: Beschreibt den aktuellen Raum und die verfügbaren Aktionen.
     - `solve_riddle(riddle)`: Präsentiert ein Rätsel und überprüft die Antwort des Spielers.
     - `end_game()`: Verabschiedet sich vom Spieler und beendet das Spiel.

2. ### Code auslagern
   - **Lagere die Funktionen** `solve_riddle(riddle)` und `end_game()` in eine externe Python-Datei namens `game_utils.py` aus.
   - **Importiere diese Funktionen** in dein Hauptprogramm.

3. ### Spielstruktur
   - Das Spiel besteht aus **mindestens drei verschiedenen Räumen**.
   - Jeder Raum enthält ein **einzigartiges Rätsel**, das gelöst werden muss, um weiterzukommen.
   - Der Spieler kann durch Eingabe von Befehlen wie `"norden"`, `"süden"`, `"osten"`, `"westen"` navigieren.
   - Wenn der Spieler den Schatz gefunden hat, soll das Spiel eine entsprechende Nachricht ausgeben und enden.

4. ### Interaktive Elemente
   - Implementiere eine **einfache Eingabeaufforderung**, die die Aktionen des Spielers entgegennimmt.
   - Verarbeite die Eingaben und führe die entsprechenden Funktionen aus.

## Optionale Erweiterungen

- Füge ein **Inventarsystem** hinzu, in dem der Spieler Gegenstände sammeln und verwenden kann.
- Implementiere ein **einfaches Punktesystem**, das die Leistung des Spielers bewertet.
- Erstelle **zusätzliche Räume und Rätsel**, um das Spiel umfangreicher zu gestalten.

## Hinweise

- Achte auf eine **saubere und übersichtliche Code-Struktur**.
- Verwende **aussagekräftige Funktions- und Variablennamen** (auf Englisch).
- **Kommentiere deinen Code**, um die Funktionsweise zu erklären.
- **Teste dein Spiel** ausgiebig, um sicherzustellen, dass alle Funktionen korrekt arbeiten.

## Ziel der Übung

Durch diese Aufgabe lernst du:

- Wie **Funktionen** dazu beitragen, deinen Code übersichtlicher und wiederverwendbar zu machen.
- Wie du Code in **externe Dateien auslagern** und in deinem Hauptprogramm verwenden kannst.
- Wie du ein **interaktives Programm** entwickelst, das Benutzereingaben verarbeitet.

---

**Viel Spaß beim Programmieren und auf zur Schatzsuche!**