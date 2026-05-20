Skills sind in Bucket-Ordnern unter `skills/` organisiert:

- `engineering/` — tägliche Code-Arbeit
- `productivity/` — tägliche Workflow-Tools ohne Code-Bezug
- `misc/` — wird behalten, aber selten genutzt
- `personal/` — an mein eigenes Setup gebunden, nicht beworben
- `in-progress/` — Drafts, noch nicht release-fertig
- `deprecated/` — nicht mehr in Verwendung

Jeder Skill in `engineering/`, `productivity/` oder `misc/` braucht eine Referenz in der Top-Level `README.md` und einen Eintrag in `.claude-plugin/plugin.json`. Skills in `personal/`, `in-progress/` und `deprecated/` dürfen in beiden nicht auftauchen.

Jeder Skill-Eintrag in der Top-Level `README.md` muss den Skill-Namen auf seine `SKILL.md` verlinken.

Jeder Bucket-Ordner hat eine `README.md`, die jeden Skill im Bucket mit einer einzeiligen Beschreibung listet, wobei der Skill-Name auf seine `SKILL.md` verlinkt ist.
