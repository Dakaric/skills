# Matt Pocock Skills

Eine Sammlung von Agent-Skills (Slash-Commands und Verhalten), die von Claude Code geladen werden. Skills sind in Buckets organisiert und werden über die per-Repo-Konfiguration konsumiert, die `/setup-matt-pocock-skills` erzeugt.

## Sprache

**Issue Tracker**:
Das Tool, das die Issues eines Repos hostet — GitHub Issues, Linear, eine lokale `.scratch/` Markdown-Konvention oder Ähnliches. Skills wie `to-issues`, `to-prd`, `triage` und `qa` lesen daraus und schreiben hinein.
_Vermeiden_: Backlog Manager, Backlog Backend, Issue Host

**Issue**:
Eine einzelne getrackte Arbeitseinheit innerhalb eines **Issue Trackers** — ein Bug, Task, PRD oder Slice, der von `to-issues` produziert wird.
_Vermeiden_: Ticket (nur verwenden, wenn externe Systeme zitiert werden, die das so nennen)

**Triage Role**:
Ein kanonisches State-Machine-Label, das während der Triage auf ein **Issue** angewendet wird (z.B. `needs-triage`, `ready-for-afk`). Jede Rolle wird über `docs/agents/triage-labels.md` auf einen echten Label-String im **Issue Tracker** gemappt.

## Beziehungen

- Ein **Issue Tracker** hält viele **Issues**
- Ein **Issue** trägt zu einer Zeit eine **Triage Role**

## Markierte Mehrdeutigkeiten

- "Backlog" wurde früher sowohl für das *Tool*, das Issues hostet, als auch für die *Menge an Arbeit* darin verwendet — aufgelöst: das Tool ist der **Issue Tracker**; "Backlog" wird nicht mehr als Domain-Begriff genutzt.
- "Backlog Backend" / "Backlog Manager" — aufgelöst: zusammengefasst zu **Issue Tracker**.
