---
name: triage
description: Issues durch eine State Machine triagen, getrieben durch Triage Roles. Nutze, wenn der User ein Issue erstellen, Issues triagen, eingehende Bugs oder Feature-Requests reviewen, Issues für einen AFK-Agent vorbereiten oder den Issue-Workflow managen will.
---

# Triage

Issues im Projekt-Issue-Tracker durch eine kleine State Machine aus Triage Roles bewegen.

Jedes Comment oder Issue, das während der Triage im Issue Tracker gepostet wird, **muss** mit diesem Disclaimer starten:

```
> *Das wurde während der Triage von KI generiert.*
```

## Referenz-Docs

- [AGENT-BRIEF.md](AGENT-BRIEF.md) - wie man durable Agent Briefs schreibt
- [OUT-OF-SCOPE.md](OUT-OF-SCOPE.md) - wie die `.out-of-scope/` Knowledge Base funktioniert

## Rollen

Zwei **Category** Rollen:

- `bug` - etwas ist kaputt
- `enhancement` - neues Feature oder Verbesserung

Fünf **State** Rollen:

- `needs-triage` - Maintainer muss bewerten
- `needs-info` - wartet auf Reporter für mehr Infos
- `ready-for-agent` - voll spezifiziert, ready für AFK Agent
- `ready-for-human` - braucht menschliche Implementation
- `wontfix` - wird nicht angegangen

Jedes triagierte Issue sollte genau eine Category Role und eine State Role tragen. Wenn State Roles in Konflikt stehen, flag es und frag den Maintainer, bevor du sonst was tust.

Das sind kanonische Rollennamen - die tatsächlichen Label-Strings im Issue Tracker können abweichen. Das Mapping sollte dir mitgegeben worden sein - falls nicht, `/setup-matt-pocock-skills` ausführen.

State Transitions: ein unlabeltes Issue geht normalerweise erst zu `needs-triage`; von dort bewegt es sich zu `needs-info`, `ready-for-agent`, `ready-for-human` oder `wontfix`. `needs-info` geht zurück zu `needs-triage`, sobald der Reporter antwortet. Der Maintainer kann jederzeit overriden - flag ungewöhnlich aussehende Transitions und frag, bevor du weitermachst.

## Invocation

Der Maintainer ruft `/triage` und beschreibt in natürlicher Sprache, was er will. Interpretier die Anfrage und handle. Beispiele:

- "Zeig mir alles, was meine Aufmerksamkeit braucht"
- "Lass uns #42 anschauen"
- "Move #42 to ready-for-agent"
- "Was ist ready für Agenten zum Aufnehmen?"

## Zeig, was Aufmerksamkeit braucht

Den Issue Tracker abfragen und drei Buckets präsentieren, älteste zuerst:

1. **Unlabeled** - nie triagiert.
2. **`needs-triage`** - Evaluation läuft.
3. **`needs-info` mit Reporter-Aktivität seit den letzten Triage Notes** - braucht Re-Evaluation.

Counts und einzeilige Summary pro Issue zeigen. Lass den Maintainer wählen.

## Ein spezifisches Issue triagen

1. **Kontext sammeln.** Das volle Issue lesen (Body, Comments, Labels, Reporter, Daten). Bisherige Triage Notes parsen, damit du keine gelösten Fragen nochmal stellst. Codebase mit dem Domain-Glossar des Projekts erkunden, ADRs im Bereich respektieren. `.out-of-scope/*.md` lesen und jede frühere Rejection rausbringen, die diesem Issue ähnelt.

2. **Empfehlen.** Sag dem Maintainer deine Category- und State-Empfehlung mit Begründung, plus eine kurze Codebase-Zusammenfassung relevant zum Issue. Warte auf Direktive.

3. **Reproduzieren (nur Bugs).** Vor jedem Grilling Reproduktion versuchen: die Schritte des Reporters lesen, den relevanten Code tracen, Tests oder Commands laufen lassen. Berichte, was passierte - erfolgreicher Repro mit Code-Path, gefehlter Repro oder unzureichende Details (starkes `needs-info` Signal). Ein bestätigter Repro macht den Agent Brief deutlich stärker.

4. **Grill (falls nötig).** Wenn das Issue Ausarbeitung braucht, eine `/grill-with-docs` Session laufen lassen.

5. **Outcome anwenden:**
   - `ready-for-agent` - einen Agent-Brief-Comment posten ([AGENT-BRIEF.md](AGENT-BRIEF.md)).
   - `ready-for-human` - gleiche Struktur wie ein Agent Brief, aber notier, warum es nicht delegierbar ist (Judgment Calls, externer Zugriff, Design-Entscheidungen, manuelles Testing).
   - `needs-info` - Triage Notes posten (Template unten).
   - `wontfix` (Bug) - höfliche Erklärung, dann schließen.
   - `wontfix` (Enhancement) - in `.out-of-scope/` schreiben, aus einem Comment darauf linken, dann schließen ([OUT-OF-SCOPE.md](OUT-OF-SCOPE.md)).
   - `needs-triage` - die Rolle anwenden. Optionaler Comment, wenn es partiellen Fortschritt gibt.

## Quick State Override

Wenn der Maintainer sagt "move #42 nach ready-for-agent", vertrau ihm und wende die Rolle direkt an. Bestätig, was du tun wirst (Rollen-Änderungen, Comment, Close), dann handle. Skip Grilling. Wenn du nach `ready-for-agent` bewegst ohne Grilling-Session, frag, ob er einen Agent Brief schreiben lassen will.

## Needs-Info Template

```markdown
## Triage Notes

**Was wir bisher festgestellt haben:**

- Punkt 1
- Punkt 2

**Was wir noch von dir brauchen (@reporter):**

- Frage 1
- Frage 2
```

Cap alles, was während des Grillings aufgelöst wurde, unter "Was wir bisher festgestellt haben", damit die Arbeit nicht verloren geht. Fragen müssen spezifisch und actionable sein, nicht "bitte mehr Infos".

## Vorherige Session fortsetzen

Wenn vorige Triage Notes am Issue existieren, lies sie, prüf, ob der Reporter offene Fragen beantwortet hat, und präsentier ein aktualisiertes Bild, bevor du weitermachst. Stell keine gelösten Fragen erneut.
