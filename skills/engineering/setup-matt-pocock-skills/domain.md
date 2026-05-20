# Domain Docs

Wie die Engineering-Skills die Domain-Dokumentation dieses Repos beim Codebase-Explore konsumieren sollen.

## Vor dem Explore lesen

- **`CONTEXT.md`** im Repo-Root, oder
- **`CONTEXT-MAP.md`** im Repo-Root, falls existent - sie zeigt auf eine `CONTEXT.md` pro Context. Jede, die zum Thema gehört, lesen.
- **`docs/adr/`** - ADRs lesen, die den Bereich treffen, in dem du gleich arbeitest. In Multi-Context-Repos auch `src/<context>/docs/adr/` für context-scoped Entscheidungen prüfen.

Wenn eines dieser Files nicht existiert, **stillschweigend weitergehen**. Flagge ihre Abwesenheit nicht; schlag nicht vorab vor, sie anzulegen. Der Producer-Skill (`/grill-with-docs`) erstellt sie lazy, wenn Begriffe oder Entscheidungen tatsächlich aufgelöst werden.

## File-Struktur

Single-Context-Repo (die meisten Repos):

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-Context-Repo (Existenz von `CONTEXT-MAP.md` im Root):

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← systemweite Entscheidungen
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← context-spezifische Entscheidungen
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## Das Glossar-Vokabular nutzen

Wenn dein Output ein Domain-Konzept benennt (in einem Issue-Title, einem Refactor-Vorschlag, einer Hypothese, einem Test-Namen), nutz den Begriff, wie er in `CONTEXT.md` definiert ist. Drift nicht zu Synonymen, die das Glossar explizit vermeidet.

Wenn das Konzept, das du brauchst, noch nicht im Glossar ist, ist das ein Signal - entweder erfindest du Sprache, die das Projekt nicht nutzt (überdenken), oder es gibt eine echte Lücke (notier für `/grill-with-docs`).

## ADR-Konflikte flaggen

Wenn dein Output einem bestehenden ADR widerspricht, leg's explizit offen, statt es still zu überschreiben:

> _Widerspricht ADR-0007 (event-sourced orders) — aber wert wieder aufzumachen, weil…_
