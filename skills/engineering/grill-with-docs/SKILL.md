---
name: grill-with-docs
description: Grilling-Session in Fragerunden, die deinen Plan gegen das bestehende Domain-Modell prüft, Terminologie schärft und Dokumentation (CONTEXT.md, ADRs) inline aktualisiert, sobald Entscheidungen sich verfestigen, wenn du einen Plan gegen Sprache und dokumentierte Entscheidungen deines Projekts stressen willst.
---

<what-to-do>

Interviewe mich unerbittlich zu jedem Aspekt dieses Plans, bis wir ein geteiltes Verständnis erreichen. Geh jeden Zweig des Design-Trees durch und löse Abhängigkeiten zwischen Entscheidungen Stück für Stück auf. Gib zu jeder Frage deine empfohlene Antwort an.

Wenn eine Frage durch Exploration der Codebase beantwortet werden kann, erkunde stattdessen die Codebase.

</what-to-do>

<runden>

## Fragen in Runden stellen

Gefragt wird in Runden, nicht einzeln. Eine Runde enthält alle Fragen, die gerade unabhängig voneinander entscheidbar sind. Eine Frage, deren Form von einer offenen Antwort abhängt, wartet auf die nächste Runde. So wenige Runden, wie die Abhängigkeiten erlauben.

**Ablauf je Runde:**

1. Lies die Codebase weiter, bis nur noch Fragen übrig sind, die der User entscheiden muss.
2. Lade den Skill `aufgaben`, er regelt Anlegen, Warten und Antworten. Lege einen Punkt an: Stufe `jetzt`, `blockiert` nennt den Plan, der wartet, `antwort_an` ist „Grill-Session <Plan>“ (nur damit zeigt das Cockpit den Knopf „Erledigt und senden“). `projekt` ist der Projektname aus einem offenen Punkt desselben Repos, sonst der Repo-Name.
   - `titel`: „Grill <Plan>: Runde <n>, <k> Fragen“ (bei k = 1 „1 Frage“)
   - `kontext`: die Fragen nummeriert (F1, F2, …), je Frage zwei, drei Sätze Lage und die Optionen
   - `antwort`: je Frage eine Zeile `F<n>: <Empfehlung>`, höchstens 1200 Zeichen, damit im Notizfeld Platz für Änderungen bleibt
   - `empfehlung`: ein Satz, dass die Zeilen geändert oder stehen gelassen und mit „Erledigt und senden“ abgeschickt werden
3. Starte den Warte-Befehl im Hintergrund und werte das Ereignis so aus:
   - `erledigt`: Lies `erledigt_notiz` zeilenweise nach `F<n>:`. Eine unveränderte Zeile ist angenommen, eine geänderte gilt mit dem neuen Wortlaut. Eine fehlende oder unklare Zeile wird nicht geraten, sie kommt in die nächste Runde. Zeilen ohne `F<n>:` sind Kommentare und fließen in die Entscheidungen ein. Ist die Notiz leer, frag im Terminal nach, statt dieselbe Runde neu zu stellen.
   - `antwort` (der User schreibt, ohne abzuhaken): Lies die Texte nach `F<n>:`-Zeilen, die gelten wie in `erledigt`, und beantworte Rückfragen. Der Punkt bleibt offen, du startest den Warte-Befehl mit `--nach-antwort` neu. Ändere den Punkt nicht per `PATCH`, ein offenes Notizfeld übernimmt das nicht.
4. Ziehe `CONTEXT.md` und ADRs nach, bevor du die nächste Runde baust.

Grenzen des Cockpits: `titel` 200 Zeichen, `kontext` 8000, `antwort` und `empfehlung` je 2000. Passt eine Runde nicht hinein, teile sie in zwei Punkte, kürze nicht. Die F-Nummern laufen über beide Punkte weiter, die Titel enden auf „Teil 1“ und „Teil 2“.

Zum Schluss fasst du die Entscheidungen im Terminal zusammen.

**Orca-Worker** (Präambel mit Task- und Dispatch-ID) legen keinen Punkt selbst an. Sie schicken `titel`, `kontext`, `antwort` und `empfehlung` im Format oben per `orca orchestration ask` an den Koordinator und bitten darum, `erledigt_notiz` wörtlich zurückzugeben. Einen Rückfall ins Terminal gibt es für sie nicht.

**Rückfall Terminal:** Scheitert das Anlegen an der Verbindung (curl scheitert, 5xx) oder will der User ausdrücklich im Terminal gegrillt werden, stellst du die Fragen eine nach der anderen und wartest jeweils auf Feedback. Bei 422 korrigierst du das genannte Feld, bei 409 gilt `aufgaben`.

</runden>

<supporting-info>

## Domain-Awareness

Während der Codebase-Exploration auch nach existierender Dokumentation suchen:

### File-Struktur

Die meisten Repos haben einen einzelnen Context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

Wenn eine `CONTEXT-MAP.md` im Root existiert, hat das Repo mehrere Contexts. Die Map zeigt, wo jeder liegt:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← systemweite Entscheidungen
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-spezifische Entscheidungen
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Files lazy anlegen - nur wenn du etwas zu schreiben hast. Wenn keine `CONTEXT.md` existiert, leg eine an, sobald der erste Begriff aufgelöst wird. Wenn kein `docs/adr/` existiert, leg es an, wenn das erste ADR gebraucht wird.

## Während der Session

### Gegen das Glossar challengen

Wenn der User einen Begriff verwendet, der mit der bestehenden Sprache in `CONTEXT.md` kollidiert, ruf das sofort raus. "Dein Glossar definiert 'cancellation' als X, aber du scheinst Y zu meinen — was denn jetzt?"

### Unscharfe Sprache schärfen

Wenn der User vage oder überladene Begriffe nutzt, schlag einen präzisen kanonischen Begriff vor. "Du sagst 'account' — meinst du den Customer oder den User? Das sind verschiedene Dinge."

### Konkrete Szenarien diskutieren

Wenn Domain-Beziehungen diskutiert werden, stress-test sie mit spezifischen Szenarien. Erfinde Szenarien, die Edge Cases proben und den User zwingen, präzise zu sein bei den Grenzen zwischen Konzepten.

### Mit Code abgleichen

Wenn der User aussagt, wie etwas funktioniert, prüf, ob der Code zustimmt. Wenn du einen Widerspruch findest, leg ihn offen: "Dein Code cancelt ganze Orders, aber du hast grad gesagt, partielle Cancellation ist möglich — was stimmt?"

### CONTEXT.md inline updaten

Wenn ein Begriff aufgelöst ist, update `CONTEXT.md` direkt dort. Sammel das nicht an - cap es, sobald es passiert. Format wie in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` sollte komplett frei von Implementierungsdetails sein. Behandle `CONTEXT.md` nicht als Spec, Scratch Pad oder Ablage für Implementierungsentscheidungen. Es ist ein Glossar und nichts anderes.

### ADRs sparsam anbieten

Biete nur dann an, ein ADR zu erstellen, wenn alle drei Punkte zutreffen:

1. **Schwer rückgängig zu machen** - die Kosten, später umzudenken, sind relevant
2. **Überraschend ohne Kontext** - ein zukünftiger Leser wird sich fragen "warum haben die das so gemacht?"
3. **Resultat eines echten Trade-offs** - es gab echte Alternativen und du hast eine aus konkreten Gründen gewählt

Wenn einer der drei fehlt, lass das ADR weg. Format wie in [ADR-FORMAT.md](./ADR-FORMAT.md).

</supporting-info>
