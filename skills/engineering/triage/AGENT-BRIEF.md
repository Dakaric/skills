# Agent Briefs schreiben

Ein Agent Brief ist ein strukturierter Comment, der auf einem GitHub Issue gepostet wird, wenn es zu `ready-for-agent` wechselt. Es ist die autoritative Spezifikation, mit der ein AFK Agent arbeitet. Der ursprüngliche Issue-Body und die Diskussion sind Kontext - der Agent Brief ist der Vertrag.

## Prinzipien

### Durability vor Precision

Das Issue kann tagelang oder wochenlang in `ready-for-agent` liegen. Die Codebase ändert sich in der Zwischenzeit. Schreib den Brief so, dass er nützlich bleibt, auch wenn Files umbenannt, verschoben oder refaktoriert werden.

- **Tu** Interfaces, Typen und Behavioral Contracts beschreiben
- **Tu** spezifische Typen, Function-Signaturen oder Config-Formen benennen, nach denen der Agent suchen oder die er ändern soll
- **Tu nicht** File-Pfade referenzieren - die werden stale
- **Tu nicht** Zeilennummern referenzieren
- **Tu nicht** annehmen, dass die aktuelle Implementation-Struktur gleich bleibt

### Behavioral, not procedural

Beschreib, **was** das System tun soll, nicht **wie** es zu implementieren ist. Der Agent wird die Codebase frisch erkunden und seine eigenen Implementation-Entscheidungen treffen.

- **Gut:** "Der `SkillConfig`-Typ sollte ein optionales `schedule`-Feld vom Typ `CronExpression` akzeptieren"
- **Schlecht:** "Öffne src/types/skill.ts und füg ein schedule-Feld in Zeile 42 hinzu"
- **Gut:** "Wenn ein User `/triage` ohne Argumente ausführt, sollte er eine Zusammenfassung der Issues sehen, die Aufmerksamkeit brauchen"
- **Schlecht:** "Füg ein switch-Statement in die main-Handler-Funktion ein"

### Vollständige Acceptance Criteria

Der Agent muss wissen, wann er fertig ist. Jeder Agent Brief braucht konkrete, testbare Acceptance Criteria. Jedes Kriterium sollte unabhängig verifizierbar sein.

- **Gut:** "`gh issue list --label needs-triage` ausführen liefert Issues zurück, die die initiale Klassifizierung durchlaufen haben"
- **Schlecht:** "Triage sollte korrekt funktionieren"

### Explizite Scope Boundaries

Sag, was out of scope ist. Das verhindert, dass der Agent goldplated oder Annahmen über benachbarte Features trifft.

## Template

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** Ein-Zeilen-Beschreibung, was passieren soll

**Current behavior:**
Beschreib, was jetzt passiert. Bei Bugs ist das das kaputte Verhalten.
Bei Enhancements ist das der Status Quo, auf dem das Feature aufbaut.

**Desired behavior:**
Beschreib, was passieren soll, nachdem die Arbeit des Agents abgeschlossen ist.
Sei spezifisch bei Edge Cases und Error Conditions.

**Key interfaces:**
- `TypeName` — was sich ändern muss und warum
- `functionName()` Return-Typ — was er aktuell zurückgibt vs. was er zurückgeben sollte
- Config-Shape — alle neuen Konfigurationsoptionen, die nötig sind

**Acceptance criteria:**
- [ ] Spezifisches, testbares Kriterium 1
- [ ] Spezifisches, testbares Kriterium 2
- [ ] Spezifisches, testbares Kriterium 3

**Out of scope:**
- Dinge, die in diesem Issue NICHT geändert oder adressiert werden sollen
- Benachbartes Feature, das verwandt scheint, aber separat ist
```

## Beispiele

### Guter Agent Brief (Bug)

```markdown
## Agent Brief

**Category:** bug
**Summary:** Skill-Description-Truncation bricht mitten im Wort ab und produziert kaputten Output

**Current behavior:**
Wenn eine Skill-Description 1024 Zeichen überschreitet, wird sie bei exakt
1024 Zeichen abgeschnitten, unabhängig von Wortgrenzen. Das produziert
Descriptions, die mitten im Wort enden (z.B. "Use when the user wants to confi").

**Desired behavior:**
Truncation sollte an der letzten Wortgrenze vor 1024 Zeichen brechen
und "..." anhängen, um die Kürzung zu signalisieren.

**Key interfaces:**
- Das `description`-Feld des `SkillMetadata`-Typs — keine Type-Änderung nötig,
  aber die Validierungs-/Processing-Logik, die es befüllt, muss Wortgrenzen
  respektieren
- Jede Funktion, die SKILL.md-Frontmatter liest und die Description extrahiert

**Acceptance criteria:**
- [ ] Descriptions unter 1024 Zeichen bleiben unverändert
- [ ] Descriptions über 1024 Zeichen werden an der letzten Wortgrenze vor
      1024 Zeichen abgeschnitten
- [ ] Gekürzte Descriptions enden mit "..."
- [ ] Die Gesamtlänge inkl. "..." überschreitet 1024 Zeichen nicht

**Out of scope:**
- Das 1024-Zeichen-Limit selbst zu ändern
- Multi-Line-Description-Support
```

### Guter Agent Brief (Enhancement)

```markdown
## Agent Brief

**Category:** enhancement
**Summary:** `.out-of-scope/`-Directory-Support hinzufügen, um abgelehnte Feature-Requests zu tracken

**Current behavior:**
Wenn ein Feature-Request abgelehnt wird, wird das Issue mit einem `wontfix`-Label
und einem Comment geschlossen. Es gibt keine persistente Aufzeichnung der
Entscheidung oder der Begründung. Künftige ähnliche Requests erfordern, dass
der Maintainer sich an die vorherige Diskussion erinnert oder danach sucht.

**Desired behavior:**
Abgelehnte Feature-Requests sollten in `.out-of-scope/<concept>.md`-Files
dokumentiert werden, die die Entscheidung, Begründung und Links zu allen
Issues, die das Feature angefragt haben, festhalten. Beim Triagen neuer
Issues sollten diese Files auf Matches geprüft werden.

**Key interfaces:**
- Markdown-File-Format in `.out-of-scope/` — jedes File sollte eine
  `# Concept Name`-Heading, eine `**Decision:**`-Zeile, eine `**Reason:**`-Zeile
  und eine `**Prior requests:**`-Liste mit Issue-Links haben
- Der Triage-Workflow sollte alle `.out-of-scope/*.md`-Files früh lesen
  und eingehende Issues nach Konzept-Ähnlichkeit dagegen matchen

**Acceptance criteria:**
- [ ] Ein Feature als wontfix schließen erstellt/aktualisiert ein File in `.out-of-scope/`
- [ ] Das File enthält die Entscheidung, Begründung und Link zum geschlossenen Issue
- [ ] Wenn ein matchendes `.out-of-scope/`-File schon existiert, wird das neue Issue
      an seine "Prior requests"-Liste angehängt, statt ein Duplikat zu erstellen
- [ ] Während des Triagens werden bestehende `.out-of-scope/`-Files geprüft und
      angezeigt, wenn ein neues Issue auf eine frühere Ablehnung matcht

**Out of scope:**
- Automatisches Matching (Mensch bestätigt den Match)
- Wieder-Öffnen vorher abgelehnter Features
- Bug-Reports (nur Enhancement-Ablehnungen gehen in `.out-of-scope/`)
```

### Schlechter Agent Brief

```markdown
## Agent Brief

**Summary:** Fix den Triage-Bug

**What to do:**
Das Triage-Ding ist kaputt. Schau ins Main-File und fix es.
Die Funktion um Zeile 150 hat das Problem.

**Files to change:**
- src/triage/handler.ts (Zeile 150)
- src/types.ts (Zeile 42)
```

Das ist schlecht, weil:
- Keine Category
- Vage Beschreibung ("the triage thing is broken")
- Referenziert File-Pfade und Zeilennummern, die stale werden
- Keine Acceptance Criteria
- Keine Scope Boundaries
- Keine Beschreibung von Current vs Desired Behavior
