---
name: setup-matt-pocock-skills
description: Setzt einen `## Agent skills` Block in AGENTS.md/CLAUDE.md und `docs/agents/` auf, damit die Engineering-Skills den Issue Tracker des Repos (GitHub oder lokales Markdown), das Triage-Label-Vokabular und das Domain-Doc-Layout kennen. Vor dem ersten Einsatz von `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture` oder `zoom-out` ausführen - oder wenn diese Skills Kontext zum Issue Tracker, zu Triage-Labels oder Domain-Docs zu fehlen scheint.
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

Die per-Repo-Konfiguration scaffolden, die die Engineering-Skills voraussetzen:

- **Issue Tracker** - wo Issues leben (GitHub per Default; lokales Markdown wird out of the box unterstützt)
- **Triage Labels** - die Strings, die für die fünf kanonischen Triage Roles genutzt werden
- **Domain Docs** - wo `CONTEXT.md` und ADRs leben und die Consumer-Regeln, um sie zu lesen

Das ist ein prompt-getriebener Skill, kein deterministisches Script. Explorier, präsentier, was du gefunden hast, bestätig mit dem User, dann schreib.

## Prozess

### 1. Explore

Schau ins aktuelle Repo, um den Startzustand zu verstehen. Lies, was existiert; nimm nichts an:

- `git remote -v` und `.git/config` - ist das ein GitHub-Repo? Welches?
- `AGENTS.md` und `CLAUDE.md` im Repo-Root - existiert eines? Gibt's schon einen `## Agent skills` Abschnitt in einer?
- `CONTEXT.md` und `CONTEXT-MAP.md` im Repo-Root
- `docs/adr/` und etwaige `src/*/docs/adr/` Verzeichnisse
- `docs/agents/` - existiert der vorherige Output dieses Skills schon?
- `.scratch/` - Zeichen, dass eine Local-Markdown-Issue-Tracker-Konvention schon im Einsatz ist

### 2. Findings präsentieren und fragen

Fass zusammen, was da ist und was fehlt. Dann führ den User durch die drei Entscheidungen **einzeln** - eine Section präsentieren, Antwort vom User bekommen, dann zur nächsten. Schmeiß nicht alle drei auf einmal raus.

Geh davon aus, dass der User nicht weiß, was diese Begriffe bedeuten. Jede Section startet mit einer kurzen Erklärung (was es ist, warum diese Skills es brauchen, was sich ändert, wenn sie anders wählen). Dann die Auswahlmöglichkeiten und den Default zeigen.

**Section A — Issue Tracker.**

> Erklärung: Der "Issue Tracker" ist, wo Issues für dieses Repo leben. Skills wie `to-issues`, `triage`, `to-prd` und `qa` lesen daraus und schreiben hinein - sie müssen wissen, ob sie `gh issue create` aufrufen, ein Markdown-File unter `.scratch/` schreiben oder einem anderen Workflow folgen, den du beschreibst. Wähl den Ort, an dem du tatsächlich Arbeit für dieses Repo trackst.

Default-Haltung: diese Skills wurden für GitHub designt. Wenn ein `git remote` auf GitHub zeigt, schlag das vor. Wenn ein `git remote` auf GitLab zeigt (`gitlab.com` oder ein selbstgehosteter Host), schlag GitLab vor. Sonst (oder wenn der User es bevorzugt), biete an:

- **GitHub** - Issues leben in den GitHub Issues des Repos (nutzt das `gh` CLI)
- **GitLab** - Issues leben in den GitLab Issues des Repos (nutzt das [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local Markdown** - Issues leben als Files unter `.scratch/<feature>/` in diesem Repo (gut für Solo-Projekte oder Repos ohne Remote)
- **Other** (Jira, Linear etc.) - bitte den User, den Workflow in einem Absatz zu beschreiben; der Skill hält es als freiformulierte Prosa fest

**Section B — Triage-Label-Vokabular.**

> Erklärung: Wenn der `triage` Skill ein eingehendes Issue verarbeitet, bewegt er es durch eine State Machine - braucht Bewertung, wartet auf Reporter, ready für einen AFK-Agent, ready für einen Menschen oder wontfix. Dafür muss er Labels (oder das Äquivalent in deinem Issue Tracker) anwenden, die zu Strings passen, die *du tatsächlich konfiguriert hast*. Wenn dein Repo schon andere Label-Namen nutzt (z.B. `bug:triage` statt `needs-triage`), map sie hier, damit der Skill die richtigen anwendet, statt Duplikate zu erzeugen.

Die fünf kanonischen Rollen:

- `needs-triage` - Maintainer muss bewerten
- `needs-info` - wartet auf Reporter
- `ready-for-agent` - voll spezifiziert, AFK-ready (ein Agent kann es ohne menschlichen Kontext aufnehmen)
- `ready-for-human` - braucht menschliche Implementation
- `wontfix` - wird nicht angegangen

Default: der String jeder Rolle entspricht ihrem Namen. Frag den User, ob er welche überschreiben will. Wenn sein Issue Tracker keine bestehenden Labels hat, sind die Defaults okay.

**Section C — Domain Docs.**

> Erklärung: Manche Skills (`improve-codebase-architecture`, `diagnose`, `tdd`) lesen eine `CONTEXT.md`, um die Domain-Sprache des Projekts zu lernen, und `docs/adr/` für vergangene architektonische Entscheidungen. Sie müssen wissen, ob das Repo einen globalen Context hat oder mehrere (z.B. ein Monorepo mit separaten Frontend-/Backend-Contexts), damit sie am richtigen Ort schauen.

Bestätig das Layout:

- **Single-Context** - eine `CONTEXT.md` + `docs/adr/` im Repo-Root. Die meisten Repos sind das.
- **Multi-Context** - `CONTEXT-MAP.md` im Root, die auf per-Context `CONTEXT.md` Files zeigt (typisch ein Monorepo).

### 3. Bestätigen und editieren

Zeig dem User einen Draft von:

- Dem `## Agent skills` Block, der in eine von `CLAUDE.md` / `AGENTS.md` gehört, je nachdem welche editiert wird (Auswahlregeln in Step 4)
- Den Inhalten von `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, `docs/agents/domain.md`

Lass sie editieren, bevor geschrieben wird.

### 4. Schreiben

**Wähl die zu editierende Datei:**

- Wenn `CLAUDE.md` existiert, editier sie.
- Sonst wenn `AGENTS.md` existiert, editier sie.
- Wenn keine existiert, frag den User, welche angelegt werden soll - wähl nicht für ihn.

Erstell nie `AGENTS.md`, wenn `CLAUDE.md` schon existiert (oder umgekehrt) - editier immer die, die schon da ist.

Wenn ein `## Agent skills` Block schon in der gewählten Datei existiert, update seine Inhalte in-place, statt ein Duplikat anzuhängen. Überschreib keine User-Edits an den umgebenden Sections.

Der Block:

```markdown
## Agent skills

### Issue tracker

[Ein-Zeilen-Zusammenfassung, wo Issues getrackt werden]. Siehe `docs/agents/issue-tracker.md`.

### Triage labels

[Ein-Zeilen-Zusammenfassung des Label-Vokabulars]. Siehe `docs/agents/triage-labels.md`.

### Domain docs

[Ein-Zeilen-Zusammenfassung des Layouts — "single-context" oder "multi-context"]. Siehe `docs/agents/domain.md`.
```

Dann schreib die drei Doc-Files mit den Seed-Templates in diesem Skill-Ordner als Ausgangspunkt:

- [issue-tracker-github.md](./issue-tracker-github.md) - GitHub Issue Tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) - GitLab Issue Tracker
- [issue-tracker-local.md](./issue-tracker-local.md) - Local-Markdown Issue Tracker
- [triage-labels.md](./triage-labels.md) - Label-Mapping
- [domain.md](./domain.md) - Domain-Doc-Consumer-Regeln + Layout

Für "andere" Issue Tracker `docs/agents/issue-tracker.md` aus der Beschreibung des Users von Grund auf schreiben.

### 5. Fertig

Sag dem User, dass das Setup komplett ist und welche Engineering-Skills jetzt aus diesen Files lesen. Erwähn, dass er `docs/agents/*.md` später direkt editieren kann - diesen Skill nochmal laufen lassen ist nur nötig, wenn er den Issue Tracker wechseln oder von Null neustarten will.
