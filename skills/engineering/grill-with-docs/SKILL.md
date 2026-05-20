---
name: grill-with-docs
description: Grilling-Session, die deinen Plan gegen das bestehende Domain-Modell prüft, Terminologie schärft und Dokumentation (CONTEXT.md, ADRs) inline aktualisiert, sobald Entscheidungen sich verfestigen. Nutze, wenn der User einen Plan gegen die Sprache und dokumentierten Entscheidungen seines Projekts stressen will.
---

<what-to-do>

Interviewe mich unerbittlich zu jedem Aspekt dieses Plans, bis wir ein geteiltes Verständnis erreichen. Geh jeden Zweig des Design-Trees durch und löse Abhängigkeiten zwischen Entscheidungen Stück für Stück auf. Gib zu jeder Frage deine empfohlene Antwort an.

Stell die Fragen eine nach der anderen und warte auf Feedback, bevor du weitergehst.

Wenn eine Frage durch Exploration der Codebase beantwortet werden kann, erkunde stattdessen die Codebase.

</what-to-do>

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
