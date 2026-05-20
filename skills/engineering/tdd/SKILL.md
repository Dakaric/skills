---
name: tdd
description: Test-driven Development mit Red-Green-Refactor Loop. Nutze, wenn der User Features bauen oder Bugs fixen will mit TDD, "red-green-refactor" erwähnt, Integration-Tests will oder nach Test-First-Entwicklung fragt.
---

# Test-Driven Development

## Philosophie

**Kernprinzip**: Tests sollten Verhalten durch öffentliche Interfaces verifizieren, nicht Implementierungsdetails. Code kann komplett wechseln; Tests sollten das nicht.

**Gute Tests** sind integration-style: sie üben echte Code-Pfade durch Public APIs aus. Sie beschreiben _was_ das System tut, nicht _wie_ es das tut. Ein guter Test liest sich wie eine Spezifikation - "User kann mit validem Cart einchecken" sagt dir exakt, welche Capability existiert. Diese Tests überleben Refactors, weil sie sich nicht um interne Struktur scheren.

**Schlechte Tests** sind an die Implementation gekoppelt. Sie mocken interne Collaborators, testen Private Methods oder verifizieren über externe Wege (z.B. direkte Datenbank-Queries statt das Interface zu nutzen). Das Warnsignal: dein Test bricht, wenn du refaktorierst, aber das Verhalten hat sich nicht geändert. Wenn du eine interne Function umbenennst und Tests failen, haben die Tests Implementation getestet, nicht Verhalten.

Siehe [tests.md](tests.md) für Beispiele und [mocking.md](mocking.md) für Mocking-Guidelines.

## Anti-Pattern: Horizontal Slices

**SCHREIB NICHT alle Tests zuerst und dann die ganze Implementation.** Das ist "Horizontal Slicing" - RED als "alle Tests schreiben" und GREEN als "den ganzen Code schreiben" behandeln.

Das produziert **Crap-Tests**:

- Tests, die in Bulk geschrieben werden, testen _imaginiertes_ Verhalten, nicht _echtes_ Verhalten
- Du landest dabei, die _Form_ der Dinge zu testen (Datenstrukturen, Function-Signaturen) statt user-gerichteten Verhaltens
- Tests werden insensitiv gegenüber echten Änderungen - sie passen, wenn Verhalten kaputtgeht, sie failen, wenn alles passt
- Du fährst über deine Scheinwerfer hinaus und commitst dich auf Test-Struktur, bevor du die Implementation verstanden hast

**Richtiger Ansatz**: Vertical Slices per Tracer Bullets. Ein Test → eine Implementation → wiederholen. Jeder Test reagiert auf das, was du im vorherigen Zyklus gelernt hast. Weil du gerade den Code geschrieben hast, weißt du genau, welches Verhalten wichtig ist und wie du es verifizierst.

```
FALSCH (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RICHTIG (vertikal):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## Workflow

### 1. Planning

Beim Codebase-Explore das Domain-Glossar des Projekts nutzen, damit Test-Namen und Interface-Vokabular zur Projektsprache passen, und ADRs im betroffenen Bereich respektieren.

Bevor irgendein Code geschrieben wird:

- [ ] Mit dem User bestätigen, welche Interface-Änderungen nötig sind
- [ ] Mit dem User bestätigen, welche Behaviors getestet werden (priorisieren)
- [ ] Gelegenheiten für [deep modules](deep-modules.md) identifizieren (kleines Interface, tiefe Implementation)
- [ ] Interfaces für [Testbarkeit](interface-design.md) designen
- [ ] Die zu testenden Behaviors listen (nicht Implementation-Schritte)
- [ ] Plan-Approval vom User holen

Frag: "Wie sollte das Public Interface aussehen? Welche Behaviors sind am wichtigsten zu testen?"

**Du kannst nicht alles testen.** Mit dem User bestätigen, welche Behaviors wirklich wichtig sind. Test-Aufwand auf Critical Paths und komplexe Logic fokussieren, nicht jeden möglichen Edge Case.

### 2. Tracer Bullet

Schreib EINEN Test, der EINE Sache am System bestätigt:

```
RED:   Test für erstes Behavior schreiben → Test failed
GREEN: Minimalen Code zum Bestehen schreiben → Test passed
```

Das ist dein Tracer Bullet - beweist, dass der Pfad end-to-end funktioniert.

### 3. Inkrementeller Loop

Für jedes verbleibende Behavior:

```
RED:   Nächsten Test schreiben → failed
GREEN: Minimaler Code zum Bestehen → passed
```

Regeln:

- Ein Test auf einmal
- Nur genug Code, um den aktuellen Test zu bestehen
- Antizipier keine zukünftigen Tests
- Tests fokussiert auf beobachtbares Verhalten halten

### 4. Refactor

Nachdem alle Tests passen, schau nach [Refactor-Kandidaten](refactoring.md):

- [ ] Duplikation extrahieren
- [ ] Module deepenen (Komplexität hinter einfache Interfaces verschieben)
- [ ] SOLID-Prinzipien anwenden, wo natürlich
- [ ] Überlegen, was neuer Code über bestehenden Code offenlegt
- [ ] Tests nach jedem Refactor-Schritt laufen lassen

**Niemals refaktorieren, während du RED bist.** Erst auf GREEN kommen.

## Checkliste pro Zyklus

```
[ ] Test beschreibt Behavior, nicht Implementation
[ ] Test nutzt nur das Public Interface
[ ] Test würde einen internen Refactor überleben
[ ] Code ist minimal für diesen Test
[ ] Keine spekulativen Features hinzugefügt
```
