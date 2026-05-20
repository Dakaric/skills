# ADR-Format

ADRs liegen in `docs/adr/` und nutzen sequenzielles Numbering: `0001-slug.md`, `0002-slug.md`, etc.

Das `docs/adr/` Verzeichnis lazy anlegen - nur wenn das erste ADR gebraucht wird.

## Template

```md
# {Kurzer Titel der Entscheidung}

{1-3 Sätze: was ist der Kontext, was haben wir entschieden, und warum.}
```

Das war's. Ein ADR kann ein einzelner Absatz sein. Der Wert liegt darin festzuhalten, *dass* eine Entscheidung getroffen wurde und *warum* - nicht im Ausfüllen von Sections.

## Optionale Sections

Nur einbauen, wenn sie echten Mehrwert bringen. Die meisten ADRs brauchen sie nicht.

- **Status** im Frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`) - nützlich, wenn Entscheidungen überdacht werden
- **Considered Options** - nur wenn die verworfenen Alternativen erwähnenswert sind
- **Consequences** - nur wenn nicht-offensichtliche Downstream-Effekte herausgehoben werden müssen

## Numbering

`docs/adr/` nach der höchsten existierenden Nummer scannen und um eins erhöhen.

## Wann ein ADR anbieten

Alle drei Punkte müssen zutreffen:

1. **Schwer rückgängig zu machen** - die Kosten, später umzudenken, sind relevant
2. **Überraschend ohne Kontext** - ein zukünftiger Leser schaut auf den Code und fragt sich "warum zur Hölle haben die das so gemacht?"
3. **Resultat eines echten Trade-offs** - es gab echte Alternativen und du hast eine aus konkreten Gründen gewählt

Wenn eine Entscheidung leicht zu reversen ist, lass es - du wirst sie eh reverten. Wenn sie nicht überraschend ist, wird sich niemand wundern. Wenn es keine echte Alternative gab, gibt's nichts festzuhalten außer "wir haben das Offensichtliche getan".

### Was qualifiziert

- **Architektonische Form.** "Wir nutzen einen Monorepo." "Das Write-Modell ist Event-Sourced, das Read-Modell wird in Postgres projiziert."
- **Integration Patterns zwischen Contexts.** "Ordering und Billing kommunizieren über Domain-Events, nicht über synchrones HTTP."
- **Technologie-Entscheidungen, die Lock-in bringen.** Datenbank, Message Bus, Auth-Provider, Deployment-Target. Nicht jede Library - nur die, die ein Quartal Aufwand zum Tauschen wären.
- **Boundary- und Scope-Entscheidungen.** "Customer-Daten gehören dem Customer-Context; andere Contexts referenzieren sie nur per ID." Die expliziten Nein-s sind genauso wertvoll wie die Ja-s.
- **Bewusste Abweichungen vom offensichtlichen Weg.** "Wir nutzen manuelles SQL statt eines ORM, weil X." Alles, wo ein vernünftiger Leser das Gegenteil annehmen würde. Diese verhindern, dass der nächste Engineer etwas "fixt", das bewusst so war.
- **Constraints, die im Code nicht sichtbar sind.** "Wir können AWS nicht nutzen wegen Compliance-Anforderungen." "Response-Zeiten müssen unter 200ms liegen wegen des Partner-API-Vertrags."
- **Verworfene Alternativen, wenn die Verwerfung nicht offensichtlich ist.** Wenn du GraphQL erwogen und REST aus subtilen Gründen gewählt hast, halt's fest - sonst schlägt jemand in sechs Monaten wieder GraphQL vor.
