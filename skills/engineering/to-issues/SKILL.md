---
name: to-issues
description: Zerleg einen Plan, eine Spec oder ein PRD in unabhängig greifbare Issues im Projekt-Issue-Tracker per Tracer-Bullet Vertical Slices. Nutze, wenn der User einen Plan in Issues umwandeln, Implementation-Tickets erstellen oder Arbeit in Issues runterbrechen will.
---

# To Issues

Einen Plan in unabhängig greifbare Issues per Vertical Slices (Tracer Bullets) zerlegen.

Der Issue Tracker und das Triage-Label-Vokabular sollten dir mitgegeben worden sein — falls nicht, `/setup-matt-pocock-skills` ausführen.

## Prozess

### 1. Kontext sammeln

Arbeite mit dem, was schon im Konversationskontext steht. Wenn der User eine Issue-Referenz (Issue-Nummer, URL oder Pfad) als Argument übergibt, hol es vom Issue Tracker und lies den vollen Body und die Comments.

### 2. Codebase erkunden (optional)

Wenn du die Codebase noch nicht erkundet hast, tu das, um den aktuellen Stand des Codes zu verstehen. Issue-Titel und -Beschreibungen sollten das Domain-Glossar-Vokabular des Projekts nutzen und ADRs im betroffenen Bereich respektieren.

### 3. Vertical Slices entwerfen

Den Plan in **Tracer-Bullet**-Issues zerlegen. Jedes Issue ist ein dünner Vertical Slice, der end-to-end durch ALLE Integrationsschichten schneidet, NICHT ein Horizontal Slice einer Schicht.

Slices können 'HITL' oder 'AFK' sein. HITL Slices brauchen menschliche Interaktion, z.B. eine architektonische Entscheidung oder ein Design-Review. AFK Slices können ohne menschliche Interaktion implementiert und gemerged werden. Bevorzug AFK gegenüber HITL, wo möglich.

<vertical-slice-rules>
- Jeder Slice liefert einen schmalen, aber VOLLSTÄNDIGEN Pfad durch jede Schicht (Schema, API, UI, Tests)
- Ein fertiger Slice ist eigenständig demobar oder verifizierbar
- Bevorzug viele dünne Slices gegenüber wenigen dicken
</vertical-slice-rules>

### 4. Den User abfragen

Präsentier die vorgeschlagene Aufteilung als nummerierte Liste. Für jeden Slice zeig:

- **Title**: kurzer beschreibender Name
- **Type**: HITL / AFK
- **Blocked by**: welche anderen Slices (falls überhaupt) zuerst fertig sein müssen
- **User stories covered**: welche User Stories das adressiert (falls das Quellmaterial welche hat)

Frag den User:

- Fühlt sich die Granularität richtig an? (zu grob / zu fein)
- Sind die Abhängigkeits-Beziehungen korrekt?
- Sollten Slices gemerged oder weiter gesplittet werden?
- Sind die richtigen Slices als HITL und AFK markiert?

Iterier, bis der User die Aufteilung absegnet.

### 5. Die Issues im Issue Tracker veröffentlichen

Für jeden genehmigten Slice ein neues Issue im Issue Tracker veröffentlichen. Nutz das Issue-Body-Template unten. Diese Issues gelten als ready für AFK Agents, also publish sie mit dem korrekten Triage-Label, außer anders instruiert.

Publish Issues in Dependency-Reihenfolge (Blockers zuerst), damit du echte Issue-Identifier im "Blocked by" Feld referenzieren kannst.

<issue-template>
## Parent

Eine Referenz auf das Parent-Issue im Issue Tracker (falls die Quelle ein bestehendes Issue war, ansonsten diesen Abschnitt weglassen).

## Was gebaut wird

Eine prägnante Beschreibung dieses Vertical Slice. Beschreib das End-to-End-Verhalten, keine Layer-by-Layer-Implementierung.

Vermeid konkrete Dateipfade oder Code-Snippets, die veralten schnell. Ausnahme: Wenn ein Prototyp ein Snippet produziert hat, das eine Entscheidung präziser kodiert als Prosa es kann (State Machine, Reducer, Schema, Type-Shape), inlinet es hier und notiert kurz, dass es aus einem Prototyp stammt. Auf die entscheidungsrelevanten Teile zuschneiden, kein lauffähiges Demo, nur die wichtigen Bits.

## Akzeptanzkriterien

- [ ] Kriterium 1
- [ ] Kriterium 2
- [ ] Kriterium 3

## Blocked by

- Eine Referenz auf das blockierende Ticket (falls vorhanden)

Oder "Keine - kann sofort starten", wenn keine Blocker da sind.

</issue-template>

Schließ oder modifizier KEIN Parent-Issue.
