---
name: scaffold-exercises
description: Exercise-Verzeichnisstrukturen mit Sections, Problems, Solutions und Explainern anlegen, die Linting bestehen. Nutze, wenn der User Exercises scaffolden, Exercise-Stubs anlegen oder eine neue Course-Section aufsetzen will.
---

# Scaffold Exercises

Exercise-Verzeichnisstrukturen anlegen, die `pnpm ai-hero-cli internal lint` bestehen, dann mit `git commit` committen.

## Verzeichnis-Naming

- **Sections**: `XX-section-name/` innerhalb `exercises/` (z.B. `01-retrieval-skill-building`)
- **Exercises**: `XX.YY-exercise-name/` innerhalb einer Section (z.B. `01.03-retrieval-with-bm25`)
- Section-Nummer = `XX`, Exercise-Nummer = `XX.YY`
- Namen sind Dash-Case (lowercase, Bindestriche)

## Exercise-Varianten

Jedes Exercise braucht mindestens eines dieser Subfolder:

- `problem/` - Student-Workspace mit TODOs
- `solution/` - Referenz-Implementation
- `explainer/` - konzeptuelles Material, keine TODOs

Beim Stubben default zu `explainer/`, außer der Plan spezifiziert anders.

## Required Files

Jeder Subfolder (`problem/`, `solution/`, `explainer/`) braucht eine `readme.md`, die:

- **Nicht leer** ist (muss echten Content haben, eine einzelne Title-Line reicht)
- Keine kaputten Links hat

Beim Stubben eine minimale Readme mit Title und Beschreibung anlegen:

```md
# Exercise-Titel

Beschreibung hier
```

Wenn der Subfolder Code hat, braucht er auch eine `main.ts` (>1 Line). Aber für Stubs ist ein Readme-only Exercise okay.

## Workflow

1. **Plan parsen** - Section-Namen, Exercise-Namen und Variant-Typen extrahieren
2. **Verzeichnisse anlegen** - `mkdir -p` für jeden Pfad
3. **Stub-Readmes anlegen** - eine `readme.md` pro Variant-Folder mit einem Titel
4. **Lint laufen lassen** - `pnpm ai-hero-cli internal lint` zum Validieren
5. **Etwaige Fehler fixen** - iterieren, bis Lint passt

## Lint-Regeln zusammengefasst

Der Linter (`pnpm ai-hero-cli internal lint`) prüft:

- Jedes Exercise hat Subfolder (`problem/`, `solution/`, `explainer/`)
- Mindestens eines von `problem/`, `explainer/` oder `explainer.1/` existiert
- `readme.md` existiert und ist nicht leer im primären Subfolder
- Keine `.gitkeep` Files
- Keine `speaker-notes.md` Files
- Keine kaputten Links in Readmes
- Keine `pnpm run exercise` Commands in Readmes
- `main.ts` pro Subfolder erforderlich, außer Readme-only

## Exercises verschieben / umbenennen

Beim Renumbern oder Verschieben:

1. `git mv` (nicht `mv`) zum Umbenennen der Verzeichnisse - behält Git-History
2. Den numerischen Prefix updaten, um die Ordnung zu erhalten
3. Lint nach Moves nochmal laufen lassen

Beispiel:

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## Beispiel: aus einem Plan stubben

Gegeben ein Plan wie:

```
Section 05: Memory Skill Building
- 05.01 Introduction to Memory
- 05.02 Short-term Memory (explainer + problem + solution)
- 05.03 Long-term Memory
```

Erstellen:

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

Dann Readme-Stubs anlegen:

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# Introduction to Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# Long-term Memory"
```
