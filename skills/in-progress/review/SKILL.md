---
name: review
description: Reviewt die Änderungen seit einem fixen Punkt (Commit, Branch, Tag oder Merge-Base) entlang zweier Achsen - Standards (folgt der Code den dokumentierten Coding-Standards dieses Repos?) und Spec (matcht der Code das, was das ausgangsgebende Issue / PRD verlangt hat?). Lässt beide Reviews in parallelen Sub-Agents laufen und reportet sie nebeneinander. Nutze, wenn der User einen Branch, einen PR, Work-in-Progress-Änderungen reviewen will oder "review since X" fragt.
---

# Review

Zwei-Achsen-Review des Diffs zwischen `HEAD` und einem fixen Punkt, den der User liefert:

- **Standards** - folgt der Code den dokumentierten Coding-Standards dieses Repos?
- **Spec** - implementiert der Code treu das ausgangsgebende Issue / PRD / Spec?

Beide Achsen laufen als **parallele Sub-Agents**, damit sie sich nicht gegenseitig den Kontext verseuchen, dann aggregiert dieser Skill ihre Findings.

Der Issue Tracker sollte dir mitgegeben worden sein - falls `docs/agents/issue-tracker.md` fehlt, `/setup-matt-pocock-skills` ausführen.

## Prozess

### 1. Fixen Punkt pinnen

Was der User gesagt hat, ist der fixe Punkt - ein Commit-SHA, Branch-Name, Tag, `main`, `HEAD~5` etc. Sei nicht meinungsstark; reich's durch. Wenn er nichts spezifiziert hat, frag: "Wogegen reviewen — einen Branch, einen Commit oder `main`?" Geh nicht weiter, bis du ihn hast.

Cap den Diff-Command einmal: `git diff <fixed-point>...HEAD` (drei Punkte, damit der Vergleich gegen die Merge-Base läuft). Auch die Liste der Commits per `git log <fixed-point>..HEAD --oneline` notieren.

### 2. Spec-Quelle identifizieren

Such die ausgangsgebende Spec, in dieser Reihenfolge:

1. Issue-Referenzen in den Commit-Messages (`#123`, `Closes #45`, GitLab `!67` etc.) - via Workflow in `docs/agents/issue-tracker.md` fetchen.
2. Einen Pfad, den der User als Argument übergeben hat.
3. Ein PRD- / Spec-File unter `docs/`, `specs/` oder `.scratch/`, das zum Branch-Namen oder Feature matcht.
4. Wenn nichts gefunden, frag den User, wo die Spec ist. Wenn er sagt, es gibt keine, skippt der **Spec** Sub-Agent und reportet "no spec available".

### 3. Standards-Quellen identifizieren

Alles im Repo, das dokumentiert, wie Code geschrieben werden soll. Übliche Orte:

- `CLAUDE.md`, `AGENTS.md`
- `CONTRIBUTING.md`
- `CONTEXT.md`, `CONTEXT-MAP.md`, per-Context `CONTEXT.md` Files
- `docs/adr/` (architektonische Entscheidungen sind Standards)
- `.editorconfig`, `eslint.config.*`, `biome.json`, `prettier.config.*`, `tsconfig.json` (maschinell durchgesetzte Standards - notieren, aber nicht doppeln, was Tooling schon checkt)
- Jede `STYLE.md`, `STANDARDS.md`, `STYLEGUIDE.md` oder Ähnliches im Repo-Root oder unter `docs/`

Die Liste der Files sammeln. Der **Standards** Sub-Agent wird sie lesen.

### 4. Beide Sub-Agents parallel spawnen

Eine einzelne Message mit zwei `Agent`-Tool-Calls senden. Nutz den `general-purpose` Subagent für beide.

**Standards-Sub-Agent-Prompt** - enthält:

- Den vollen Diff-Command und die Commit-Liste.
- Die Liste der Standards-Source-Files, die du in Step 3 gefunden hast.
- Der Brief: "Lies die Standards-Docs. Dann lies das Diff. Reporte — wo relevant pro File/Hunk — jede Stelle, an der das Diff einen dokumentierten Standard verletzt. Zitier den Standard (File + die Regel). Unterscheid harte Verletzungen von Judgement Calls. Skip alles, was Tooling enforced. Unter 400 Wörtern."

**Spec-Sub-Agent-Prompt** - enthält:

- Den Diff-Command und die Commit-Liste.
- Den Pfad oder den geholten Inhalt der Spec.
- Der Brief: "Lies die Spec. Dann lies das Diff. Reporte: (a) Anforderungen, die die Spec verlangt hat und die fehlen oder unvollständig sind; (b) Verhalten im Diff, das nicht verlangt war (Scope-Creep); (c) Anforderungen, die implementiert aussehen, wo die Implementation aber falsch wirkt. Zitier die Spec-Zeile für jedes Finding. Unter 400 Wörtern."

Wenn die Spec fehlt, skip den Spec-Sub-Agent und notier das im finalen Report.

### 5. Aggregieren

Die zwei Reports unter `## Standards` und `## Spec` Headings präsentieren, verbatim oder leicht aufgeräumt. Findings **nicht** mergen oder neu ranken - die zwei Achsen sind bewusst separat, damit der User sie unabhängig sieht.

Mit einer einzeiligen Summary enden: Gesamt-Findings pro Achse und das schlimmste einzelne Issue (falls eines geflaggt).

## Warum zwei Achsen

Eine Änderung kann eine Achse passen und an der anderen failen:

- Code, der jedem Standard folgt, aber das Falsche implementiert → **Standards pass, Spec fail.**
- Code, der genau das tut, was das Issue verlangt, aber die Konventionen des Projekts bricht → **Spec pass, Standards fail.**

Sie separat zu reporten verhindert, dass eine Achse die andere maskiert.
