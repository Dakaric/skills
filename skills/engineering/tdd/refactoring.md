# Refactor-Kandidaten

Nach dem TDD-Zyklus schau nach:

- **Duplikation** → Function / Class extrahieren
- **Lange Methoden** → in Private Helpers aufbrechen (Tests bleiben am Public Interface)
- **Shallow Modules** → kombinieren oder deepenen
- **Feature Envy** → Logic dahin verschieben, wo die Daten leben
- **Primitive Obsession** → Value Objects einführen
- **Bestehender Code**, den der neue Code als problematisch offenlegt
